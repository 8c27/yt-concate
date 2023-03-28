from yt_concate.pipeline.steps.get_video_list_from_channel import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight

ChannelId = "UCKSVUHI9rbbkXhvAXK-2uxA"  # channel ID


def main():
    inputs = {
        "channel_id": ChannelId
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]



    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs,utils)


if __name__ == "__main__":
    main()
