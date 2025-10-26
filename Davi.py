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

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2", device="cpu")

GROQ_API_KEY = ""
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

@st.cache_resource(show_spinner="DAVI está acordando...")
def carregar_index():
    documentos = SimpleDirectoryReader('davi').load_data()
    index = VectorStoreIndex.from_documents(documentos, embed_model=embed_model)
    return index

def response_generator(pergunta):
    resposta = chat_engine.chat(pergunta).response
    return resposta
    
if "chat_store" not in st.session_state:
    st.session_state.chat_store = SimpleChatStore()

if "chat_memory" not in st.session_state:
    st.session_state.chat_memory = ChatMemoryBuffer.from_defaults(
        chat_store=st.session_state.chat_store,
        token_limit=3000
    )

index = carregar_index()
chat_engine = index.as_chat_engine(
    llm=llm,
    chat_mode="condense_plus_context",
    memory=st.session_state.chat_memory
)

st.title("🤖 DAVI")
st.markdown("**D**ata**V**ision **A**rtificial **I**ntelligence - Seu assistente virtual inteligente treinado com conhecimento completo sobre a DataVision. Tire dúvidas sobre produtos, planos, políticas, equipe e muito mais!")

with st.expander("💡 Sugestões de Perguntas"):
    st.markdown("""
        - O que é a DataVision e quando foi fundada?
        - Quais produtos vocês oferecem?
        - Quanto custa o plano Empresarial?
        - A DataVision atende empresas fora do Brasil?
        - Como funciona a política de cancelamento?
        - A empresa cumpre a LGPD?
        - Quem são os fundadores da DataVision?
        - Quais integrações estão disponíveis?
        - Existe período de teste gratuito?
        - Como entro em contato com o suporte técnico?
    """)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

try:
    if pergunta := st.chat_input("Digite sua pergunta:"):
        st.session_state.mensagens.append({"role": "user", "content": pergunta})
        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            resposta_completa = response_generator(pergunta)
            
            palavras = resposta_completa.split()
            texto_atual = ""
            for palavra in palavras:
                texto_atual += palavra + " "
                placeholder.empty()
                placeholder.markdown(texto_atual)
                sleep(0.05)
            
        st.session_state.mensagens.append({"role": "assistant", "content": resposta_completa})
        
        st.rerun()
except Exception as e:
    st.error("Desculpe, houve um erro ao gerar a resposta. Tente novamente mais tarde ou contate o suporte da DataVision.")
    st.error(e)