# Text-to-Speech Converter

This Python script converts text to speech using the Google Text-to-Speech (gTTS) API and saves the output as a WAV file.

## Prerequisites

- Python 3.6 or higher
- `gtts` library (can be installed via `pip install gtts`)

## Usage

1. Clone the repository or download the `text_to_speech.py` file.

2. Install the required dependencies by running the following command:

    ```
    pip install gtts
    ```

3. Open a command prompt or terminal and navigate to the directory where you saved the script.

4. Run the script with the desired text and output filename as command-line arguments. For example:

    ```
    python text_to_speech.py "Hello, how are you?" output_file
    ```

    - Replace `"Hello, how are you?"` with the text you want to convert to speech.
    - Replace `output_file` with the desired filename for the WAV file (without the extension).

5. The script will generate the audio file `output_file.wav` in the same directory.

## Notes

- Make sure you have an internet connection while running the script, as it relies on Google's Text-to-Speech API.
- The language of the generated audio is set to English by default. You can modify the `lang` parameter in the `text_to_speech` function to generate audio in other languages.

## License

This project is licensed under the [MIT License](LICENSE).
