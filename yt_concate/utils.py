import os
from yt_concate.setting import CAPTION_DIR
from yt_concate.setting import DOWNLOADS_DIR
from yt_concate.setting import VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0
    @staticmethod
    def get_video_id(url):
        return url.split('watch?v=')[1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id(url) + ".txt")

    def captions_file_exists(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
