from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify
from data_rendering import download_video, transcribe
from model import run_model
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "Please provide a video URL."}), 400

    try:
        audio_path = download_video(url)
        transcript = transcribe(audio_path)

        if isinstance(transcript, dict) and "error" in transcript:
            return jsonify({"error": transcript["message"]}), 500

        result = run_model(transcript, url)
        return jsonify({"result": result, "transcript": transcript})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)