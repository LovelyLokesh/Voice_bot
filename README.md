**Lokesh Voice bot**

**Overview**

Lokesh Voice Bot is an AI-powered chatbot that allows users to ask questions via speech and receive AI-generated responses in both text and speech. This system leverages Retrieval-Augmented Generation (RAG) to process and retrieve information from PDF documents and provide context-aware responses.

**Features**

* Converts speech input into text using speech recognition.

* Utilizes a Retrieval-Augmented Generation (RAG) pipeline to generate AI-driven answers.

* Converts AI-generated responses into speech output.

* Uses Gradio for an interactive web-based interface.

* Processes PDFs to extract relevant content for contextual responses.

* Easy to install and configure.

**Installation**

**Prerequisites**

Ensure you have the following installed:

* Python 3.8+

* pip

**Steps**

Clone the repository:

* git clone https://github.com/your-repo/chat-with-lokesh.git
cd chat-with-lokesh

**Install dependencies:**

* pip install -r requirements.txt

* Ensure your config.json file is properly set up with necessary parameters.

* Place PDF files inside the ./pdfs directory.

**Configuration**

* Create a config.json file in the root directory with the following format:

{
    "pdf_directory": "./pdfs",
    "api_key": "your_mistral_api_key"
}

**Note:** Replace your_mistral_api_key with your actual API key.

**Usage**

To launch the chatbot, run:

* python main.py

This will start a Gradio web interface where you can interact with the AI.

**File Structure**

chat-with-lokesh/
│── pdfs/                 	# Folder for storing PDF documents
│── config.json           	# Configuration file
│── requirements.txt      	# List of dependencies
│── main.py               	# Main application script
│── rag_pdf_processing.py 	# PDF processing and RAG model
│── speech_processing.py  	# Speech-to-text and text-to-speech functions
│── README.md             	# This documentation file

How It Works

**Speech Processing:** Converts spoken input into text using speech_recognition.

**RAG Pipeline:** Extracts content from PDFs, processes it with embeddings, and retrieves relevant information.

**AI Response:** Uses a language model to generate responses based on retrieved data.

**Speech Output:** Converts AI-generated text responses back into speech using gTTS.

**Gradio UI:** Provides an interactive interface for user interaction.

**Contributing**

Contributions are welcome! If you'd like to improve the chatbot, please fork the repository, make your changes, and submit a pull request.

**License**

This project is open-source and licensed under the MIT License.

**Contact**

For any inquiries or suggestions, feel free to reach out at lokeshb9025@gmail.com .

