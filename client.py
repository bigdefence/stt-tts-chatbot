import streamlit as st
import requests
import io
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import threading
import time
from gtts import gTTS
import os
import pygame


st.set_page_config(page_title="음성 인식 기반 한국어 챗봇", layout="wide")


st.sidebar.title("챗봇 정보")
st.sidebar.info(
    "이 챗봇은 음성 인식과 Llama3 모델을 기반으로 한 한국어 대화 시스템입니다. "
    "음성으로 질문하거나 텍스트로 입력할 수 있습니다."
)

st.sidebar.title("사용 방법")
st.sidebar.markdown(
    """
    1. '음성 녹음' 버튼을 클릭하여 5초 동안 음성을 녹음하세요.
    2. 녹음이 완료되면 자동으로 서버로 전송됩니다.
    3. 또는 채팅 입력창에 텍스트로 질문을 입력하세요.
    4. AI가 응답을 생성하고 음성으로 읽어줍니다.
    5. 대화 기록은 자동으로 저장됩니다.
    """
)

API_ENDPOINT = "API 서버 주소"


def record_audio(duration=5, sample_rate=16000):
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    return audio_data, sample_rate


def send_audio_get_response(audio_data, sample_rate):

    audio_buffer = io.BytesIO()
    wav.write(audio_buffer, sample_rate, audio_data)
    audio_buffer.seek(0)
    

    files = {'file': ('audio.wav', audio_buffer, 'audio/wav')}
    response = requests.post(f"{API_ENDPOINT}/speech_to_chat", files=files)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"transcription": "Error: Unable to process audio.", "response": "Error: Unable to get response from the server."}


def send_text_get_response(text):
    response = requests.post(f"{API_ENDPOINT}/chat", json={"message": text})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to get response from the server."


def text_to_speech(text):
    tts = gTTS(text=text, lang='ko')
    tts.save("response.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    
    os.remove("response.mp3")


def record_and_send():
    with st.spinner("음성을 녹음 중..."):
        audio_data, sample_rate = record_audio()
    
    with st.spinner("음성을 처리 중..."):
        result = send_audio_get_response(audio_data, sample_rate)
        transcription = result["transcription"]
        response = result["response"]
        
        st.session_state.messages.append({'role': 'user', 'content': f"{transcription}"})
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        

        text_to_speech(response)


def main():
    st.title('음성 인식 기반 한국어 챗봇')
    

    if 'messages' not in st.session_state:
        st.session_state.messages = []


    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])


    if st.sidebar.button("음성 녹음 (5초)"):
        record_and_send()
        st.experimental_rerun()

    st.sidebar.title("개발자 정보")
    st.sidebar.markdown(
        """
        - **개발자**: 정강빈
        - **버전**: 1.0.0
        """
    )


    if prompt := st.chat_input('질문을 입력하세요'):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.markdown(prompt)

        with st.chat_message('assistant'):
            with st.spinner('답변 생성 중...'):
                response = send_text_get_response(prompt)
            st.markdown(response)
        
        st.session_state.messages.append({'role': 'assistant', 'content': response})
        


if __name__ == "__main__":
    main()