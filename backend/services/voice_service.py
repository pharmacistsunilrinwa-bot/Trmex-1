import os
from openai import OpenAI
from gtts import gTTS
import tempfile

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class VoiceService:
    @staticmethod
    async def speech_to_text(audio_file_path: str) -> str:
        with open(audio_file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        return transcript.text

    @staticmethod
    async def text_to_speech(text: str) -> str:
        # Using Google TTS for free/easy implementation, or can swap to OpenAI TTS
        tts = gTTS(text=text, lang='en')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name

voice_service = VoiceService()
