import os
import sys
import pyfiglet
from termcolor import colored
import yt_dlp

# Title banner
ascii_banner = pyfiglet.figlet_format("Manan Downloader")
print(colored(ascii_banner, "cyan"))

# Password check
password = input(colored("Enter password: ", "yellow")).strip()
if password != "manan":
    print(colored("❌ Incorrect password. Access denied!", "red"))
    sys.exit()

# Ask for profile link
profile_url = input(colored("Enter profile link: ", "green")).strip()

if not profile_url:
    print(colored("❌ No link provided. Exiting...", "red"))
    sys.exit()

# Download settings
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'best',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([profile_url])
    print(colored("✅ Download completed successfully!", "cyan"))
except Exception as e:
    print(colored(f"❌ Error: {str(e)}", "red"))
