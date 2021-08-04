import speech_recognition as sr

def takeCommandHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='hi-In')

            print(query)

            # Writing it in a text file
            with open('output.txt', 'a', encoding='utf8') as file:
                file.write(query + '\n')
                file.close()

        # handling the exception
        except Exception as e:
            print(e)
            print("Phir se boliye")
            return "None"
        return query


while True:
    takeCommandHindi()
