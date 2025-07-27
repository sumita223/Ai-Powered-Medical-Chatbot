# 🧠 AI-Powered Medical Chatbot

An intelligent **multimodal healthcare assistant** capable of understanding **voice, text, and medical images**.  
Built with state-of-the-art vision and language models, this chatbot simulates medical consultations — enhancing **accessibility** and **patient engagement**.

---

## 🔍 Key Features

- 🗣️ **Voice Input** via OpenAI Whisper  
- 📷 **Medical Image Analysis** using Meta LLaMA 3 Vision 90B  
- 🧾 **Textual Understanding** using GPT-3.5-Turbo / GPT-4-Turbo  
- 🎙️ **Voice Output** with gTTS or ElevenLabs TTS  
- 🧑‍⚕️ **Simulated Medical Consultations** (AI as virtual doctor)  
- 🧠 **Multimodal Fusion** of voice, image, and text inputs  
- 🌐 **Gradio Web Interface** for interactive user experience  

---

## ⚙️ Tech Stack

| Component              | Technology                         |
|------------------------|-------------------------------------|
| 🧠 Multimodal Reasoning | Meta LLaMA 3 Vision 90B             |
| 💬 Language Model       | OpenAI GPT-3.5 / GPT-4 Turbo        |
| 🎤 Speech Recognition   | OpenAI Whisper                     |
| 🔊 Text-to-Speech       | gTTS, ElevenLabs                   |
| 🖥️ Frontend UI          | Gradio                             |
| 🚀 Deployment           | Render|

---

## 🚀 How It Works

- User speaks a query and uploads a medical image (e.g., chest X-ray)  
- Whisper transcribes the spoken input into text  
- LLaMA 3 Vision processes the uploaded medical image  
- GPT-3.5 / GPT-4 analyzes the combined context (text + image)  
- TTS engine (gTTS or ElevenLabs) generates a spoken response

## Getting Started
## Step 1:Clone the Repository
bash
git clone https://github.com/sumita223/Ai-Powered-Medical-Chatbot.git

## Step 2: Create and Activate a Virtual Environment
bash
python -m venv venv
For Linux/Mac:
bash
source venv/bin/activate
For Windows:
bash
venv\Scripts\activate
## Step 3: Install Dependencies
bash
pip install -r requirements.txt
## Step 4: Set Up API Keys
Create a .env file in the root directory and add the following:
OPENAI_API_KEY=your-openai-key
ELEVENLABS_API_KEY=your-elevenlabs-key
## Step 5: Run the App
bash
python app.py
Gradio UI will automatically open in your browser.

##  Example Use Case
## Prompt
Voice + Image Input:
 "Hey doctor, can you tell me what's wrong with my face?"
(User uploads a facial image showing a skin condition)

## Response
 "Based on the uploaded image, it appears to be a mild skin irritation consistent with dermatitis. For a precise diagnosis, please consult a dermatologist."

## 🔮 Future Enhancements
- Integration with Electronic Health Records (EHR)
- Symptom tracking dashboard for users
- Realistic doctor avatars using Sora or DeepMotion


