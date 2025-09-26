# Reverse Audio Tool  

Little project that shows in depth how to reverse an audio file using Python’s built-in `wave` library.

---

## Features
1. Select an audio file via a simple **file picker** (`easygui`)  
2. Supports **.wav** and **.mp3** (mp3 files are converted to wav with `pydub`)  
3. Generates a completely **reversed audio file**  
4. Prints detailed audio information:
  -  Sample width  
  -  Number of frames  
  -  Sample rate (frame rate)  
  -  Number of channels  
  -  Duration  

---

## 📦 Requirements
Make sure you have **Python ≥ 3.7** and install the dependencies:  

```bash
pip install pydub easygui
⚠️ Note: To handle .mp3 files with pydub, you need ffmpeg
```
---

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/Fchris10/reverse-audio.git
   cd reverse-audio
   ```
2. Run the script:
  ```
  python raudio.py
  ```
3. Follow the steps in the terminal:

- Confirm if you have an audio file
- Select the file using the file picker
- Wait for the reversed file to be created

---

## 📂Output
The reversed audio file will be saved on your Desktop as:
```
~/Desktop/reversed_audio1.wav
```
---

## Example
```
# WELCOME TO REVERSE AUDIO #

Do you have an audio file to reverse? [Y/N]: y
Sample width: 2 bytes
Number of frames: 210240
Frame rate (sample rate): 44100 frames/second
Number of channels: 2
Duration: 4.77 seconds

Reversed audio is saved to Desktop!

```

