import yt_dlp
import os

import whisper

model = whisper.load_model("base")


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


def transcribe(file_path: str):
    try:
        print("File passed to Whisper:", file_path)
        print("Absolute path:", os.path.abspath(file_path))
        print("Exists:", os.path.exists(file_path))

        result = model.transcribe(file_path, fp16=False)

        return result["text"]

    except Exception as e:
        return {
            "error": str(e),
            "message": "Sorry, there was an error processing the video.",
        }