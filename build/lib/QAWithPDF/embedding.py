from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from data_ingestion import load_data
from model_api import load_model


import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="embedding-gecko-001")
        
    
        logging.info("")
        index = VectorStoreIndex.from_documents(
                document,
                llm=model,
                embed_model=GeminiEmbedding,
                chunk_size=800,
                chunk_overlap=20
                )

    
        index.storage_context.persist()
        
        logging.info("")    
        query_engine = index.as_query_engine(llm=model)
        return query_engine
    except Exception as e:
        raise customexception(e,sys)