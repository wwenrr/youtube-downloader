import subprocess
import threading
import re
from src.exception.download_opt_exception import DownloadOptionException

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

def download_video(video_url:str, height:int, log_callback, option:str = "video"):
    def run_command(command:list):
        process = subprocess.Popen(command, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.STDOUT,startupinfo=startupinfo, 
                                   creationflags=subprocess.CREATE_NO_WINDOW,
                                   text=True, 
                                   bufsize=1
                                )
        global text

        for line in process.stdout:
            log_callback(line.strip())

        process.wait()
        return process
    
    def download_video_only():
        global video

        command = [
            "resources/yt-dlp.exe",
            "-N", "5",
            "-f", f"bestvideo[height<={height}]+bestaudio",
            "--merge-output-format", "mp4",
            "--ffmpeg-location", "resources/ffmpeg.exe",
            "-o", "video/%(title)s/%(title)s.%(ext)s", 
            video_url
        ]
        return run_command(command)
    
    def download_audio(): 
        global audio

        command = [
            "resources/yt-dlp.exe",
            "-f", "bestaudio",  
            "--extract-audio",  
            "--audio-format", "mp3",  
            "--audio-quality", "0",  
            "--ffmpeg-location", "resources/ffmpeg.exe",
            "-o", "video/%(title)s/audio/%(title)s.%(ext)s",  
            video_url
        ]
        return run_command(command)

    if option == "video":
        return download_video_only()
    elif option == "audio":
        return download_audio()
    elif option == "both":
        audio_thread = threading.Thread(target=download_audio)  
        audio_thread.start()
        process = download_video_only()  
        audio_thread.join()  
        return process
    else:
        raise DownloadOptionException
