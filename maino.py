from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser
from dict import websites
import requests
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'


pygame.mixer.init()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

his=[]

def AI(c, history=[]):
    model_name = "microsoft/DialoGPT-medium"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    new_user_input_ids = tokenizer.encode(c + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([torch.tensor(history, dtype=torch.int64), new_user_input_ids],
                              dim=-1) if history else new_user_input_ids
    attention_mask = torch.ones_like(bot_input_ids)  
    if history:
        attention_mask[:, :history[-1].shape[-1]] = 0  
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id,
                                      attention_mask=attention_mask)
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    his.append(chat_history_ids)  
    print(response)
    speak(response)

def google_search(query):
    base_url = "https://www.google.com/search?q="
    encoded_query = query.replace(' ', '+')
    url = base_url + encoded_query
    webbrowser.open(url)


News_api_link = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b391114c4590453182c8c0d7430e7dd4"


def processcommand(c: str):
    c = c.lower()
    if 'open' in c:
        for web in websites:
            if web in c:
                webbrowser.open(websites[web])
                break
    elif 'search' in c:
        c = c.replace("search", "")
        google_search(c.replace(" on google", ""))
    elif 'news' in c:
        r = requests.get(News_api_link)
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry unable to get News currently")
    elif 'define' in c:
        word = c[7::]
        r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if r.status_code == 200:
            data = r.json()
            speak(f"the word {word} is defined as" + data[0]["meanings"][0]["definitions"][0]["definition"])
        else:
            AI(c,his)

    else:
        AI(c,his)

if __name__ == "__main__":
    print("Initializing Jarvis.....")
    speak("Initializing Jarvis.....")
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,phrase_time_limit=1, timeout=2)
            command = r.recognize_google(audio)
            print(command)
            if command.lower() == "jarvis":
                print("hello sir")
                speak("hello sir")
                try:
                    with sr.Microphone() as source:
                        print("Jarvis active!")
                        cmd = r.listen(source, phrase_time_limit=1, timeout=2)
                        command2 = r.recognize_google(cmd)
                        processcommand(command2)
                except:
                    print("error 2")
        except:
            print("Error")
