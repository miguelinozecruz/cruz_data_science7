import openai
import streamlit as st
import os

# Pegue a chave da API da OpenAI a partir de variáveis de ambiente ou defina diretamente
openai.api_key = os.getenv("OPENAI_API_KEY")  # Defina sua chave de API aqui se não usar variável de ambiente

# Função para interagir com o agente de IA usando o GPT-3.5-turbo
def conversar_com_agente(mensagem_usuario):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usando o modelo GPT-3.5-turbo
            messages=[
                {"role": "system", "content": "Você é o assistente da Cruz Data Science. Responda somente sobre os serviços de ciência de dados."},
                {"role": "user", "content": mensagem_usuario}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro ao se comunicar com o agente de IA: {str(e)}"

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

# Perguntas pré-definidas
st.write("### Perguntas sugeridas:")
perguntas_pre_definidas = [
    "Quais serviços de ciência de dados você oferece?",
    "Como a Cruz Data Science pode me ajudar a melhorar meus processos?",
    "Você pode me explicar sobre análise preditiva?",
    "O que é automação de dados e como ela funciona?"
]

# Exibir as perguntas pré-definidas como botões
for pergunta in perguntas_pre_definidas:
    if st.button(pergunta):
        st.session_state.user_input = pergunta
        enviar_mensagem()

# Exibir o histórico de conversas acima
for mensagem in st.session_state.messages:
    if mensagem["role"] == "user":
        st.write(f"Você: {mensagem['content']}")
    else:
        st.write(f"Agente: {mensagem['content']}")

# Mover a caixa de texto para o final da página
st.text_input("Digite sua mensagem:", key="user_input", on_change=enviar_mensagem, placeholder="Escreva sua mensagem aqui...")
