from TTS.api import TTS

# Initialize TTS with your chosen model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)
tts.to("cpu")  # Ensure the model is on the correct device

# Path to the input file containing text
input_file_path = "short.txt"
# Path to the output file where the audio will be saved
output_file_path = "output.wav"

# Read text from the input file
with open(input_file_path, "r") as file:
    text = file.read()

# Convert text to speech and save to the output file
tts.tts_to_file(text=text, file_path=output_file_path)

print(f"Speech has been saved to {output_file_path}")
