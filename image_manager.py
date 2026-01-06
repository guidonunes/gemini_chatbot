import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()


GEMINI_API = os.getenv("GEMINI_API")
MODEL = "gemini-2.5-flash"
genai.configure(api_key=GEMINI_API)

def generate_image(image_path):
    temp_img = genai.upload_file(
        path=image_path,
        display_name="uploaded_image"
    )
    print(f"Image uploaded: {temp_img.uri}")

    return temp_img
