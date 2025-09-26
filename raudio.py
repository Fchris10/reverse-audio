import os
import wave
import array
import easygui
from pydub import AudioSegment
from pathlib import Path



def get_audio_reverse(filename):

    if filename is None:
        return
    
    # Open a wave file
    with wave.open(filename, "rb") as f:
        
        # Read the wave file parameters

        width = f.getsampwidth() # Return sample width in bytes 
        nframes = f.getnframes()
        rate = f.getframerate()
        channels = f.getnchannels() # Return number of audio channels (1 for mono, 2 for stereo)
        print(f"Sample width: {width} bytes")
        print(f"Number of frames: {nframes}")
        print(f"Frame rate (sample rate): {rate} frames/second")
        print(f"Number of channels: {channels}")
        print(f"Duration: {nframes / rate} seconds\n\n")


        # Read the frames of wave file as bytes object
        frames = f.readframes(nframes)



    # Convert the byte data to an array of integers

    if width == 1: # 8-bit audio
        audio_data = array.array('b', frames) # 'b' is the type code for char
    elif width == 2: # 16-bit audio
        audio_data = array.array('h', frames) # 'h' is the type code for signed short
    elif width == 4: # 32-bit audio
        audio_data = array.array('i', frames) # 'i' is the type code for int
    elif width == 8: # 64-bit audio
        audio_data = array.array('q', frames) # 'q' is the type code for long long
    else:
        print("Unsupported sample width!")
        return
    

    # Reverse the audio data
    audio_data.reverse()


    # Convert the array of integers back to bytes
    reversed_frames = audio_data.tobytes()


    # Write the reversed audio data to a new wave file and save it in Desktop
    download = Path(Path.home(), "Desktop")
    path_file = os.path.join(download, "reversed_audio.wav")

    with wave.open(path_file, "wb") as out:
        out.setnchannels(channels)
        out.setsampwidth(width)
        out.setframerate(rate)
        out.writeframes(reversed_frames)

    print("Reversed audio is saved to Desktop!")
    return
        



def get_audio():

    file_audio = easygui.fileopenbox(title="Select an audio file")

    if file_audio is None:
        print("\nNo file selected. Exiting the program.")
        return None

    elif file_audio.endswith(".wav"):
        return file_audio
    
    elif file_audio.endswith(".mp3"):
        # Convert .mp3 file to .wav file
        sound = AudioSegment.from_mp3(file_audio)
        sound.export("audio.wav", format="wav")
        return "audio.wav"
    
    else:
        print("Unsupported file format! Please select a .wav or .mp3 file.")
        return None




if __name__ == "__main__":

    print("# WELCOME TO REVERSE AUDIO TOOL #\n\n")
    answer = input("Do you have an audio file to reverse? [Y/N]: ")

    if answer.lower() != 'y':
        print("\nExiting the program.")
        exit()

    filename = get_audio()
    get_audio_reverse(filename)
