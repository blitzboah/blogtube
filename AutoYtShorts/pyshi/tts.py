from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch", progress_bar=True)
tts.to("cuda")

input_file_path = "short.txt"
output_file_path = "output.wav"

speaker_id = 12

with open(input_file_path, "r") as file:
    text = file.read()

tts.tts_to_file(text=text, file_path=output_file_path)

print(f"Speech has been saved to {output_file_path}")
