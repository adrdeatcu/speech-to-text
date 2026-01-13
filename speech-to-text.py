import customtkinter as ctk 
import speech_recognition as sr
import threading
from tkinter import filedialog



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

        self.btn2 = ctk.CTkButton(self.root, text="Save File", command=self.save_file)
        self.btn2.pack(pady=10)

        self.btn_clear = ctk.CTkButton(self.root, text="Clear", command=lambda: self.result.delete("1.0", "end"))
        self.btn_clear.pack(pady=10)

        self.result = ctk.CTkTextbox(self.root, width=500, height=200)
        self.result.pack(pady=20)

    def recognize_speech(self):
        def run():
            r = sr.Recognizer() #initializam recunoasterea vocala 
            r.pause_threshold = 1.5 #pragul de pauza
            mic = sr.Microphone() #initializam microfonul
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=1) #ajustare zgomot de fond
                audio = r.listen(source, phrase_time_limit=10) #ascultare audio cu limita de 10s
            try:
                text = r.recognize_google(audio, language='ro-RO')
                self.result.insert("end", text + "\n")
            except:
                self.result.insert("end", "Repeat the sentece\n")
        threading.Thread(target=run).start()  # Evită blocarea GUI

    def save_file(self):  # se apelază la salvarea fișierului
        content = self.result.get("1.0", "end-1c")  # Extrage textul de la prima linie si prima coloana pana la sfarsit
        if not content.strip(): # Verifică dacă textbox-ul e gol
            return #ieșire dacă nu există text de salvat
        
        #salveaza dialogul si alegere nume si destinatie fisier
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Salvează transcriptul"
        )
        
        if filename:  # Dacă user nu a apăsat Cancel
            try:
                with open(filename, 'w', encoding='utf-8') as f: #creeaza/suprascrie fisierul
                    f.write(content) # Scrie conținutul în fisier
                print(f"Salvat: {filename}")  # Sau adaugă label feedback
            except Exception as e:
                print(f"Eroare: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App() #crearea unei instante a clasei App
    app.run() #pornirea aplicatiei