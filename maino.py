# import sounddevice as sd
# import soundfile as sf
import speech_recognition as sr
# import os
import tempfile
from gtts import gTTS
import pygame
import webbrowser
from dict import websites
import requests
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
# import torch
# import chatbot
# import openai
# from crewai import Agent, Task, Crew

# openai_api_key = "sk-proj-BWPEIPwaTfoA84gNFR42T3BlbkFJu7VNmLbFj5XkCMNDQmwJ"
# os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
# chatbot.demo()

# Initialize pygame mixer
# from transformers import pipeline, set_seed


# def AI(input_text):
#     '''# Initialize the text generation pipeline with GPT-2
#     device = 0 if torch.cuda.is_available() else -1
#     generator = pipeline('text-generation', model='gpt2', device=device)
#
#     # Set a seed for reproducibility
#     set_seed(42)
#
#     # Generate the response
#     # response = generator(input_text, max_length=50, num_return_sequences=1, truncation=True)
#     response = generator(input_text,num_return_sequences=1,
#         truncation=True,  max_length=100, temperature=0.9, top_k=50, top_p=0.95)
#
#     # Return the generated text
#     speak(response[0]['generated_text'])'''
#     pass
# from transformers import pipeline

# Example usage
# input_text = "Hello, I'm a language model,"
# response = generate_response(input_text)
# print(response)


pygame.mixer.init()
# def speak_old(text):
#     # Convert text to speech and save to a temporary file
#     tts = gTTS(text)
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
#         tts.save(fp.name)
#         temp_filename = fp.name
#
#     # Load and play the audio file
#     pygame.mixer.music.load(temp_filename)
#     pygame.mixer.music.play()
#
#     # Wait until the audio is finished playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#
#     # Remove the temporary file
#     os.remove(temp_filename)

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



'''def speak(text):
    # Convert text to speech and save to a temporary file
    tts = gTTS(text)
    # print("1-",type(tts))
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as fp:
        tts.save(fp.name)
        temp_filename = fp.name
        # print("2-",type(fp))
        # print("3-",type(temp_filename))

    # Load the audio data from the file
    data, sample_rate = sf.read(temp_filename)
    # print("3-",type(data))
    # print("4-",type(sample_rate))

    # Playing the audio data
    sd.play(data, sample_rate)
    sd.wait()  # Wait until the audio is finished playing

    # Remove the temporary file
    os.remove(temp_filename)'''


# def AI(c):
#     # Initialize the text generation pipeline with a model from Hugging Face
#     generator = pipeline('text-generation', model='gpt2')
#
#     # Generate a response for the given command
#     response = generator(c, max_length=100, num_return_sequences=1)
#
#     # Extract and return the generated text
#     print(response[0]['generated_text'])
#     speak(response[0]['generated_text'])
# def AI(c):
#     # Initialize the question-answering pipeline with a model from Hugging Face
#     qa_pipeline = pipeline('question-answering', model='deepset/roberta-base-squad2')
#
#     # Context needs to be provided for better answers. Here, we'll use a general context for demo purposes.
#     context = """
#     Paris is the capital and most populous city of France. The city has a population of 2,148,271 inhabitants as of 2020, within its administrative limits. Paris has been one of Europe's major centers of finance, diplomacy, commerce, fashion, science, and arts.
#     """
#
#     # Generate a response for the given command
#     response = qa_pipeline(question=c, context=context)
#
#     # Extract and return the answer
#     print( response['answer'])
#     speak(response['answer'])

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
his=[]

# def AI(c, history=[]):
#     # Load the model and tokenizer
#     model_name = "microsoft/DialoGPT-medium"
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
#     model = AutoModelForCausalLM.from_pretrained(model_name)
#
#     # Append the new user input to the chat history
#     new_user_input_ids = tokenizer.encode(c + tokenizer.eos_token, return_tensors='pt')
#     bot_input_ids = torch.cat([torch.tensor(history, dtype=torch.int64), new_user_input_ids],
#                               dim=-1) if history else new_user_input_ids
#
#     # Generate the response
#     chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#
#     # Decode the response and add to history
#     response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
#     global his
#     his = chat_history_ids.tolist()[0]  # Update history with the new chat history
#
#     # return response, history
#     print(response)
#     speak(response)
def AI(c, history=[]):
    # if history is None:
    #     history = []  # Initialize history if it's None

    # Load the model and tokenizer
    model_name = "microsoft/DialoGPT-medium"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Append the new user input to the chat history
    new_user_input_ids = tokenizer.encode(c + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([torch.tensor(history, dtype=torch.int64), new_user_input_ids],
                              dim=-1) if history else new_user_input_ids

    # Generate the attention mask
    attention_mask = torch.ones_like(bot_input_ids)  # Initialize to all 1s
    if history:
        attention_mask[:, :history[-1].shape[-1]] = 0  # Set 0s for the padding tokens in history

    # Generate the response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id,
                                      attention_mask=attention_mask)

    # Decode the response and add to history
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    his.append(chat_history_ids)  # Update history with the new chat history

    print(response)
    speak(response)
def google_search(query):
    base_url = "https://www.google.com/search?q="
    encoded_query = query.replace(' ', '+')
    url = base_url + encoded_query
    webbrowser.open(url)


News_api_link = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b391114c4590453182c8c0d7430e7dd4"


def processcommand(c: str):
    '''print(c)
    speak(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")'''
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
            # meanings = data.get('meanings',[])
            # speak(meanings['definitions']['definition'])
            speak(f"the word {word} is defined as" + data[0]["meanings"][0]["definitions"][0]["definition"])
        else:
            AI(c,his)

    else:
        #CHATBOT
        AI(c,his)


# AI('Hello how are you')
# processcommand('Hello how are you')
# processcommand("open youtube")
# processcommand("search pushpit jain linkedin on google")
# processcommand("news")
if __name__ == "__main__":
    print("Initializing Jarvis.....")
    speak("Initializing Jarvis.....")
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,phrase_time_limit=1, timeout=2)
            # print(r.recognize_google(audio))
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
