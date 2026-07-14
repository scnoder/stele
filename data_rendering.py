import yt_dlp
import whispher
import os

def download_video(url: str) -> str:
    filename = "audio"
    
    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{filename}.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    return "audio.mp3"

def transcribe(url: str) -> str:
    """
        Download the video from the provided URL, extract the audio, and transcribe it using OpenAI's Whisper model.
    """
    try:
        audio_file = download_video(url)
        model = whispher.load_model("base")
        result = model.transcribe(audio_file)
        
        os.remove(audio_file)  # Clean up the audio file after transcription

        return result["text"]
    except Exception as e:
        return {"error": str(e),
                "message": "Sorry, there was an error processing the video. Please ensure the URL is valid and try again."}
    