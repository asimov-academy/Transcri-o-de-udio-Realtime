from whisper_live.client import TranscriptionClient
import threading
from pynput import keyboard
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


client = TranscriptionClient(
  "192.168.1.5",
  9091,
  lang="pt",
  translate=False,
  use_vad=True,
  model="small",
  save_output_recording=True,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav",  # Only used for microphone input
  verbose=True
)


threading.Thread(target=lambda: client()).start()
# threading.Thread(target=lambda x: client(x), args=("wake_detect.wav",)).start()


template = """
        You are a chatbot helping a human with audio transcriptions.
        You will recieve the text from the audio and should help the user.
        Answer only in Portuguease.

        Chat History: {chat_history}
        Last transcription:{audio}
        Input: {input}
        """

base_prompt = PromptTemplate(
input_variables=["input"], template=template
)

# Você deve ter o Ollama instalado e rodando no seu computador. 
# Troque o modelo se sentir necessidade.
llm = ChatOllama(temperature=0, model="llama3:8b-instruct-q8_0")

# Você também pode usar a API da Groq
# llm = ChatGroq(temperature=0, model="llama3-8b-8192")
memory = ConversationBufferMemory(memory_key="chat_history",
                                input_key='input')
llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)


# =====================
# Definição de Hotkeys
transcript = ""
os.system("clear")

def on_press(key):
    global transcript
    
    # Esta hotkey é usada para parar a transcrição e salvar o texto na variável transcript
    if key == keyboard.Key.alt_l:
        client.client.client_socket.close()
        transcript = "".join(client.client.text)
        os.system("clear")
        print(transcript)
        print("\n\n")  
          

    # Aqui ativamos o modo de conversa com a LLM escolhida.
    if key == keyboard.Key.cmd:

        user_input = input("\nVocê: ")
        response = llm_chain.invoke({"input": user_input,
                                     "audio": transcript})["text"]

        print(f"\n IA: {response}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join() 






