import os
import pypdf
import warnings
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import StrOutputParser
from langchain_mistralai import ChatMistralAI
import json
os.environ['USER_AGENT'] = 'myagent'
warnings.filterwarnings("ignore")

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

MISTRAL_API_KEY = config["MISTRAL_API_KEY"]
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
CHROMA_DB_DIR = "chroma_db"

# Load and Process PDFs
def load_and_process_pdfs(pdf_directory):
    texts = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(pdf_directory, filename)
            reader = PyPDFLoader(filepath)
            text = "\n".join([page.page_content for page in reader.load()])
            texts.append(text)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    documents = [Document(page_content=text, metadata={"source": f"Document_{i}"}) for i, text in enumerate(texts)]
    pdf_chunks = splitter.split_documents(documents)
    return pdf_chunks

# Create RAG pipeline
def create_rag_pipeline(pdf_chunks):
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME, model_kwargs={"device": "cuda"})
    vectordb = Chroma.from_documents(documents=pdf_chunks, embedding=embeddings, persist_directory=CHROMA_DB_DIR)
    retriever = vectordb.as_retriever()

    prompt = PromptTemplate.from_template(
        """
            You are Lokesh, an AI Engineer with expertise in AI Agents, RAG, LLMs, Data Science, Time Series, ML, and AI. 
            You are attending an interview for an AI Agent role. Answer concisely, professionally, and respectfully.
        {context}

        Question: {question}
        Answer:
        """
    )
    llm = ChatMistralAI(mistral_api_key=MISTRAL_API_KEY)

    return ( 
        {"context": retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)), "question": RunnablePassthrough()} 
        | prompt 
        | llm 
        | StrOutputParser() 
    )

# Main function to process PDFs and return RAG pipeline
def initialize_rag_pipeline(pdf_directory):
    pdf_chunks = load_and_process_pdfs(pdf_directory)
    return create_rag_pipeline(pdf_chunks)
