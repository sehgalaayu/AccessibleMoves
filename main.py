import speech_recognition as sr
import pyttsx3

# Initialize the Google Cloud Speech client
import google.cloud.speech_v1p1beta1 as speech

# Initialize the pyttsx3 engine
engine = pyttsx3.init(driverName='nsss')




def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio_data = recognizer.listen(source)

    try:
        # Use Google Cloud Speech to recognize the audio
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio_data.frame_data)
        config = speech.RecognitionConfig(language_code="en-US")
        
        response = client.recognize(config=config, audio=audio)
        
        # Get the recognized text
        for result in response.results:
            return result.alternatives[0].transcript.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

def run_gui():
    # Your GUI code here
    
    while True:
        command = recognize_speech()
        
        if command:
            if "start navigation" in command:
                # Handle start navigation command
                engine.say("Starting navigation")
                engine.runAndWait()
            elif "stop" in command:
                # Handle stop command
                engine.say("Stopping")
                engine.runAndWait()
            elif "turn left" in command:
                # Handle turn left command
                engine.say("Turning left")
                engine.runAndWait()
            elif "turn right" in command:
                # Handle turn right command
                engine.say("Turning right")
                engine.runAndWait()

if __name__ == "__main__":
    run_gui()
