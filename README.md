# MyVoiceAssistant-Prototype
This repository contains a Desktop Voice Assistant built in Python, created and managed by Aalhad Ramteke.

🎙️ Desktop Voice Assistant
A feature-rich virtual assistant built using Python. This project uses speech recognition to understand voice commands and text-to-speech to respond. 
It can perform various tasks such as opening system applications, browsing the web, providing information, and controlling system settings.

✨ Features
Voice Interaction: Uses the Google Speech Recognition API to listen to commands and the pyttsx3 library to speak responses.
Greeting System: Dynamically greets the user ("Aalhad") based on the time of day (Morning, Afternoon, Evening).
Web Browsing: Quickly opens popular websites like YouTube, Google, and Stack Overflow.
System Control: Opens native Windows applications like Notepad, Command Prompt, and Calculator.
Information Retrieval:
Fetches summaries from Wikipedia.
Tells the current time and date.
Tells random programming jokes.

Media & Utilities:
Plays music from a local directory.
Takes screenshots and saves them with timestamps.
System Power: Can schedule a system shutdown or cancel it via voice command.

🛠️ Prerequisites
Python 3.x installed on your machine.
Microphone for voice input.
Speakers/Headphones for voice output.
Windows OS (The code utilizes Windows-specific system paths and commands like sapi5, notepad.exe, and shutdown /s).

📦 Installation
Clone the repository (or download the script).

🚀 Usage

Use the following voice commands:

"Open YouTube"	Opens YouTube in your default browser.
"Open Google"	Opens Google.
"Open Stack Overflow"	Opens Stack Overflow.
"Open Notepad"	Opens Notepad.
"Open Command Prompt" / "Open CMD"	Opens CMD.
"Open Calculator"	Opens the Calculator.
"Play Music"	Plays the first song from your defined Music folder.
"The time"	Tells the current time.
"The date"	Tells today's date.
"Tell me a joke" / "Joke"	Tells a random programming joke.
"Explain [topic]"	Searches Wikipedia for a summary of the topic.
"Screenshot"	Takes a screenshot and saves it in the script directory.
"Shutdown"	Initiates a 10-second shutdown timer.
"Cancel shutdown"	Cancels the active shutdown timer.
"Exit" / "Quit" / "Stop"	Closes the assistant.

👨‍💻 Credits
Created and developed by Aalhad M. Ramteke.

📝 License
This project is open-source and available for educational purposes.
