import openai
import streamlit as st
import os

# Obtém a chave da API da OpenAI do segredo do GitHub
openai.api_key = os.getenv("OPENAI_API_KEY")

# ID do seu agente específico
AGENT_ID = "asst_78f9iKPVOB39CBgxne4hZyZX"

# Título do aplicativo no Streamlit
st.markdown("<h1 style='text-align: center;'>Cruz Data Science</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Soluções Exclusivas em Ciência de Dados Para Cada Cliente</h3>", unsafe_allow_html=True)

# Exibir contatos abaixo do título
st.markdown("**Contatos:**")
st.markdown("📞 (37) 998751870")
st.markdown("📧 migueljosepereiracruz@gmail.com")

# Manter o histórico de chat na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Perguntas pré-definidas
perguntas_pre_definidas = [
    "Quais serviços de ciência de dados você oferece?",
    "Como a Cruz Data Science pode me ajudar a melhorar meus processos?",
    "Você pode me explicar sobre análise preditiva?",
    "O que é automação de dados e como ela funciona?"
]

# Função para interagir com o agente de IA
def conversar_com_agente(mensagem_usuario):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Modelo específico usado no agente
        messages=[
            {"role": "system", "content": "Você é o assistente de Cruz Data Science. Responda somente de acordo com os serviços de ciência de dados oferecidos. Não responda a perguntas fora deste escopo."},
            {"role": "user", "content": mensagem_usuario}
        ]
    )
    return response.choices[0].message["content"]

# Função chamada ao enviar a mensagem
def enviar_mensagem():
    if st.session_state.user_input:
        st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})

        # Chamada para o agente da OpenAI
        resposta = conversar_com_agente(st.session_state.user_input)

        # Adicionar a resposta do agente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta})

        # Limpar a caixa de input
        st.session_state.user_input = ""

# Mostrar as perguntas pré-definidas como botões
st.write("### Perguntas sugeridas:")
for pergunta in perguntas_pre_definidas:
    if st.button(pergunta):
        st.session_state.user_input = pergunta
        enviar_mensagem()

# Mostrar o histórico de conversas acima
for mensagem in st.session_state.messages:
    if mensagem["role"] == "user":
        st.write(f"Você: {mensagem['content']}")
    else:
        st.write(f"Agente: {mensagem['content']}")

# Mover a caixa de texto para o final da página
st.text_input("Digite sua mensagem:", key="user_input", on_change=enviar_mensagem, placeholder="Escreva sua mensagem aqui...")
