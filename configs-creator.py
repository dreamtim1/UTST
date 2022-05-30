import sys

with open('video-formats-list.txt') as inputs:
    video_formats_list = [el.strip() for el in inputs.readlines()]

with open('.gitignore', 'a') as outputs:
    for format in video_formats_list:
        ignore = f'\n*.{format}'
        outputs.write(ignore)
