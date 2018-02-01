from alice import Alice
import speech_recognition as sr

GOOGLE_SPEECH_RECOGNITION_API_KEY = None
bot = Alice()

def run_transcription_loop():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            r.adjust_for_ambient_noise(source)
            print("Awaiting user input.")
            audio = r.listen(source)
            print("Attempting to transcribe user input.")
            try:
                result = r.recognize_google(
                    audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY
                )
                bot.handle_action(result)
            except sr.UnknownValueError:
                print("Unable to understand audio")
            except sr.RequestError:
                print("Internet connection error")
            except Exception as e:
                print(e)
                print("I don't know :/")


if __name__ == '__main__':

    bot.speak("Hi Mayank")
    run_transcription_loop()
