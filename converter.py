import pafy
import os
import json

SERVER_URL = 'http://52.232.85.160/'
EXT = ".m4a"

def download_audio(video_id):
    if not video_id:
        return {"status": False, "error": "Video id not specified"}
    song = get_song(video_id)

    if song:
        return song

    try:
        video = pafy.new(str(video_id))
    except ValueError as e:
        print(e)
        return {"status": False, "error": "Invalid video id specified"}

    streams = video.audiostreams
    if len(streams) > 0:
        filename = video.getbestaudio(preftype=EXT[1:]).download(filepath="./dist", quiet=True)
        os.rename(filename, './dist/' + video_id + EXT)
        song_url = SERVER_URL + video_id
        song = add_song(video_id, get_sec(video.duration), song_url)
        return song
    return {"status": False, "error": "No audio streams found"}


def add_song(id, duration, url):
    with open('songs.json', 'a') as file:
        try:
          songs = json.loads(file)
        except:
          songs = {}
        songs[id] = {"duration": duration, "url": url}
        print(songs)
        json.dump(songs, file)
        return songs[id]


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_song(id):
    with open('songs.json', 'a') as file:
        try:
            songs = json.load(file)
            print(songs)
            return songs[id]
        except:
            return None
