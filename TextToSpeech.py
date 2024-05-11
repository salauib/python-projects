import pyttsx3
def main():
    engine = pyttsx3.init()
    engine.say(input("Enter a word or sentence to speech?: \n"))
    engine.runAndWait()
finalAnswer = main()