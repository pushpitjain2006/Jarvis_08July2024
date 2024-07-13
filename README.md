# J.A.R.V.I.S - Just A Rather Very Intelligent System

## Overview

J.A.R.V.I.S is a voice-activated assistant built using Python. It uses several libraries to handle different functionalities such as speech recognition, text-to-speech, and web browsing. The assistant can perform tasks like searching on Google, fetching news, and defining words, among others.

## Features

- **Voice Commands:** Activate and control the assistant with your voice.
- **Google Search:** Perform Google searches using voice commands.
- **News Updates:** Fetch and read out the latest news headlines.
- **Word Definitions:** Get definitions of words using an online dictionary API.
- **Customizable Websites:** Open predefined websites with voice commands.

## Installation

### Prerequisites

- Python 3.7 or higher
- Required libraries: transformers, torch, speech_recognition, gtts, pygame, webbrowser, requests

### Setting Up

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required libraries:
    ```bash
    pip install transformers torch speechrecognition gtts pygame requests
    ```

3. Set up the News API key:
    Replace `your_news_api_key` in the code with your actual News API key.

## Usage

1. Run the `jarvis.py` script:
    ```bash
    python jarvis.py
    ```

2. Upon running, the assistant initializes and waits for voice commands. Say "Jarvis" to activate it and then provide your command.

## How It Works

### Speech Recognition

- The assistant uses the `speech_recognition` library to capture and interpret voice commands.

### Text-to-Speech

- The `gtts` (Google Text-to-Speech) library converts text responses into speech which is played back using the `pygame` library.

### Natural Language Processing

- The `transformers` library with the `microsoft/DialoGPT-medium` model processes and generates responses for general queries.

### Web Integration

- The `webbrowser` module is used to open predefined websites.
- The `requests` module fetches news and dictionary definitions from online APIs.

## Configuration

### Adding Custom Websites

You can add or modify the websites the assistant can open by editing the `websites` dictionary in the `dict.py` file.

### Changing the API Keys

- **News API:** Update the `News_api_link` variable with your API key.
- **Dictionary API:** The assistant uses a free online dictionary API that does not require an API key.

## Known Issues

- The voice recognition might not work perfectly in noisy environments.
- Some commands might not be processed correctly due to speech recognition inaccuracies.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the `transformers` library and models.
- [Google Text-to-Speech](https://pypi.org/project/gTTS/) for the TTS functionality.
- [Pygame](https://www.pygame.org/) for the audio playback.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for capturing voice commands.

Feel free to contribute to this project by adding more features or improving the existing ones.
