import json
import os
import time
from google import genai
from google.genai import types
import streamlit as st
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do ficheiro .env
load_dotenv()

# Configuração da página no Streamlit
st.set_page_config(
    page_title="Triagem de Suporte - Gemini", page_icon="✉️", layout="centered"
)

st.title("✉️ Sistema Inteligente de Triagem de Suporte")
st.write(
    "Insere abaixo o email recebido do cliente para análise automática da"
    " urgência, categorização e geração de resposta."
)

# Obter a chave da API do ambiente
api_key = os.getenv("GEMINI_API_KEY")

# Caixa de texto para o operador colar o email do cliente
email_texto = st.text_area(
    "Mensagem do Cliente:",
    placeholder=(
        "Ex: Olá, o meu sistema bloqueou após a última atualização e não consigo"
        " emitir faturas urgentemente..."
    ),
    height=150,
)

if st.button("Analisar Email e Gerar Resposta", type="primary"):
    if not email_texto.strip():
        st.warning("Por favor, insere o texto de um email para analisar.")
    elif not api_key:
        st.error(
            "Chave GEMINI_API_KEY não encontrada. Certifica-te de que criaste o"
            " ficheiro .env com a tua chave."
        )
    else:
        with st.spinner("A analisar o email com a inteligência artificial..."):
            try:
                # Inicialização do cliente Gemini
                client = genai.Client(api_key=api_key)

                # Prompt estruturado para forçar saída JSON limpa
                prompt = f"""
                Analisa o seguinte email de suporte de um cliente e devolve estritamente um objeto JSON válido contendo as seguintes chaves:
                - "cliente": Nome do cliente (se identificado, senão "Desconhecido")
                - "categoria": Categoria do problema (ex: Suporte Técnico, Financeiro, Dúvidas Gerais, Comercial)
                - "urgencia": Nível de urgência (Baixa, Média, Alta)
                - "resumo_problema": Breve resumo técnico do problema relatado
                - "resposta_sugerida": Minuta de resposta profissional, empática e orientada à solução para o operador enviar ao cliente.

                Texto do email:
                {email_texto}
                """

                # Lógica com tentativas automáticas em caso de instabilidade (503)
                max_tentativas = 3
                response = None
                
                for tentativa in range(max_tentativas):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                response_mime_type="application/json"
                            ),
                        )
                        break 
                    except Exception as api_err:
                        if tentativa == max_tentativas - 1:
                            raise api_err 
                        time.sleep(2)

                resultado = json.loads(response.text)

                st.success("Análise concluída com sucesso!")

                # Exibição visual limpa e profissional
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Categoria", value=resultado.get("categoria", "N/A"))
                with col2:
                    st.metric(label="Urgência", value=resultado.get("urgencia", "N/A"))

                st.subheader("📋 Resumo do Problema")
                st.write(resultado.get("resumo_problema", ""))

                st.subheader("✍️ Minuta de Resposta Sugerida")
                st.info(resultado.get("resposta_sugerida", ""))

                with st.expander("Ver JSON Completo (Dados Técnicos)"):
                    st.json(resultado)

            except Exception as e:
                st.error(f"Ocorreu um erro ao processar o pedido: {e}")