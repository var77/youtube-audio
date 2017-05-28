import pafy
import os


SERVER_URL = 'http://52.232.85.160/'
EXT = ".m4a"

def download_audio(video_id):
    if not video_id:
        return {"status": False, "error": "Video id not specified"}

    if os.path.exists('./dist/' + video_id + EXT):
        return {"status": True, "url": SERVER_URL + video_id}

    try:
        video = pafy.new(str(video_id))
    except ValueError as e:
        print(e)
        return {"status": False, "error": "Invalid video id specified"}

    streams = video.audiostreams
    if len(streams) > 0:
        filename = video.getbestaudio(preftype=EXT[1:]).download(filepath="./dist", quiet=True)
        os.rename(filename, './dist/' + video_id + EXT)
        return {"status": True, "url": SERVER_URL + video_id}
    return {"status": False, "error": "No audio streams found"}
