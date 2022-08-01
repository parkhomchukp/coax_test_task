import os
import hashlib

from urllib import request
from moviepy.editor import VideoFileClip

video_link = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'


def video_to_gif(link):
    hash_object = hashlib.md5(link.encode())
    hash_md5 = hash_object.hexdigest()

    video_file_path = f'videos/tiktok_video_{hash_md5}.mp4'
    gif_file_path = f'gifs/tiktok_gif_{hash_md5}.gif'

    if os.path.exists(gif_file_path):
        return f'{os.path.dirname(os.path.abspath(__file__))}/{gif_file_path}'

    request.urlretrieve(link, video_file_path)

    video_clip = VideoFileClip(video_file_path)
    video_clip.write_gif(gif_file_path)
    video_clip.close()

    os.remove(video_file_path)

    return f'{os.path.dirname(os.path.abspath(__file__))}/{gif_file_path}'


if __name__ == '__main__':
    print(video_to_gif(video_link))
