import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3 as ttx

from neuralintents import BasicAssistant

class Assistant:

    def __init__(self):
        self.recognizer=speech_recognition.Recognizer()
        self.speaker=ttx.init()
        self.speaker.setProperty("rate",150)

        self.assistant= BasicAssistant("intents_voice.json")
        self.assistant.training_data

        self.root=tk.Tk()
        self.label=tk.Label(text=":D", font=("Arial", 120, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()


    def create_file(self):
        pass

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio= self.recognizer.listen(mic)
                    text=self.recognizer.recognize_google(audio)
                    text=text.lower()
                    if text=="stop":
                        self.speaker.say("Bye")
                        self.speaker.runAndWait()
                        self.speaker.stop()
                        self.root.destroy()
                        sys.exit()
                    else:
                        if text is not None:
                            self.speaker.say('responses')
                            self.speaker.runAndWait()
                        self.label.config(fg="black")
            except:
                self.label.config(fg="black")
                continue
         
Assistant()