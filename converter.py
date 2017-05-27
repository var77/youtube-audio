import pafy
import os


SERVER_URL = 'http://localhost/'


def download_audio(video_id):
    if not video_id:
        return {"status": False, "error": "Video id not specified"}

    if os.path.exists('./dist/' + video_id + ".ogg"):
        return {"status": True, "url": SERVER_URL + video_id}
    try:
        video = pafy.new(video_id)
    except ValueError:
        return {"status": False, "error": "Invalid video id specified"}

    streams = video.audiostreams
    if len(streams) > 0:
        filename = streams[0].download(filepath="./dist", quiet=True)
        os.rename(filename, './dist/' + video_id + '.ogg')
        return {"status": True, "url": SERVER_URL + video_id}
    return {"status": False, "error": "No audio streams found"}