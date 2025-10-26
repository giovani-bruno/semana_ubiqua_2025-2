import streamlit as st
from main import barra_navegacao
from utils import tecnologias, adicionar_tecnologia, botao_voltar

st.set_page_config(layout='wide', page_title="Stark")
barra_navegacao()
botao_voltar()

st.title("Stark")

st.write("O Stark é uma inteligência artificial personalizada feita para responder perguntas sobre mim no meu portfólio.")
st.write("Para criar o Stark, utilizei uma combinação de tecnologias modernas de IA que trabalham em conjunto para proporcionar uma experiência conversacional personalizada.")

st.write('''No coração do sistema está o [LlamaIndex](https://docs.llamaindex.ai/en/stable/), que funciona como o "cérebro" do Stark. 
         Ele é responsável por organizar todas as informações sobre mim em uma estrutura pesquisável. O LlamaIndex recebe um documento markdown com 
         informações sobre mim, cria um índice vetorial dessas informações e permite buscar conteúdo relevante quando alguém faz uma pergunta.''')

st.write('''A técnica principal que faz o Stark funcionar é o RAG (Retrieval Augmented Generation). Quando você faz uma pergunta, o sistema 
         primeiro recupera informações relevantes sobre mim do índice. Essas informações são então usadas como contexto para o modelo de linguagem, 
         que gera uma resposta baseada nesse contexto específico. Esta abordagem permite respostas precisas sobre mim sem as "alucinações" que modelos 
         de linguagem geralmente apresentam quando não têm acesso a informações específicas.''')

st.write("""Para o processamento de linguagem natural, utilizo o [Groq](https://groq.com/) como provedor do modelo de linguagem. 
         O Stark roda com o modelo Llama 3.3 70B Versatile, um dos mais avançados disponíveis atualmente. Este modelo processa as 
         perguntas e gera respostas naturais, conectado via API para trabalhar com o contexto fornecido pelo RAG.""")
         
st.write("""Finalmente, o [HuggingFace Embeddings](https://huggingface.co/) é responsável por transformar texto em representações matemáticas (vetores). 
         Utilizando o modelo sentence-transformers/all-MiniLM-L6-v2, o sistema converte tanto as perguntas quanto o conteúdo sobre mim em vetores. Isso 
         permite comparar semanticamente a pergunta com as informações disponíveis e ajuda a encontrar as informações mais relevantes mesmo quando as palavras exatas não coincidem nas buscas.""")

st.write("Juntas, essas tecnologias criam uma experiência de IA interativa e personalizada, capaz de fornecer respostas precisas e contextuais sobre mim, com base nas informações armazenadas e organizadas no sistema.")

st.write("Eu tive essa ideia de botar uma IA no meu portfólio há bastante tempo, e agora, finalmente consegui implementá-lo.")

st.write("O nome Stark é uma homenagem ao meu primeiro animal de estimação.")

st.image("imagens/stark_gato.jpg", width=700)

st.divider()

st.subheader("Tecnologias Utilizadas")

col1, col2 = st.columns(2)
adicionar_tecnologia(tecnologias['Python'], "Linguagem de programação principal utilizada.", 
                     200, col1)

adicionar_tecnologia(tecnologias['Groq'], "Serviço de API que oferece modelos LLM como o Llama 3.3 70B Versatile usado para criar o Stark.", 
                     150, col2)

adicionar_tecnologia(tecnologias['Llama Index'], """Framework que gerencia todo o processo de indexação do documento markdown sobre mim e a consulta 
                     dessas informações quando perguntas são feitas. Ele funciona como a ponte entre minhas informações e o modelo de linguagem da Groq.""",
                     200, col1)

adicionar_tecnologia(tecnologias['Hugging Face'], """Responsável por fornecer o modelo de embeddings que transforma textos em vetores matemáticos, permitindo 
                     que o sistema encontre informações relevantes sobre mim mesmo quando as perguntas não contêm as palavras exatas no documento original.""",
                     250, col2)

st.divider()

st.write("""#### Curioso para saber mais sobre mim? O Stark está disponível na barra lateral à esquerda, pronto para responder suas perguntas! \
         Basta clicar e começar uma conversa para descobrir mais sobre meus projetos, habilidades e experiências de forma interativa e personalizada.""")
