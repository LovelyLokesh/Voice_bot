import speech_recognition as sr
from gtts import gTTS
import tempfile

def speech_to_text(audio_path):
    """Convert speech from an audio file to text."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Error connecting to the speech recognition service."

def text_to_speech(response_text):
    """Convert text to speech and return the audio file path."""
    tts = gTTS(text=response_text, lang="en", slow=False)
    temp_audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    tts.save(temp_audio_path)
    return temp_audio_path
