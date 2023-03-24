from yt_concate.pipeline.steps.get_video_list_from_channel import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline
ChannelId = "UCAuUUnT6oDeKwE6v1NGQxug"  # TED channel ID
def main():
    inputs = {
        "channel_id" : ChannelId
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()



