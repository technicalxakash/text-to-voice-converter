from gtts import gTTS
import os

# Input text to convert to speech
text = "Pushpa ante flower anukuntiva, fireu kadu wild fireu"

# Set the language for the TTS (e.g., 'en' for English)
language = 'en'

# Generate the TTS audio
tts = gTTS(text=text, lang=language, slow=False)

# Save the audio file
audio_file = "output.mp3"
tts.save(audio_file)

# Play the audio file (works on most systems)
os.system(f"start {audio_file}")  # For Windows
# os.system(f"open {audio_file}")  # For macOS
# os.system(f"xdg-open {audio_file}")  # For Linux

print(f"Audio saved as {audio_file}.")
