import fitz
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

doc = fitz.open("Reglugerd-HSI-um-Handknattleiksmot-vor-2025.pdf")
text = "\n".join([page.get_text() for page in doc])
splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=100)
texts = splitter.split_text(text)

embeddings = OpenAIEmbeddings()
db = FAISS.from_texts(texts, embeddings)
db.save_local("hsi_faiss_index")
