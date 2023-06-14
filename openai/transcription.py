import logging
from pathlib import Path

import whisper
from pytube import YouTube


def main():
    logging.basicConfig(level=logging.INFO)

    transcriptions_base_path = Path("transcriptions")
    # url = "https://www.youtube.com/watch?v=dCxSsr5xuL8"
    url = "https://www.youtube.com/watch?v=8lGpZkjnkt4"
    yt = YouTube(url)
    title = yt.title
    audio_stream = yt.streams.filter(only_audio=True).first()
    filename = f'{title}.mp3'
    output_path = transcriptions_base_path / title
    audio_stream.download(filename=filename,output_path=str(output_path))

    model = whisper.load_model("base")
    result = model.transcribe(str(output_path / filename))
    with open(output_path / f'{title}.txt','w') as f:
        f.writelines(result['text'])


if __name__ == '__main__':
    main()