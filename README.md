# 🪙 SatoshiAI - Intelligent Financial Advisor

> **Your Partner in Wealth and Well-being.** An emotionally intelligent financial chatbot powered by Google's Gemini LLM.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![License](https://img.shields.io/badge/license-MIT-grey)

## 📖 Overview

**SatoshiAI** is a next-generation financial assistant designed to bridge the gap between technical data and human emotion. Unlike standard chatbots, SatoshiAI utilizes a **Dynamic Persona Engine** that analyzes user sentiment in real-time to adjust its interaction style—shifting from a high-energy "Financial Cheerleader" to a calm "Market Analyst" or an "Empathetic Guide" depending on the user's anxiety levels.

It also features **Computer Vision** integration, allowing users to upload images of financial charts for instant technical analysis.

---

## 📸 Demo & Screenshots

### 1. Dynamic Personas
SatoshiAI adapts its tone based on the context:

| **Positive (Cheerleader)** 🚀 | **Neutral (Analyst)** 📊 | **Negative (Empathetic)** 🛡️ |
|:---:|:---:|:---:|
| *Celebrating a savings milestone* | *Explaining ETF allocation* | *Handling market crash anxiety* |


### 2. Technical Analysis (Computer Vision)
Upload a chart, and SatoshiAI identifies trends, support/resistance levels, and indicators.


---

## ✨ Key Features

* 🧠 **Emotional Intelligence Engine:** Automatically detects user sentiment (Positive, Neutral, Negative) and switches system prompts dynamically.
* 👁️ **Multimodal Capabilities:** Uses Google Gemini Vision to "read" and analyze uploaded financial images and charts.
* 📉 **Technical Analysis:** Recognizes patterns like Head & Shoulders, Support/Resistance, and Moving Averages.
* 🔒 **Secure Sessions:** Custom Flask session management with server-side signing (`app.secret_key`) for data persistence.
* 💬 **Smart Conversation Flow:** Enforces brevity and "follow-up" logic to keep the user engaged without overwhelming them with text.

---

## 🛠️ Tech Stack

* **Core:** Python 3.10+
* **Backend Framework:** Flask
* **AI Model:** Google Gemini 2.5 Flash
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Environment Management:** `python-dotenv`

---

## 🚀 Installation & Setup

Follow these steps to run SatoshiAI locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/satoshi-ai.git](https://github.com/yourusername/satoshi-ai.git)
cd satoshi-ai
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
   
Create a file named .env in the root directory and add your credentials:

```
GEMINI_API=your_google_gemini_api_key_here
FLASK_SECRET_KEY=your_generated_secret_key_here
(Tip: You can generate a secret key by running python -c 'import secrets; print(secrets.token_hex(24))' in your terminal)
```

### 5. Run the Application
```bash
python app.py
Access the bot at http://127.0.0.1:5000/.
```

## 📂 Project Structure
```
satoshi-ai/
├── static/
│   ├── css/          # Stylesheets
│   ├── img/          # Icons and Logos
│   └── js/           # Frontend logic (DOM manipulation)
├── templates/
│   └── index.html    # Main Chat Interface
├── data/
│   └── satoshi_ai.txt # The "Brain" (Context & Policies)
├── app.py            # Main Flask Application
├── bot_persona.py    # Persona Definitions (Positive/Neutral/Negative)
├── .env              # API Keys (Not committed)
└── requirements.txt  # Dependencies
```
