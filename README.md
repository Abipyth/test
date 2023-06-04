Assignment 1: Real-time Voice Transcription App

Objective: Create a real-time voice transcription app using Streamlit.

Introduction: The Real-time Voice Transcription App is a web application that allows users to transcribe their speech in real-time. With just a click of a microphone button, users can have their speech automatically transcribed as they speak. This app utilizes Streamlit to provide a user-friendly interface and a seamless transcription experience.

Technologies Used: Python, Streamlit, sounddevice, SpeechRecognition, puaudio

Key Features:

    Real-time transcription: Transcribe speech in real-time as the user speaks.
    Microphone input: Capture audio input through the microphone.
    Speech recognition: Utilize speech recognition libraries to convert audio into text.
    User-friendly interface: Streamlit provides an intuitive and easy-to-use interface for a seamless transcription experience.

Installation:
Open a terminal or command prompt.
Ensure you have Python and pip installed on your system.
Install the Streamlit library by running the following command:
pip install streamlit
Wait for the installation to complete. Once it's finished, try running the Streamlit app again using the command:
python -m streamlit run realtime_transcription_app.py

Usage:

    Launch the app by running streamlit run app.py.
    Click the "Initialize transcription" button to begin capturing audio.
    Speak into the microphone to have your speech transcribed in real-time.
    The transcribed text will be displayed in the text area.

Assignment 2: Implement Token Healing in Python

Objective: Understand token healing as implemented in Microsoft's GUIDANCE and create a standalone Python script to perform token healing on a given text.

Introduction: Token Healing is a technique used to correct errors in text by identifying and replacing incorrect or mistyped tokens with their intended correct forms. The Python script developed for this assignment implements token healing, inspired by Microsoft's GUIDANCE. It aims to enhance the quality of text data by automatically correcting common errors.

Technologies Used: Python, Spellchecker

Key Features:

    Token Healing: Identify and replace incorrect or mistyped tokens with their correct forms.
    Error Correction: Improve the quality of text data by automatically correcting common errors.
    Standalone Script: The Python script can be run independently on any given text.

Installation:

    Download or clone the repository.
    Ensure Python is installed on your system.
    Run the script using python token_healing_text.py.

Usage:

    Prepare a text file or provide a string input containing the text to be processed.
    Run the token_healing_text.py script.
    The script will analyze the text and perform token healing, correcting errors and improving the overall quality.
    The corrected text will be displayed or saved, depending on the script configuration.

Assignment 3: Optimize Prompt Text for Language Model API Calls

Objective: Develop a method to reduce the token count of prompt text without losing critical information, to minimize token usage when calling language models like GPT-3.

Introduction: The Optimize Prompt Text script is a tool developed to reduce the token count of prompt text without sacrificing important information. When interacting with language model APIs like GPT-3, minimizing token usage is crucial for cost efficiency and response time. This script offers an optimization method to maximize the utilization of available tokens while preserving critical information.

Technologies Used: Python

Key Features:

    Token Count Reduction: Minimize the token count of prompt text.
    Information Preservation: Preserve critical information during token optimization.

Installation:

    Ensure Python is installed on your system.
    Run the script using python reduce_token_count.py


