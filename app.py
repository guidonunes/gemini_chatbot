from flask import Flask, render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep
from helper import load_knowledge_base, save
from bot_persona import personas, select_persona
from history_manager import delete_old_messages, summarize_history

load_dotenv()


GEMINI_API = os.getenv("GEMINI_API")
MODEL = "gemini-2.5-flash"
genai.configure(api_key=GEMINI_API)


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

context = load_knowledge_base("data/satoshi_ai.txt")

def save_conversation():
    current_persona = "neutral"

    system_instruction = f"""
        {current_persona}

        ##PERSONA
        You are a Financial Advisor chatbot.
        You should only answer questions related to finance, budgeting, and investment markets.
        If the user asks about unrelated topics, politely decline to answer.

        ##HISTORY
        You are to remember all previous interactions in this conversation to provide better answers.

        ### FORMATTING RULES (STRICT):
        1. **Be Concise:** Keep your answer short and direct (maximum 3-4 sentences, short bullet points or a short paragraph). Avoid long essays.
        2. **No Fluff:** Get straight to the point.
        3. **Follow-up Question:** You MUST end every single response with a short, relevant question to keep the conversation going.

        ##CONTEXT
        Use the following context to answer the user's questions:
        {context}


        """

    model_config = {
        "temperature" : 0.1,
        "max_output_tokens" : 8192
    }

    llm = genai.GenerativeModel(
        model_name= MODEL,
        system_instruction=system_instruction,
        generation_config=model_config
    )

    chatbot = llm.start_chat(history=[])

    return chatbot

chatbot = save_conversation()

def generate_response(prompt):
    max_retries = 1
    attempt_count = 0

    current_persona = personas[select_persona(prompt)]
    user_message = f"""
    considering the following persona guidelines, respond to the user's message.
    {current_persona}

    answer the folowing message from the user, always remembering the previous questions and answers in this conversation history.
    {prompt}
    """

    while True:

        try:

            response = chatbot.send_message(user_message)

            if len(chatbot.history) > 10:
                chatbot.history = summarize_history(chatbot.history)
                chatbot.history = delete_old_messages(chatbot.history)

            print(f"Queries: {len(chatbot.history)}\n {chatbot.history}")

            return response.text.strip()

        except Exception as error:
            attempt_count += 1
            if attempt_count >= max_retries:
                return "Gemini Error: %s" % error

            sleep(50)


@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    response = generate_response(prompt)
    return response

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
