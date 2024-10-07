from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch", progress_bar=True)
tts.to("cuda")

input_file_path = "short.txt"
intro_file_path = "intro.txt"
output_file_path = "output.wav"

with open(input_file_path, "r") as file:
    text = file.read()

with open(intro_file_path, "r") as file:
    intro_text = file.read()


final_text = intro_text + " " + text
length_scale = 0.8


tts.tts_to_file(text=final_text, file_path=output_file_path, speaker_wav=None, length_scale=length_scale)

print(f"Speech has been saved to {output_file_path}")
