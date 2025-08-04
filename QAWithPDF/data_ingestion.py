from llama_index.core import SimpleDirectoryReader
import sys
import os
import fitz  # PyMuPDF

# Fix the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exception import customexception
from logger import logging

'''def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)
'''
'''
def extract_pdf_text(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        raise customexception(e, sys)



def load_data(uploaded_file):
    try:
        logging.info("data loading started...")

        # Read the uploaded file contents
        content = uploaded_file.read().decode("utf-8")  # or "latin-1" if encoding fails
        doc = Document(text=content, metadata={"filename": uploaded_file.name})

        logging.info("data loading completed...")
        return [doc]
    except Exception as e:
        logging.error("Exception in loading data")
        raise customexception(e, sys)
'''



import streamlit as st

def save_uploaded_file(uploaded_file, save_dir="uploaded_docs"):
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def load_data_from_file(file_path):
    try:
        logging.info(f"Loading file: {file_path}")
        if file_path.endswith(".pdf") or file_path.endswith(".txt"):
            reader = SimpleDirectoryReader(input_files=[file_path])
            return reader.load_data()
        else:
            raise ValueError("Only PDF and TXT files are supported.")
    except Exception as e:
        raise customexception(e, sys)

def load_data():
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        documents = load_data_from_file(file_path)
        st.success("File uploaded and processed successfully!")
        return documents
    return None


