from groq import Groq
import os

def _get_groq_client():
    """Initialize and return a Groq client using GROQ_API_KEY from .env."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not set. Add it to a .env file in the project root."
        )
    return Groq(api_key=api_key)

SYSTEM_PROMPT = "You are Stele, a helpful assistant that provides information about the the videos that were provided to you. Your job is to provide detailed and helpful information using markup language."

def new_session(transcript: str, video_url: str) -> dict:
    """
        Initialize and return a fresh session dict for one user interaction.
    """

    return {
        "transcript": transcript,
        "video_url": video_url
    }

def run_model(transcript: str, video_url: str) -> str:
    """
        Run the model with the provided transcript and video URL, returning the model's response.
    """
    client = _get_groq_client()
    session = new_session(transcript, video_url)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""
             Please provide detailed information about the video at {video_url} based on the following transcript: {transcript}.
             Use the information from the video to summarize what the video says and any additional and useful information related to the video.
             Please provide your response in a clear and organized manner, using headings, bullet points, and any other formatting that enhances readability.
             """},
            {"role": "user", "content": transcript}
        ]
    )

    return response.choices[0].message.content