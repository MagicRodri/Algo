import whisper

model = whisper.load_model("base")
result = model.transcribe("audio_fr.mp3")
print(result["text"])