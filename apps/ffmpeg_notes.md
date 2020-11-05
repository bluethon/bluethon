# Ffmpeg Notes

## Notes

### 音频前插入空白(audio/insert/silence)

> [SO](https://superuser.com/a/579110/603441)
> [Doc](https://ffmpeg.org/ffmpeg-filters.html#adelay)

    # insert 8s
    ffmpeg -i input.flac -af "adelay=8000" output.mp3
