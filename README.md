# Speech-to-Text ASR Tool

## 1. Project Overview

The Speech-to-Text ASR Tool is a Python-based Automatic Speech Recognition (ASR) application that converts human speech into written text.

The application captures audio through the computer's microphone, processes the speech using a speech recognition service, and displays the recognized text in a graphical user interface.

## 2. Objective

The main objective of this project is to implement an Automatic Speech Recognition system that can:

* Capture speech through a microphone
* Convert spoken words into text
* Display the recognized text
* Clear the generated text
* Save the transcription as a text file

## 3. Features

* 🎤 Real-time microphone input
* 📝 Speech-to-text conversion
* 🖥️ Simple graphical user interface
* 🗑️ Clear transcription
* 💾 Save recognized text
* 🇮🇳 English (India) speech recognition
* ⚠️ Error handling for unclear speech and connection problems

## 4. Technologies Used

| Technology                | Purpose                      |
| ------------------------- | ---------------------------- |
| Python                    | Main programming language    |
| SpeechRecognition         | Speech recognition interface |
| PyAudio                   | Microphone/audio input       |
| Tkinter                   | Graphical user interface     |
| Google Speech Recognition | Speech-to-text processing    |
| Git                       | Version control              |
| GitHub                    | Project hosting              |

## 5. How ASR Works

The application follows these steps:

```text
User Speech
     ↓
Microphone
     ↓
Audio Capture
     ↓
Speech Recognition
     ↓
Speech-to-Text Processing
     ↓
Recognized Text
     ↓
Display / Save Text
```

## 6. Requirements

* Windows/Linux/macOS
* Python 3.x
* Working microphone
* Internet connection
* Required Python libraries

## 7. Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Speech-to-Text-ASR
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 8. Running the Application

Run:

```bash
python app.py
```

The ASR application window will open.

Click **Start Listening**, speak clearly into the microphone, and wait for the recognized text to appear.

## 9. Project Structure

```text
Speech-to-Text-ASR/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

### app.py

Contains the complete Python implementation of the ASR application and GUI.

### requirements.txt

Contains the Python dependencies required to run the project.

### README.md

Contains project documentation and instructions.

### screenshots/

Contains screenshots demonstrating the working application.

## 10. Testing

The application was tested using different spoken sentences through the computer microphone.

Test cases included:

1. Speaking a simple sentence.
2. Speaking multiple sentences.
3. Clearing recognized text.
4. Saving the transcription.
5. Handling unclear or unavailable speech.
6. Handling internet connection errors.

## 11. Advantages

* Easy to use
* Simple graphical interface
* Converts speech into text quickly
* Can save the generated transcription
* Useful for basic voice-based applications
* Easy to understand and modify

## 12. Limitations

* Internet connection is required for the speech recognition service.
* Recognition accuracy can be affected by background noise.
* Different accents may produce different recognition results.
* Microphone quality can affect the output.

## 13. Future Enhancements

Future versions can include:

* Offline speech recognition
* Support for multiple languages
* Continuous speech recognition
* Voice commands
* Text-to-speech functionality
* Audio recording and playback
* Improved noise reduction
* More advanced speech recognition models

## 14. Conclusion

The Speech-to-Text ASR Tool demonstrates the basic implementation of Automatic Speech Recognition using Python. It captures human speech through a microphone and converts it into readable text, providing a simple example of how ASR technology can be integrated into real-world applications.
