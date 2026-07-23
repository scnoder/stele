# Stele

A collection and organization app that extracts useful information from short or long videos (YouTube, Instagram Reels, etc.) and presents it in a clean, structured format.

## Problem & Goal

It's easy to stumble across great resources — scholarships, internships, opportunities — in Instagram Reels or YouTube videos, but hard to save and revisit them in a useful way. Apps like Albo exist but don't surface the specific details or listed items mentioned in the video. Stele fixes this: paste a video URL, and it downloads the audio, transcribes it, and uses an LLM to produce a detailed, organized breakdown — including any items, links, or resources mentioned.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12 + Flask |
| Video download | yt-dlp |
| Transcription | OpenAI Whisper (`base` model) |
| LLM analysis | Groq API — `llama-3.3-70b-versatile` |
| Frontend | Vanilla HTML/CSS/JS (served by Flask) |
| Env management | python-dotenv |

## How to run

```
python app.py
```

## Background

I kept running into the same problem: I would discover amazing scholarship and internship opportunities through Instagram videos, but I had no effective way to organize them or revisit the information later. While apps like Albo offered a similar concept, they didn't present the information in the way I needed, and they often missed the specific resources mentioned throughout the videos.

That challenge inspired me to start building a platform focused on collecting, organizing, and making valuable information from both short-form and long-form videos easy to save, search, and access. My goal is to help students spend less time scrolling and more time discovering opportunities that can shape their future.

## Environment

Requires a `.env` file in the project root (or a Replit Secret) with:


## Project structure

```
app.py               Flask server — / (UI) and /analyze (POST)
model.py             Groq client and LLM prompt
data_rendering.py    yt-dlp download + Whisper transcription
templates/
  index.html         Single-page frontend
requirements.txt     Python dependencies
```

## User preferences

- API keys stored in a `.env` file (loaded via python-dotenv) and/or Replit Secrets
