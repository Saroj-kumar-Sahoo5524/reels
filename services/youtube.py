import yt_dlp
import os

def download_video(video_url: str):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    cookie_file = os.path.join(base_dir, 'cookies.txt')

    ydl_opts = {
        'cookiefile': cookie_file,
        'outtmpl': os.path.join(base_dir, 'videos', '%(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            return {
                "status": "success",
                "title": info.get("title"),
                "filename": ydl.prepare_filename(info)
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}
