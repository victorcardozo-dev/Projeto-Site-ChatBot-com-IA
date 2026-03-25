# Projeto de ChatBot com IA
# a cada mensagem que o usuário enviar
    # mostra a mensagem que o usuário enviou no chat
    # pegar a pergunta e enviar para a IA responder
    # exibir a reposta da IA da tela

import streamlit as st
from openai import OpenAI

st.write('# ChatBot com IA') # Seguem o formato markdown
texto_usuario = st.chat_input('Digite sua mensagem: ')


# cria a lista de mensagens se nao tiver cookies no navegador do usuário
if not 'lista_mensagem' in st.session_state:
    st.session_state['lista_mensagem'] = []


# escreve a lista com as mensagens do usuário e respostas da IA no chat
for mensagem in st.session_state['lista_mensagem']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)

modelo_ia = OpenAI(api_key='chave API') # precisa criar uma chave API e colocar aqui

if texto_usuario:
    # Mensagem do usuário
    st.chat_message('user').write(texto_usuario)
    mensagem_usuario = {'role': 'user', 'content': texto_usuario } # role é quem está respondendo (user ou assistant) e content é o conteúdo da mensagem

    st.session_state['lista_mensagem'].append(mensagem_usuario)  # Adiciona a mensagem do usuário na lista de mensagens
   
    # Resposta da IA
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state['lista_mensagem'],
        model= 'gpt-4o'
    )
    print(resposta_ia) # Você vai conseguir vizualiar no terminal a resposta completa da IA (é uma lista com várias informaçôes) e você precisa selecionar somente a parte com o conteúdo da resposta
    texto_resposta_ia = resposta_ia.choices[0].message.content # Esse é caminho para pegar o conteúdo da resposta
    st.chat_message('assistant').write(texto_resposta_ia)
    mensagem_ia = {'role': 'assistant', 'content': texto_resposta_ia}
    st.session_state['lista_mensagem'].append(texto_resposta_ia)  # Adiciona a resposta da IA na lista de mensagens
