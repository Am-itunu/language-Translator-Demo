# Language Translator App

This simple language translator application is built using the Tkinter GUI toolkit in Python. The app allows users to enter text, choose a target language from a dropdown menu, and then translates the input text into the selected language using the Google Translate API and converts it into speech using gTTS.

## Usage

1. Run the application using the Python script.
2. Enter the text you want to translate into the provided entry field.
3. Choose the target language from the dropdown menu.
4. Click the "Translate" button to see the translated text.
5. The translated text will be displayed below, and the translated speech will be played.

## Features

- User-friendly graphical interface.
- Supports translation to various languages, including Japanese, English, German, Irish, French, Spanish, and Chinese.
- Real-time translation using the Google Translate API.
- Speech synthesis of the translated text using gTTS.

## Installation

Ensure you have Python installed on your system. You can install the required Python packages using the following command:

```bash
pip install tk googletrans==4.0.0-rc1 gtts
```

## Code Structure

- `transLanguage()`: Function to handle the translation process based on the selected language.
- `lang_choice`: List of supported target languages.
- Tkinter GUI elements:
  - `entry_window`: Entry widget for user input.
  - `drpDwn`: StringVar for the dropdown menu to select the target language.
  - `list_lang`: OptionMenu for selecting the target language.
  - `two_label`: Label to display the translated language.
  - `translate_b`: Button to trigger the translation process.

## Requirements

- Python 3.x
- Tkinter library
- Googletrans library (version 4.0.0-rc1)
- gTTS library

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or even pull requests. Your input is highly appreciated!
