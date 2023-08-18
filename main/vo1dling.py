import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize speech recognition engine
r = sr.Recognizer()
r.pause_threshold = 1

# Initialize text-to-speech engine
engine = pyttsx3.init()

wake_word = "void"


# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


def open_website(url):
    webbrowser.open(url)
    speak("Opening website.")


def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")


# Check if wake-up keyword is detected
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

if wake_word in r.recognize_google(audio):
    speak("Yes sir?")

    # Listen for command
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)

    try:
        # Convert speech to text
        command = r.recognize_google(audio)
        print("You said: " + command)

        # Execute command
        if "open" in command:
            if "website" in command:
                url = command.split()[-1]
                open_website(url)
            else:
                speak("I'm not sure what you want me to open.")
        elif "time" in command:
            tell_time()
        else:
            speak("I'm sorry, I didn't understand that.")

    except sr.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
    except sr.RequestError as e:
        speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
