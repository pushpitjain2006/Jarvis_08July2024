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


his = []


def AI(c, history=None):
    if history is None:
        history = []
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


News_api_link = "Your API Key"


def processcommand(c: str):
    c = c.lower()
    if 'open' in c:
        for web in websites:
            if web in c:
                webbrowser.open(websites[web])
                return f"Opening {web}"
    elif 'search' in c:
        c = c.replace("search", "")
        c = c.replace(" on google", "")
        google_search(c)
        return f"Searching for{c}"

    elif 'news' in c:
        req_get = requests.get(News_api_link)
        if req_get.status_code == 200:
            data = req_get.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
            return "Here are the top news headlines"
        else:
            speak("Sorry unable to get News currently")
            return "Sorry unable to get News currently"
    elif 'define' in c:
        word = c[7::]
        req_get = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if req_get.status_code == 200:
            data = req_get.json()
            speak(f"the word {word} is defined as" + data[0]["meanings"][0]["definitions"][0]["definition"])
        else:
            AI(c, his)
            return "Artificial Intelligence"
        return f"{c} is defined as .."

    else:
        AI(c, his)
        return "Artificial Intelligence"


if __name__ == "__main__":
    if __name__ == "__main__":
        print("Initializing Jarvis.....")
        speak("Initializing Jarvis.....")
        r = sr.Recognizer()
        while True:
            try:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source, phrase_time_limit=5, timeout=5)
                command = r.recognize_google(audio)
                print(command)
                if command.lower() == "jarvis":
                    print("Hello sir")
                    speak("Hello sir")
                    try:
                        with sr.Microphone() as source:
                            print("Jarvis active!")
                            cmd = r.listen(source, phrase_time_limit=5, timeout=5)
                            command2 = r.recognize_google(cmd)
                            processcommand(command2)
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
