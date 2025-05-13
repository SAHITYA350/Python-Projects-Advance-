 # --- J.A.R.V.I.S Voice Assistant --- #
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import datetime
import os

# ✅ Explicit import of PyAudio
try:
    import pyaudio
except ImportError:
    print("❌ PyAudio not found. Install it using: pip install pyaudio")
    exit()


# ✅ Setup text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ✅ Voice recognition function
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("🔎 Recognizing...")
            data = recognizer.recognize_google(audio)
            print("🗣️ You said:", data)
            return data.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("⚠️ Could not request results from Google Speech service.")
            speak("Could not request results from Google Speech service.")
            return ""

# ✅ Tell time
def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak("The time is " + now)
    print("🕒 Time:", now)

# ✅ Tell joke
def tell_joke():
    joke = pyjokes.get_joke(language="en", category="all")
    speak(joke)
    print("🤖 ::", joke)
    speak("anything else sir, i will help you")            
    print("🤖  ::  anything else sir, i will help you")      

# ✅ Play music
def open_music():
    music_dir = r"C:\Users\Sahitya\OneDrive\Desktop\Musics"
    if os.path.exists(music_dir):
        songs = os.listdir(music_dir)
        if songs:
            speak(" Playing music")
            speak("anything else sir, i will help you")            
            print("🤖  ::  anything else sir, i will help you")             
            os.startfile(os.path.join(music_dir, songs[1]))
        else:
            speak("No songs found in the folder.")
    else:
        speak("Music directory not found.")

# ✅ Open camera
def open_camera():
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        speak(" Opening camera. Press Q to close.")
        speak("anything else sir, i will help you")            
        print("🤖  ::  anything else sir, i will help you")     
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except ImportError:
        speak("OpenCV is not installed. Please install it to use the camera.")

# ✅ Greet user
print("🤖  ::  Welcome Sir. I am Jarvis. What shall we begin with today?")
speak("Welcome Sir. I am Jarvis. What shall we begin with today?")



# ✅ Main loop
if __name__ == '__main__':
    while True:
        command = sptext()

        if any(phrase in command for phrase in ["your name", "what is your name", "what's your name"]):
            speak("My name is Jarvis")
            print("🤖  ::  My name is Jarvis")
            speak("anything else sir, i will help you")            
            print("🤖  ::  anything else sir, i will help you") 


        elif any(phrase in command for phrase in ["turn on jarvis", "turn on", "jarvis", "jarvis on"]):
            speak("System activated")
            print("🤖  ::  System ACTIVATED")
            speak("anything else sir, i will help you")            
            print("🤖  ::  anything else sir, i will help you") 
        

        elif any(phrase in command for phrase in ["how old are you", "launch date", "born"]):
            speak("I don't have an age like a person, but I was released in my current form in 2025.")
            print("🤖  ::  I was released in my current form in 2025.")
            speak("anything else sir, i will help you")            
            print("🤖  ::  anything else sir, i will help you") 
            

        elif any(phrase in command for phrase in ["time", "what is the time", "time now", "what's the time"]):
            tell_time()
            
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you") 

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")
            print("🤖  ::  anything else sir, i will help you") 

        elif "code with harry" in command:
            speak("Opening Code With Harry's YouTube channel")
            webbrowser.open("https://www.youtube.com/@CodeWithHarry")
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you") 

        elif any(phrase in command for phrase in ["open my ld", "open sahitya ghosh ld", "my ld"]):
            speak("Opening your LinkedIn")
            webbrowser.open("http://www.linkedin.com/in/sahitya-ghosh-9ba098292")
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you")

        elif "play music" in command or "music" in command:
            open_music()

        elif any(phrase in command for phrase in ["joke", "make a joke", "break a joke"]):
            tell_joke()

        elif "open whatsapp" in command:
            speak("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you") 

        elif "open camera" in command:
            open_camera()
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you") 

        elif "search" in command:
            speak("What should I search?")
            query = sptext()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here is what I found for {query}")
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you")


        elif any(phrase in command for phrase in ["exit", "shutdown", "bye"]):
            speak("Goodbye sir. Powering down systems.")
            print("🤖  ::  Goodbye sir. Powering down systems...")
            break

        elif command != "": 
            speak("I did not understand that. Please try again.")
            speak("anything else sir, i will help you")
            print("🤖  ::  anything else sir, i will help you")
            
            
                
