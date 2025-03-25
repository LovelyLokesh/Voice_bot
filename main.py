import gradio as gr
import json
import os

# Install required packages
os.system("pip install -r requirements.txt")

from rag_pdf_processing import initialize_rag_pipeline
from speech_processing import speech_to_text, text_to_speech

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

PDF_DIRECTORY = "./pdfs"
rag_pipeline = initialize_rag_pipeline(PDF_DIRECTORY)

def process_audio(audio):
    """Process user audio input and return AI response in text and speech."""
    if not audio:
        return "No audio provided.", None
    
    text_query = speech_to_text(audio)
    if "Sorry" in text_query or "Error" in text_query:
        return text_query, None

    response_text = rag_pipeline.invoke(text_query)
    response_audio = text_to_speech(response_text)
    
    return response_text, response_audio

# Gradio Interface (Text + Audio Output)
iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(type="filepath", label="Ask your question"),
    outputs=[
        gr.Textbox(label="Lokesh Text Response"),
        gr.Audio(label="Lokesh Response")
    ],
    title="Chat With Lokesh",
    description="Ask Your Questions to Lokesh"
)

# Launch the UI
iface.launch()
