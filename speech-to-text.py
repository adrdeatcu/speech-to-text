import customtkinter as ctk 
import speech_recognition as sr
import threading



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Speech to Text")
        self.root.geometry("600x400")

        self.label = ctk.CTkLabel(self.root, text="Speech to Text", font=ctk.CTkFont(size=20))
        self.label.pack(pady=20)

        self.btn = ctk.CTkButton(self.root, text="Record", command=self.recognize_speech)
        self.btn.pack(pady=10)

        self.result = ctk.CTkTextbox(self.root, width=400, height=200)
        self.result.pack(pady=20)

    def recognize_speech(self):
        def run():
            r = sr.Recognizer() #initializam recunoasterea vocala 
            mic = sr.Microphone() #initializam microfonul
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='ro-RO')
                self.result.insert("end", text + "\n")
            except:
                self.result.insert("end", "Repeat the sentece\n")
        threading.Thread(target=run).start()  # Evită blocarea GUI

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App() #crearea unei instante a clasei App
    app.run() #pornirea aplicatiei