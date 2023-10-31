# Whisper Audio Transcriber

Note: To perform RAG on your audio, use the Jupyter notebook. Other files are for the Streamlit app which is currently only set up to transcribe the file and nothing else.


-------------- 

The Whisper Audio Transcriber is a user-friendly web application built with Streamlit for converting audio files to text using the Whisper ASR model.

## How to Run

1. Ensure you have Streamlit installed:

   ```bash
   pip install streamlit
   ```
2. Clone the repository

  ```bash  
  git clone https://github.com/ingridstevens/whisper-audio-transcriber.git
  ```
3. Navigate to the project directory

   
  ```bash
  cd whisper-audio-transcriber
  ```

4. Run the application with Streamlit
  ```bash
  streamlit run streamlit-whisper.py
  ```

5. Access the application at

  `http://localhost:8501`


## Features

* Simple and intuitive user interface.
* Supports uploading of common audio formats (WAV, MP3, M4A).
* Provides audio playback for easy content review.
* Accurate transcription using the Whisper ASR model.
* Display and download transcribed text.


## Use Cases

* Content creators, researchers, and general users can benefit from efficient audio-to-text transcription.

## Technology Stack

* Streamlit: Simplifies web app development with Python.
* Whisper ASR Model: Powers accurate audio transcription.


## TODOs / Wish List 

* add a button to download transcribed content
* add functionality to enter in youtube video URLs to generate transcripts / or alternatively SRT files for captions
* integrate with openai & use langchain to query the transcript 

Enjoy transcribing your audio content effortlessly with the Whisper Audio Transcriber!

