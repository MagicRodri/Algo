from gpt4all import GPT4All

model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')
with model.chat_session():
    response = model.generate(prompt='Give a title for the text', top_k=1)
    response = model.generate(prompt='What is python?', top_k=1)
    response = model.generate(prompt='thank you', top_k=1)
    print(model.current_chat_session)