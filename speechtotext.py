import speech_recognition as sr
import pyttsx3
import cv2

# Initialize recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    
    while True:
        try:
            # Use mic as input source
            with sr.Microphone() as source2:
                        
                # Prep recognizer to receive input and prep for ambient noise
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listens to user input
                audio2 = r.listen(source2)

                # Use Google to recognize audio
                UserWord = r.recognize_google(audio2)
                first_word= UserWord.split()[0]
                return first_word
                    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")

def output_text(text):
    # Gives access to output txt file, 'a' indicates we will append text to the end
    with open("output.txt", "a") as f:
        f.write(text)
        f.write("\n")

    return



while True:
    text = record_text()
    output_text(text)

    print("You said:",text)

   
