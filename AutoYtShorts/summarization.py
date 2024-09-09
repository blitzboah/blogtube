from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

# Read text from a file
with open('content.txt', 'r') as file:
    title = file.readline().strip()
    content = file.read()

# Summarize title and content
summarized_title = summarize_text(title, num_sentences=1)
summarized_content = summarize_text(content)

# Print summaries
print("Summarized Title:")
print(summarized_title)
print("\nSummarized Content:")
print(summarized_content)

