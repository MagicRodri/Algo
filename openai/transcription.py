import logging
import os
import random
import textwrap
from pathlib import Path

import requests
import whisper
from dotenv import load_dotenv
from pytube import YouTube


def rephrase(text: str, api_key: str) -> str:
    """Rephrase recursivly text using AI21 API"""
    print(len(text))
    MAX_LENGTH = 500
    base_url = "https://api.ai21.com/studio/v1/"
    segmentation_url = f"{base_url}segmentation"
    paraphrase_url = f"{base_url}paraphrase"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    if len(text) <= MAX_LENGTH:
        paraphrase_response = requests.post(paraphrase_url,
                                            headers=headers,
                                            json={
                                                "style": "formal",
                                                "text": text
                                            })
        paraphrase_response.raise_for_status()
        random_paraphrase = random.choice(
            paraphrase_response.json()["suggestions"])['text']
        return random_paraphrase

    segments = textwrap.wrap(text=text,
                             width=MAX_LENGTH,
                             fix_sentence_endings=True)
    for segment in segments:
        print(segment)
        print()
    # segment_response = requests.post(segmentation_url, headers=headers, json={
    #     "sourceType": "TEXT",
    #     "source": text,
    # })
    # segment_response.raise_for_status()
    # segments = segment_response.json()["segments"]
    # paraphrase_list = []
    # for segment in segments:
    #     segment_text = segment['segmentText']
    #     segment_paraphrase = rephrase(segment_text,api_key)
    #     paraphrase_list.append(segment_paraphrase)
    # paraphrase = " ".join(paraphrase_list)
    # return paraphrase


def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    AI21_API_KEY = os.getenv("AI21_API_KEY")

    transcriptions_base_path = Path("transcriptions")
    url = "https://www.youtube.com/watch?v=dCxSsr5xuL8"
    # url = "https://www.youtube.com/watch?v=8lGpZkjnkt4"

    # Download audio from youtube
    yt = YouTube(url)
    title = yt.title
    audio_stream = yt.streams.filter(only_audio=True).first()
    filename = f'{title}.mp3'
    output_path = transcriptions_base_path / title
    # audio_stream.download(filename=filename,output_path=str(output_path))

    # # Transcribe audio
    # model = whisper.load_model("base")
    # result = model.transcribe(str(output_path / filename))
    # with open(output_path / f'{title}.txt','w') as f:
    #     f.write(result["text"])

    with open(output_path / "Nuxt in 100 Seconds.txt", 'r') as f:
        text = f.read()
        paraphrase = rephrase(text, AI21_API_KEY)
        with open(output_path / f'{title}_paraphrase.txt', 'w') as f:
            f.write(paraphrase)


if __name__ == '__main__':
    main()