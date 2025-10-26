import streamlit as st
from main import barra_navegacao
from time import sleep
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer

st.set_page_config(page_title="Davi", layout="wide", page_icon="🤖")
barra_navegacao()

st.title("Aqui será implementado o Davi 🤖")
st.subheader("Vamos Comecar!")