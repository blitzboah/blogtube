#!/bin/bash

read -p "enter the link of the blog: " link
read -p "enter the title of video: " title
read -p "1. full video or 2. short video?: " ch

link_file="./links.txt"
intro_file="pyshi/intro.txt"

echo "$link" >"$link_file"
echo "$title" >"$intro_file"

echo "scraping blog"
mvn spring-boot:run
echo -en '\n'

cd pyshi

if [ "$ch" -eq 1 ]; then
  cp ../content.txt ./short
  python long-tts.py
  ffmpeg -i long_background.mp4 -i output.wav -vf "scale=1920:1080" -c:v h264_nvenc -preset fast -c:a aac -map 0:v:0 -map 1:a:0 -shortest -y output_full.mp4
elif [ "$ch" -eq 2 ]; then
  python summarization.py
  python tts.py
  python subtitles.py
  ffmpeg -i short_background.mp4 -i output.wav -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920,subtitles=output.srt:force_style='Alignment=2'" \
    -c:v h264_nvenc -b:v 6000k -cq 19 -preset hq -c:a aac -b:a 192k -map 0:v:0 -map 1:a:0 -shortest -y output_short.mp4

else
  echo "invalid choice"
  exit
fi

echo "owarida!"
