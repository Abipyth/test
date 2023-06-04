import sys
sys.path.append("C:/users/abinaya/appdata/roaming/python/python311/site-packages")
import streamlit as st
import speech_recognition as sr
import pyaudio

def transcribe_speech():
    recognizer= sr.Recognizer()
    mic = sr.Microphone()
    
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            st.write("Listening.....")
            audio = recognizer.listen(source)
            st.write ("Transcribing.....")

    
        text= recognizer.recognize_google(audio)
        st.success ("Transcripted Voice: {}".format(text))
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand your speech.")
    except sr.RequestError:
        st.error ("Sorry, there was an issue with the speech recognition service.")

def main():
    st.title("Voice to Text App ")
    st.write("Click the 'Initialize Transcription' button and speak into your microphone")

    if st.button("Initialize Transcription"):
        transcribe_speech()

if __name__ == "__main__":
    main()
