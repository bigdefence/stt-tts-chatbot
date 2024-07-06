# 🎤💬 한국어 음성 지원 챗봇

음성 인식과 텍스트 음성 변환 기능을 갖춘 Streamlit 기반 챗봇 애플리케이션입니다. 한국어 언어 모델을 활용하여 자연스러운 대화를 제공합니다.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688)

## ✨ 주요 기능

- 🎙️ Whisper를 이용한 음성-텍스트 변환 입력
- ⌨️ 텍스트 기반 채팅 입력
- 🤖 Llama3의 Bllosom 강력한 언어 모델 활용을 사용한 AI 응답 생성
- 🔊 AI 응답의 텍스트-음성 변환 출력
- 🖥️ 사용자 친화적인 Streamlit 인터페이스

## 🚀 시작하기
### 라이브러리 설치
```bash
   pip install -r requirements.txt
   ```

### 서버 설정

1. 서버 실행:
   ```bash
   python server.py
   ```

### 클라이언트 설정

1. Streamlit 앱 실행:
   ```bash
   streamlit run client.py
   ```

## 📘 사용 방법

1. 서버를 시작하고 ngrok 공개 URL을 확인합니다.
2. `client.py`의 `API_ENDPOINT`를 ngrok URL로 업데이트합니다.
3. Streamlit 앱을 실행합니다.
4. 사이드바의 "음성 녹음" 버튼을 사용하여 음성 입력을 하거나 채팅 입력창에 질문을 입력합니다.
5. AI의 응답을 텍스트로 확인하고 음성으로 들을 수 있습니다.

## 🛠️ 사용된 기술

- FastAPI
- Streamlit
- Transformers (Hugging Face)
- Whisper (OpenAI)
- PyTorch
- gTTS (Google Text-to-Speech)
- LLaMA3 (Meta LLM)

## 👨‍💻 개발자 정보

- **이름**: 정강빈
- **버전**: 1.0.0

## 📄 라이선스

[여기에 라이선스를 명시하세요]

## 🤝 기여하기

프로젝트에 기여하고 싶으신가요? 훌륭합니다! 
다음 단계를 따라주세요:

1. 이 저장소를 포크합니다.
2. 변경사항을 커밋합니다.
3. 브랜치를 푸시합니다.
4. 풀 리퀘스트를 열어주세요.

## ⭐ 프로젝트 지원하기

이 프로젝트가 마음에 드셨나요? 별표를 눌러주세요! ⭐
