import openai
import streamlit as st

# Chave de API da OpenAI
openai.api_key = "sk-Aoagmc8uALVozvcgWohfuvbQJgmtPMF-zAzQy0juY4T3BlbkFJLtFjs2dpGRWQTc-Ag6Ya2u8eEGxvb8KVG0JsvenBcA"

# ID do seu agente específico
AGENT_ID = "asst_78f9iKPVOB39CBgxne4hZyZX"  # ID do agente personalizado na OpenAI

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

# Função para interagir com o agente de IA
def conversar_com_agente(mensagem_usuario):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use o modelo correto, como GPT-4, dependendo do agente que você configurou
        messages=[
            {"role": "system", "content": "Você é o assistente da Cruz Data Science. Responda com base nos serviços personalizados de ciência de dados que a empresa oferece."},
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

# Perguntas sugeridas
st.write("### Perguntas sugeridas:")
perguntas_pre_definidas = [
    "Quais serviços de ciência de dados você oferece?",
    "Como a Cruz Data Science pode me ajudar a melhorar meus processos?",
    "Você pode me explicar sobre análise preditiva?",
    "O que é automação de dados e como ela funciona?"
]

# Exibir as perguntas como botões
for pergunta in perguntas_pre_definidas:
    if st.button(pergunta):
        st.session_state.user_input = pergunta
        enviar_mensagem()

# Exibir o histórico de conversas
for mensagem in st.session_state.messages:
    if mensagem["role"] == "user":
        st.write(f"Você: {mensagem['content']}")
    else:
        st.write(f"Agente: {mensagem['content']}")

# Mover a caixa de texto para o final da página
st.text_input("Digite sua mensagem:", key="user_input", on_change=enviar_mensagem, placeholder="Escreva sua mensagem aqui...")
