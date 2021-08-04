# Hindi Speech to Text

This script will help you type in hindi just by speaking.

## Installation

1. First install "Kruti Dev 010 Regular" font (already provided) if you don't have it.  
2. Install all the requirements by using "requirements.txt".

```bash
pip install -r requirements.txt
```
3. Install Pyaudio.

```bash
pip install pipwin
pipwin install pyaudio
```
4. Thats it! You are good to go.

## Usage

```python
python htext.py
```

## Notes

This program is tested on python version 3.9.6 and will work on all version of python 3. The text output will be generated in same location of htext.py named as "output.txt". Ignore wierd text in your terminal because terminal can't write hindi alphabets.

## Libraries used

```python
SpeechRecognition
PyAudio
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
