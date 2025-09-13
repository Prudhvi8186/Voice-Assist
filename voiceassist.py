import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("\nAvailable microphones:")
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {mic_name}")

mic_index = int(input("\nEnter the number for your microphone: "))
print(f"Using microphone: {sr.Microphone.list_microphone_names()[mic_index]}")


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_limit=5):
    """Listen for a single phrase with timeout"""
    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            query = recognizer.recognize_google(audio).lower()
            print(f"You said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, could not understand.")
            return ""
        except sr.RequestError:
            print("Speech recognition service error.")
            return ""

def main():
    speak("Hello! I am your assistant. How can I help?")
    while True:
        command = listen()
        if not command:
            continue

        
        if "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "search" in command:
            search_term = command.replace("search", "").strip()
            if search_term:
                speak(f"Searching for {search_term}")
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
            else:
                speak("Please tell me what to search for.")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {now}")

        elif "hello" in command:
            speak("Hello! How are you today?")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I am not sure how to do that yet.")

if __name__ == "__main__":
    main()
