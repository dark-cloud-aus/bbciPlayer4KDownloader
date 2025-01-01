# 2025 BBCiPLAYER 4K DOWNLOADER by David Gilmore


import yt_dlp
import sys
import os

# Command for terminal : python3 bbc_downloader.py "INSERT HYPERLINK HERE"

def download_bbc_video(url):
    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download best quality
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output template with downloads folder
        'geo_verification_proxy': None,  # Use this if you're using a VPN
        'verbose': True,
        'progress': True,
        'fragment_retries': 10,          # Retry failed fragments up to 10 times
        'retries': 10,                   # Retry the download up to 10 times
        'continuedl': True,              # Continue partial downloads
        'hls_prefer_native': True,       # Use native HLS implementation
        'hls_use_mpegts': True,         # Use MPEG-TS format for HLS
        'nocheckcertificate': True       # Skip SSL verification
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bbc_downloader.py <BBC iPlayer URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    if not url.startswith("https://www.bbc.co.uk/iplayer/"):
        print("Please provide a valid BBC iPlayer URL")
        sys.exit(1)
        
    download_bbc_video(url)
