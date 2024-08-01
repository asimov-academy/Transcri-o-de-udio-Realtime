# Chatbot de Transcrição de Áudio

Este projeto é um chatbot de transcrição de áudio que usa Whisper para transcrição e integra com um modelo de linguagem (LLM) para ajudar os usuários com as transcrições de áudio. O chatbot pode processar comandos via hotkeys do teclado.

# Requisitos

- `Python 3.6+`
- `pynput` para interação com o teclado
- `whisper_live` para transcrição de áudio. Para mais instruções sobre como rodar o servidor de transcrição, [clique aqui](https://github.com/collabora/WhisperLive).
- `langchain`, `langchain_groq`, `langchain_ollama` para interação com o modelo de linguagem
- `python-dotenv` para gerenciamento de variáveis de ambiente
- `Ollama` instalado no seu computador (caso queira rodar modelos locais).

# Instalação

1.	Clone o repositório e navegue até o diretório do projeto.
2.	Instale os pacotes Python necessários:

`pip install -r requirements.txt`

3.	Certifique-se de ter o Ollama ou Groq rodando na sua máquina.


# Configuração

1.	Crie um arquivo .env no diretório raiz do projeto com as variáveis de ambiente necessárias.

Executando o Projeto

1.	Atualize o script com o endereço IP e a porta corretos para o TranscriptionClient.
2.	Inicie o script:

`python seu_script.py`


