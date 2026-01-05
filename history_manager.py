import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API = os.getenv("GEMINI_API")
MODEL = "gemini-2.5-flash"
genai.configure(api_key=GEMINI_API)

def delete_old_messages(history):
    return history[2:]



def summarize_history(history):
    """
    Summarizes the conversation history to retain important context while reducing length.
    This method is called when the conversation history exceeds a length of 10 queries.
    """

    full_history_text = " ".join([
        snippet.text if hasattr(snippet, 'text') else snippet
        for message in history for snippet in message['snippets']
    ])

    prompt_summarize = f"""
    Summarize the following conversation history between a Financial Advisor AI and a user.
    Focus on retaining key financial topics, user concerns, and any important details that would help maintain
    {full_history_text}
    """

    llm = genai.GenerativeModel(
        model_name= MODEL,
        system_instruction=prompt_summarize,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 512
        }
    )

    response = llm.generate_content(prompt_summarize)
    summary = response.text.strip()

    history_summary = [{'role': 'model', 'snippets': [summary]}]

    return history_summary
