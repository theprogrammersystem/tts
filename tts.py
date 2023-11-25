import pyttsx3
import os
from datetime import datetime
from IPython.display import Audio, display, FileLink

def text_to_speech(text, voice_gender='male', output_directory='output', rate=0.5):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Generate a filename using the current date and time
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"{current_time}.mp3"
    output_path = os.path.join(output_directory, output_file)

    engine = pyttsx3.init()

    # Set the voice gender
    voices = engine.getProperty('voices')
    if voice_gender == 'male':
        engine.setProperty('voice', voices[0].id)  # Assuming the first voice is male
    elif voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)  # Assuming the second voice is female

    # Set the rate of speech
    engine.setProperty('rate', engine.getProperty('rate') * rate)

    # Convert text to speech
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    # Display the audio preview
    display(Audio(output_path, autoplay=True))

    # Provide a link for downloading the audio file
    display(FileLink(output_path))

if __name__ == "__main__":
    while True:
        user_text = input("Enter the text you want to convert to speech (or type 'exit' to end): ")
        
        if user_text.lower() == 'exit':
            break
        
        user_gender = input("Enter the gender of the voice (male/female): ")
        speech_rate = float(input("Enter the speech rate (e.g., 0.5 for slower, 1 for normal): "))
        
        text_to_speech(user_text, user_gender, rate=speech_rate)
