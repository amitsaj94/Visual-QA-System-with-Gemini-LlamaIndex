from llama_index.core import SimpleDirectoryReader
import sys
import os
import fitz  # PyMuPDF

# Fix the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from exception import customexception
from logger import logging

# This module handles the ingestion of PDF and TXT files for the QA system.


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


