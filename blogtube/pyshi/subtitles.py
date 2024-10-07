from pydub import AudioSegment
import nltk
import math


def seconds_to_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

def create_srt(text_file, audio_file, output_srt, words_per_segment=10):
    audio = AudioSegment.from_file(audio_file)
    audio_duration = len(audio) / 1000  
    with open(text_file, 'r') as f:
        text = f.read()

    sentences = nltk.sent_tokenize(text)

    total_words = sum(len(sentence.split()) for sentence in sentences)
    words_duration = audio_duration / total_words  
    with open(output_srt, 'w') as srt_file:
        current_time = 0.0
        index = 1
        for sentence in sentences:
            words = sentence.split()
            num_words = len(words)
            segment_duration = num_words * words_duration

            start_time = current_time
            end_time = current_time + segment_duration

            srt_file.write(f"{index}\n")
            srt_file.write(f"{seconds_to_srt_time(start_time)} --> {seconds_to_srt_time(end_time)}\n")
            srt_file.write(f"{sentence}\n\n")

            current_time = end_time
            index += 1

    print(f"SRT file '{output_srt}' created successfully.")

create_srt('short.txt', 'output.wav', 'output.srt', words_per_segment=10)
