from pydub import AudioSegment
import nltk
import math


def seconds_to_srt_time(seconds):
    """Convert seconds to SRT timestamp format: hh:mm:ss,ms"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

def create_srt(text_file, audio_file, output_srt, words_per_segment=10):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)
    audio_duration = len(audio) / 1000  # Convert to seconds

    # Read the text file
    with open(text_file, 'r') as f:
        text = f.read()

    # Split the text into sentences or phrases
    sentences = nltk.sent_tokenize(text)

    # Determine how long each segment should be based on audio length
    total_words = sum(len(sentence.split()) for sentence in sentences)
    words_duration = audio_duration / total_words  # seconds per word

    # Write the SRT file
    with open(output_srt, 'w') as srt_file:
        current_time = 0.0
        index = 1
        for sentence in sentences:
            words = sentence.split()
            num_words = len(words)
            segment_duration = num_words * words_duration

            # Start and end times for this segment
            start_time = current_time
            end_time = current_time + segment_duration

            # Write the subtitle entry
            srt_file.write(f"{index}\n")
            srt_file.write(f"{seconds_to_srt_time(start_time)} --> {seconds_to_srt_time(end_time)}\n")
            srt_file.write(f"{sentence}\n\n")

            # Update the current time and index
            current_time = end_time
            index += 1

    print(f"SRT file '{output_srt}' created successfully.")

# Example usage
create_srt('short.txt', 'output.wav', 'output.srt', words_per_segment=10)

