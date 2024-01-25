import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

def getPDFText(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def getTextChunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="/n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def getVectorStore(chunks):
    st.write("he;lo")




def main():
    load_dotenv()
    st.set_page_config(page_title='chat with pdfs',page_icon='🧑‍💻')
    st.header('chat with PDFs')
    st.text_input("Ask a Question about your docs")

    with st.sidebar:
        st.subheader("your documents")
        pdf_docs = st.file_uploader("upload pdf here and click on process",accept_multiple_files=True)
        if st.button("Process"):
            with  st.spinner("processing.."):
            # get the pdf text 
                raw_text = getPDFText(pdf_docs)
            
            # get the text chunks
                text_chunks = getTextChunks(raw_text)
                st.write(text_chunks)

            # create a vector store
                vectorStore = getVectorStore(text_chunks)








if __name__ == '__main__':
    main()
