import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException

'''
class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.captions_file_exists(url):
                continue
            source = YouTube(url)
            caption = source.captions.get_by_language_code('a.en')
            caption_convert_to_srt = (caption.generate_srt_captions())
            text_file = open(utils.get_caption_path(url), "w", encoding="utf-8")
            text_file.write(caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took',end-start,'seconds')
'''
class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()

        for url in data:
            try:
                source = YouTube(url)
                caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = caption.generate_srt_captions()
                print(en_caption_convert_to_srt)

                text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
            except (KeyError, AttributeError):
                print("An Error for :", url)
                continue
        end = time.time()
        print('took', end-start, 'seconds')

