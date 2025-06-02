import streamlit as st
import os
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 🌍 OpenAI lykill úr Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

@st.cache_resource
def hlaða_leitarkerfi():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("hsi_faiss_index", embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever()

@st.cache_resource
def hlaða_svarskeðju():
    retriever = hlaða_leitarkerfi()
    llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo")
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

qa = hlaða_svarskeðju()

st.set_page_config(page_title="HSÍ Regluagent – nákvæmt", page_icon="🤾")
st.title("📘 Regluagent HSÍ – með venslaleit")
st.markdown("Spurðu út frá reglugerð HSÍ og fáðu nákvæmt svar úr venslaleitarkerfi.")

spurning = st.text_input("💬 Spurning:")

if st.button("Senda") and spurning:
    svar = qa.run(spurning)
    st.markdown("---")
    st.markdown(f"**Svar:**\n\n{svar}")
