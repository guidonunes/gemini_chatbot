from flask import Flask, render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


GEMINI_API = os.getenv("GEMINI_API")
MODEL = "gemini-2.5-flash"
genai.configure(api_key=GEMINI_API)


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
