from flask import Flask, render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
from time import sleep
from helper import load_knowledge_base, save
from bot_persona import personas, select_persona

load_dotenv()


GEMINI_API = os.getenv("GEMINI_API")
MODEL = "gemini-2.5-flash"
genai.configure(api_key=GEMINI_API)


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

context = load_knowledge_base("data/satoshi_ai.txt")



def generate_response(prompt):
    max_retries = 1
    attempt_count = 0

    current_persona = personas[select_persona(prompt)]

    while True:

        try:

            # I updated this prompt to match your Financial Advisor context
            system_instruction = f"""
            {current_persona}

            ##PERSONA
            You are a Financial Advisor chatbot.
            You should only answer questions related to finance, budgeting, and investment markets.
            If the user asks about unrelated topics, politely decline to answer.

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

            response = llm.generate_content(prompt)
            return response.text

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
