import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

def process_voice_input(file_path):
    # Convert voice file to WAV format
    audio = AudioSegment.from_ogg(file_path)
    wav_path = file_path.replace(".ogg", ".wav")
    audio.export(wav_path, format="wav")

    # Recognize speech
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        query = recognizer.recognize_google(audio_data)

    # Process query
    from bot.nlp import process_input
    response_text = process_input(query)

    # Convert text response to speech
    tts = gTTS(response_text)
    response_audio_path = "response.mp3"
    tts.save(response_audio_path)
    
    return response_audio_path
