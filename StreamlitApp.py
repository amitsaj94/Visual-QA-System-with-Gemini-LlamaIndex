import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config(page_title="QA System with Gemini", layout="wide")
    st.title("📚 Visual QA System with Gemini + LlamaIndex")

    # Tabs in the UI
    tab1, tab2 = st.tabs(["📄 Upload Document", "💬 Ask Questions"])

    # Session state for persistent data
    if "query_engine" not in st.session_state:
        st.session_state.query_engine = None

    with tab1:
        st.subheader("Upload Your PDF or TXT File")
        documents = load_data()  # file upload
        if documents:
            st.success("Document uploaded and processed.")
            model = load_model()
            query_engine = download_gemini_embedding(model, documents)
            st.session_state.query_engine = query_engine
            st.info("Now switch to the 'Ask Questions' tab.")

    with tab2:
        st.subheader("Ask Questions About Your Document")
        if st.session_state.query_engine is None:
            st.warning("Please upload and process a document first in the 'Upload Document' tab.")
        else:
            question = st.text_input("Type your question here:")
            if question:
                with st.spinner("Thinking..."):
                    response = st.session_state.query_engine.query(question)
                    st.markdown(f"**Answer:** {response.response}")

if __name__ == "__main__":
    main()

