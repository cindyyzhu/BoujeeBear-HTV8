import speech_recognition as sr
import time
from gtts import gTTS
import os

# Initialize recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = r.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    LVL1 = ["run", "rabbit", "yell", "tool", "bowl"]
    LVL2 = ["carrot", "bird", "horse", "earring", "giraffe"]
    LVL3 = ["spoon", "space", "spider", "sports", "sleeve"]
    NUM_Tries = 2
    PROMPT_LIMIT = 8
    language= 'en'

    welc = "Welcome to Bougie Bear Cards!"
    myobjw = gTTS(text=welc, lang=language, slow=False)
    myobjw.save("W.mp3")
    os.system("afplay W.mp3")
    

    # get a random word from the list
    for word in LVL1:
        # format the instructions string
        instructions = f"Repeat after me! {word}"
        myobj = gTTS(text=instructions, lang=language, slow=False)
        myobj.save("S.mp3")
        os.system("afplay S.mp3")
        time.sleep(0.5)

        for _ in range(NUM_Tries):
            # get the guess from the user
            for _ in range(PROMPT_LIMIT):
                print('Speak!')
                guess = record_text()
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")

            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                break

            # show the user the transcription
            print("You said: {}".format(guess["transcription"]))

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = NUM_Tries - 1 > 0

            # determine if the user has won the game
            if guess_is_correct:
                print("Correct! Let's move on to the next one!")
                break
            elif user_has_more_attempts:
                print("Close! Let's try again.")
            else:
                print("Not quite right, let's try again!".format(word))
                break

        # If the last word was correctly guessed, print the completion message
        if guess_is_correct and word == LVL1[-1]:
            print("Congratulations! You've completed level 1. Good job!")
            cont=input("Do you want to try level medium? Type Y for yes N for no: ")
            if cont== 'Y' or 'y':
                break
            elif cont== 'N' or 'n':
                exit()

    

    for word in LVL2:
        instructions = f"Repeat after me! {word}"
        myobj = gTTS(text=instructions, lang=language, slow=False)
        myobj.save("S.mp3")
        os.system("afplay S.mp3")
        time.sleep(0.5)

        for _ in range(NUM_Tries):
            # get the guess from the user
            for _ in range(PROMPT_LIMIT):
                print('Speak!')
                guess = record_text()
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")

            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                break

            # show the user the transcription
            print("You said: {}".format(guess["transcription"]))

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = NUM_Tries - 1 > 0

            # determine if the user has won the game
            if guess_is_correct:
                print("Correct! Let's move on to the next one!")
                break
            elif user_has_more_attempts:
                print("Close! Let's try again.")
            else:
                print("Not quite right, let's try again!".format(word))
                break
        # If the last word was correctly guessed, print the completion message
        if guess_is_correct and word == LVL1[-1]:
            print("Congratulations! You've completed level 2. You are making great progress good job!!")
            cont=input("Do you want to try level medium? Type Y for yes N for no: ")
            if cont== 'Y' or 'y':
                break
            elif cont== 'N' or 'n':
                exit()
            
    for word in LVL3:
        instructions = f"Repeat after me! {word}"
        myobj = gTTS(text=instructions, lang=language, slow=False)
        myobj.save("S.mp3")
        os.system("afplay S.mp3")
        time.sleep(0.5)

        for _ in range(NUM_Tries):
            # get the guess from the user
            for _ in range(PROMPT_LIMIT):
                print('Speak!')
                guess = record_text()
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")

            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                break

            # show the user the transcription
            print("You said: {}".format(guess["transcription"]))

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = NUM_Tries - 1 > 0

            # determine if the user has won the game
            if guess_is_correct:
                print("Correct! Let's move on to the next one!")
                break
            elif user_has_more_attempts:
                print("Close! Let's try again.")
            
            else:
                print("Not quite right, let's try again!".format(word))
                break
        # If the last word was correctly guessed, print the completion message
        if guess_is_correct and word == LVL1[-1]:
            print("Congratulations! You've completed level 3. Great Job.!!")
            cont=input("Do you want to try level medium? Type Y for yes N for no: ")
            if cont== 'Y' or 'y':
                break
            else:
                exit()
            
    

