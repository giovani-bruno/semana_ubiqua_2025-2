import streamlit as st
from main import barra_navegacao


st.set_page_config(
    page_title="DataVision - Soluções em Dados e IA",
    page_icon="📊",
    layout='wide'
)
barra_navegacao()

st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #3B82F6;
        margin-top: 0;
    }
    .product-card {
        background-color: #F0F9FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 10px 0;
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
    }
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚀 DataVision</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Democratizando o acesso à inteligência de dados</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    ## Sobre a DataVision
    
    Fundada em **2021** em Recife-PE, a DataVision é uma startup especializada em 
    soluções de análise de dados, automação e inteligência artificial.
    
    Nossa missão é **democratizar o acesso à inteligência de dados** para negócios 
    de todos os portes, tornando a análise preditiva acessível e compreensível.
    
    ### 🎯 Nossa Visão
    Ser referência em soluções de IA aplicada na América Latina até 2027, 
    impactando positivamente mais de 1000 empresas.
    
    ### 💡 Nossos Valores
    - Inovação com propósito
    - Transparência e ética em IA
    - Foco no cliente
    - Aprendizado contínuo
    - Impacto social positivo
    """)

with col2:
    st.markdown("### 📊 DataVision em Números")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">120+</div>
            <div class="stat-label">Clientes Ativos</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">98%</div>
            <div class="stat-label">Satisfação (NPS)</div>
        </div>
        """, unsafe_allow_html=True)
    
    c3, c4 = st.columns(2)
    with c3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Disponibilidade</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">15</div>
            <div class="stat-label">Especialistas</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.markdown("## 🛍️ Nossos Produtos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="product-card" style="background-color: #262730;">
        <h3>🟢 DataVision Insights</h3>
        <p><strong>Dashboards e BI Inteligente</strong></p>
        <ul>
            <li>Dashboards personalizados</li>
            <li>Relatórios automáticos</li>
            <li>Alertas inteligentes</li>
            <li>50+ tipos de visualizações</li>
        </ul>
        <p><em>Ideal para: Gestores e equipes operacionais</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="product-card" style="background-color: #262730;">
        <h3>🟡 DataVision Predict</h3>
        <p><strong>Machine Learning Preditivo</strong></p>
        <ul>
            <li>Previsão de demanda</li>
            <li>Detecção de churn</li>
            <li>Análise de sentimento</li>
            <li>Recomendação de produtos</li>
        </ul>
        <p><em>Ideal para: E-commerce, SaaS, Varejo</em></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="product-card" style="background-color: #262730;">
        <h3>🔵 DataVision Chat</h3>
        <p><strong>Assistente Conversacional IA</strong></p>
        <ul>
            <li>Respostas automáticas 24/7</li>
            <li>Integração com documentos</li>
            <li>Suporte multilíngue</li>
            <li>Analytics de atendimento</li>
        </ul>
        <p><em>Ideal para: Suporte, RH, Vendas</em></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("## 💰 Planos e Preços")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **📦 Essencial**
    
    **R$ 497/mês**
    
    ✅ 1 produto à escolha  
    ✅ Até 5 usuários  
    ✅ 10.000 registros/mês  
    ✅ Suporte por e-mail  
    ✅ 14 dias grátis  
    
    *Ideal para startups e pequenas empresas*
    """)

with col2:
    st.success("""
    **🚀 Empresarial**
    
    **R$ 1.497/mês**
    
    ✅ 2 produtos inclusos  
    ✅ Até 20 usuários  
    ✅ 100.000 registros/mês  
    ✅ Suporte prioritário (chat)  
    ✅ Onboarding incluso  
    
    *Ideal para empresas em crescimento*
    """)

with col3:
    st.warning("""
    **⭐ Enterprise**
    
    **Sob consulta**
    
    ✅ Todos os produtos  
    ✅ Usuários ilimitados  
    ✅ Registros ilimitados  
    ✅ Gerente de conta dedicado  
    ✅ SLA premium 99,9%  
    
    *Ideal para grandes corporações*
    """)

st.divider()

st.markdown("## 👥 Nossa Equipe")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Lucas Menezes
    **CEO e Co-fundador**
    
    Engenheiro de computação (UFPE) com MBA pela FGV. 
    8 anos de experiência em Microsoft e Accenture.
    
    Lidera a visão estratégica da empresa.
    """)

with col2:
    st.markdown("""
    ### Ana Paula Ferreira
    **CTO e Co-fundadora**
    
    Cientista da computação com mestrado em IA (UFPE). 
    Experiência em fintechs e startups de grande porte.
    
    Responsável pela arquitetura técnica.
    """)

with col3:
    st.markdown("""
    ### Giovani Costa
    **Head de Data Science**
    
    Doutor em Machine Learning (UFPE). 
    Especialista em IA ética e explicável.
    
    Lidera desenvolvimento de modelos preditivos.
    """)

st.divider()

st.markdown("## 🌟 Por que escolher a DataVision?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ Diferenciais Técnicos
    - **Interface 100% em português e espanhol**
    - **APIs abertas para integração**
    - **Conformidade total com LGPD**
    - **Servidores no Brasil (AWS São Paulo)**
    - **Certificação ISO 27001**
    """)

with col2:
    st.markdown("""
    ### ✅ Diferenciais de Negócio
    - **Preços acessíveis e planos flexíveis**
    - **Suporte humanizado e próximo**
    - **Treinamento incluso em todos os planos**
    - **14 dias de teste grátis**
    - **Cases de sucesso comprovados**
    """)

st.divider()

st.markdown("## 📞 Entre em Contato")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    ### 💬 Fale Conosco
    
    **📧 E-mail Geral:** contato@datavision.tech  
    **🛠️ Suporte Técnico:** suporte@datavision.tech  
    **💼 Comercial:** comercial@datavision.tech  
    
    **📱 WhatsApp Enterprise:** +55 81 9 8765-4321  
    
    **📍 Endereço:**  
    Porto Digital - Recife, PE  
    Rua da Guia, 142 - Recife Antigo
    
    **🕐 Horário de Atendimento:**  
    Segunda a Sexta: 9h às 18h (horário de Brasília)
    """)

with col2:
    st.markdown("""
    ### 🔗 Siga-nos nas Redes
    """)
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown("🔗 [LinkedIn](https://linkedin.com/company/datavision-tech)")
    with c2:
        st.markdown("📘 [Instagram](https://instagram.com/datavision.tech)")
    with c3:
        st.markdown("🐦 [Twitter](https://twitter.com/datavision_tech)")
    with c4:
        st.markdown("📺 [YouTube](https://youtube.com/@datavision)")
    
    st.markdown("---")
    
    with st.form("contact_form"):
        st.markdown("**Envie uma mensagem:**")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        mensagem = st.text_area("Mensagem")
        
        submitted = st.form_submit_button("📨 Enviar Mensagem")
        
        if submitted:
            if nome and email and mensagem:
                st.success("✅ Mensagem enviada com sucesso! Retornaremos em breve.")
            else:
                st.error("❌ Por favor, preencha todos os campos.")

st.divider()

st.markdown("""
<div style='text-align: center; color: #64748B; padding: 20px;'>
    <p>© 2024 DataVision - Todos os direitos reservados</p>
    <p>CNPJ: 12.345.678/0001-90 | Recife - PE, Brasil</p>
    <p><small>Política de Privacidade | Termos de Uso | LGPD</small></p>
</div>
""", unsafe_allow_html=True)