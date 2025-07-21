from fastapi import FastAPI, Query
from services.youtube import download_video

app = FastAPI()

@app.get("/download")
async def download(video_url: str = Query(...)):
    return download_video(video_url)
