import tkinter as tk
from tkinter import messagebox, filedialog
import speech_recognition as sr
import threading


class ASRTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech-to-Text ASR Tool")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.recognizer = sr.Recognizer()

        # Title
        title = tk.Label(
            root,
            text="Speech-to-Text ASR Tool",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            root,
            text="Automatic Speech Recognition using Python",
            font=("Arial", 12)
        )
        subtitle.pack()

        # Status
        self.status = tk.Label(
            root,
            text="Status: Ready",
            font=("Arial", 11)
        )
        self.status.pack(pady=15)

        # Text box
        self.text_box = tk.Text(
            root,
            height=12,
            width=75,
            font=("Arial", 12),
            wrap=tk.WORD
        )
        self.text_box.pack(padx=20, pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        self.start_button = tk.Button(
            button_frame,
            text="🎤 Start Listening",
            font=("Arial", 12, "bold"),
            command=self.start_recording,
            padx=15,
            pady=8
        )
        self.start_button.grid(row=0, column=0, padx=8)

        clear_button = tk.Button(
            button_frame,
            text="🗑 Clear",
            font=("Arial", 12),
            command=self.clear_text,
            padx=15,
            pady=8
        )
        clear_button.grid(row=0, column=1, padx=8)

        save_button = tk.Button(
            button_frame,
            text="💾 Save Text",
            font=("Arial", 12),
            command=self.save_text,
            padx=15,
            pady=8
        )
        save_button.grid(row=0, column=2, padx=8)

    def start_recording(self):
        # Run recording in a separate thread
        thread = threading.Thread(target=self.recognize_speech)
        thread.daemon = True
        thread.start()

    def recognize_speech(self):
        try:
            self.status.config(text="Status: Listening... 🎤")
            self.start_button.config(state=tk.DISABLED)

            with sr.Microphone() as source:

                # Adjust microphone for background noise
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                self.status.config(text="Status: Speak now...")

                audio = self.recognizer.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=15
                )

            self.status.config(text="Status: Processing speech...")

            # Convert speech to text
            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            self.text_box.insert(
                tk.END,
                text + "\n"
            )

            self.status.config(
                text="Status: Speech recognized successfully ✅"
            )

        except sr.WaitTimeoutError:
            self.status.config(
                text="Status: No speech detected"
            )
            messagebox.showwarning(
                "Timeout",
                "No speech was detected. Please try again."
            )

        except sr.UnknownValueError:
            self.status.config(
                text="Status: Could not understand speech"
            )
            messagebox.showwarning(
                "Recognition Error",
                "Sorry, I could not understand the speech."
            )

        except sr.RequestError:
            self.status.config(
                text="Status: Internet connection error"
            )
            messagebox.showerror(
                "Connection Error",
                "Could not connect to the speech recognition service."
            )

        except Exception as e:
            self.status.config(
                text="Status: Error occurred"
            )
            messagebox.showerror(
                "Error",
                str(e)
            )

        finally:
            self.start_button.config(state=tk.NORMAL)

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)
        self.status.config(text="Status: Ready")

    def save_text(self):
        text = self.text_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning(
                "Empty Text",
                "There is no recognized text to save."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)

            messagebox.showinfo(
                "Saved",
                "Transcription saved successfully!"
            )


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ASRTool(root)
    root.mainloop()