from gtts import gTTS
import argparse

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f'Audio saved as {filename}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text-to-Speech Converter')
    parser.add_argument('text', help='The text to convert to speech')
    parser.add_argument('filename', help='Output filename (without extension)')
    args = parser.parse_args()

    text_to_speech(args.text, args.filename + '.wav')
