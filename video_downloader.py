import yt_dlp

def download_video(url, output_path):
   
    # Set yt-dlp options
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best[ext=mp4]/best',  # MP4 prioritized, fallback to best available
        'noplaylist': True,  # Do not download playlists
        'merge_output_format': 'mp4',
    }
    
    # Download the video, check for errors
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfully downloaded to: {output_path}")
    except Exception as e:
        print(f"Error downloading video: {e}")

# Insert URL here:
input_link = input("Enter the video URL: ")
download_video(input_link, './%(title)s.%(ext)s')   # Replace './' with desired path if needed