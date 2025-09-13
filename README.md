# Voice-Assist
Python Voice Assistant

A simple voice-controlled assistant built with Python that can:

Open websites

Perform Google searches

Tell the current time

Greet you

Respond to basic commands

It uses speech recognition and text-to-speech (TTS) to interact with the user.

🚀 Features

🎙️ Speech Recognition with speech_recognition

🔊 Text-to-Speech with pyttsx3

🌐 Open Google or perform searches

⏰ Get the current time

👋 Simple greetings

❌ Exit on "stop" or "exit" command

📦 Requirements

Make sure you have Python installed (>=3.7). Install dependencies:

pip install speechrecognition pyttsx3 pyaudio


👉 Note: On some systems, you may need to install pyaudio separately:

Windows: pip install pipwin && pipwin install pyaudio

Linux/macOS: brew install portaudio or use your package manager

🛠️ How to Run

Clone the repository:

git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant


Run the script:

python assistant.py


Choose your microphone from the list shown at startup.

Start giving commands like:

"open google"

"search python programming"

"time"

"hello"

"stop"

📂 Project Structure
voice-assistant/
│── assistant.py   # Main script
│── README.md      # Project description

🧑‍💻 Example Output
Available microphones:
0: Microphone (Realtek Audio)
1: USB Microphone
Enter the number for your microphone: 0
Using microphone: Microphone (Realtek Audio)

Assistant: Hello! I am your assistant. How can I help?
Listening...
You said: open google
Assistant: Opening Google.

🔮 Future Improvements

Add weather updates 🌦️

Open apps (e.g., Notepad, Calculator)

Play music 🎵

Remember user preferences

📜 License

This project is licensed under the MIT License.
