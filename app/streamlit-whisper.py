import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

def load_whisper_model():
    # Load the Whisper ASR model
    st.sidebar.success(":tada: Whisper model loaded")
    return whisper.load_model("base")

def transcribe_audio(audio_file):
    # Transcribe the audio using the Whisper model
    with NamedTemporaryFile() as temp:
        temp.write(audio_file.getvalue())
        temp.seek(0)
        model = load_whisper_model()
        result = model.transcribe(temp.name, fp16=False)
        transcription_text = result.get("text", "")
        return transcription_text


def display_audio(audio_file):
    # Display the original audio in the sidebar
    st.sidebar.header("Play Original Audio")
    st.sidebar.audio(audio_file)  

def display_transcription(audio_file):
    transcription = transcribe_audio(audio_file)
    if transcription:
        # Display the transcription result in a text area
        text_area = st.empty()
        text_area.text_area("Transcribed Text", transcription)
        st.sidebar.success(":tada: Transcription complete")
    else:
        st.sidebar.error("No audio file uploaded")


def main():
    # Set the title of the app
    st.title("Whisper Audio Transcriber :speaker:")
    st.sidebar.text("Progress...")
    # Sidebar: Upload audio file
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])
    if audio_file:
        st.sidebar.success(":tada: Audio file uploaded")

    # Display a success message in the sidebar once the Whisper model is loaded

    if st.button("Transcribe Audio", type="primary"):
        if audio_file is not None:
            display_transcription(audio_file)
        else:
            st.sidebar.error("No audio file uploaded")
       
       

if __name__ == "__main__":
    main()
