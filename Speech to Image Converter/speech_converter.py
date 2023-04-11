# For speech recognition
# pip install SpeechRecognition
# For accessing mic
# pip install PyAudio

import speech_recognition as sr

class SpeechConverter:

    @staticmethod
    def get_prompt_from_speech():
        """
        Prompts a meat robot for a speech description and 
        converts that speech into text
        """
        r = sr.Recognizer()
        audio_text = ""

        # listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            print("[Talk, hooman]")
            audio = r.listen(source)
            print("[Talking time over, thanks hooman]")

            # recognize_google() method will throw a request error if the API is unreachable
            try:
                # using google speech recognition
                audio_text = r.recognize_google(audio)
            except:
                print("[Sorry, I did not get that?! Open ya mouf!]")
        print("Text:  " + audio_text)
        return audio_text



# prompt = SpeechConverter.get_prompt_from_speech()
# prompt = "The Golden Girls on crack"
# print("Prompt: " + prompt)