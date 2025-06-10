# #Step1 a: Setup Text to Speech–TTS–model with gTTS
# from gtts import gTTS
# from pydub import AudioSegment
# import os
# import platform
# import subprocess

# def text_to_speech_with_gtts(input_text, output_filepath_mp3):
#     language = "en"
    
#     # Step 1: Generate MP3 from text
#     tts = gTTS(text=input_text, lang=language, slow=False)
#     tts.save(output_filepath_mp3)
#     return output_filepath_mp3  # 👈 Return the path
#     # Step 2: Convert MP3 to WAV for Windows playback
#     output_filepath_wav = output_filepath_mp3.replace(".mp3", ".wav")
#     sound = AudioSegment.from_mp3(output_filepath_mp3)
#     sound.export(output_filepath_wav, format="wav")

#     # Step 3: Playback based on OS
#     os_name = platform.system()
#     try:
#         if os_name == "Windows":
#             subprocess.run(['powershell', '-c',
#                             f'(New-Object Media.SoundPlayer "{output_filepath_wav}").PlaySync();'])
#         elif os_name == "Darwin":
#             subprocess.run(['afplay', output_filepath_mp3])
#         elif os_name == "Linux":
#             subprocess.run(['mpg123', output_filepath_mp3])  # Or 'aplay' for WAV
#         else:
#             raise OSError("Unsupported operating system.")
#     except Exception as e:
#         print(f"Playback error: {e}")


# input_text="Hi this is Ai with Sumita, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath_mp3="gtts_testing_autoplay.mp3")


from gtts import gTTS
from pydub import AudioSegment
import os
import platform
import subprocess

def text_to_speech_with_gtts(input_text, output_filepath_mp3):
    language = "en"
    
    # Step 1: Generate MP3 from text
    tts = gTTS(text=input_text, lang=language, slow=False)
    tts.save(output_filepath_mp3)
    
    # Step 2: Convert MP3 to WAV for Windows playback
    output_filepath_wav = output_filepath_mp3.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(output_filepath_mp3)
    sound.export(output_filepath_wav, format="wav")

    # Step 3: Playback based on OS
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c',
                            f'(New-Object Media.SoundPlayer "{output_filepath_wav}").PlaySync();'])
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath_mp3])
        elif os_name == "Linux":
            subprocess.run(['mpg123', output_filepath_mp3])
        else:
            raise OSError("Unsupported operating system.")
    except Exception as e:
        print(f"Playback error: {e}")
    
    return output_filepath_mp3  # 👈 Now placed at the end

# Example usage
input_text = "Hi, this is AI with Sumita, autoplay testing!"
text_to_speech_with_gtts(input_text=input_text, output_filepath_mp3="gtts_testing_autoplay.mp3")
