echo "scraping blog"
mvn spring-boot:run
echo -en '\n'
cd pyshi
echo -en '\n'
echo "summarizing"
python summarization.py
echo -en '\n'
echo "text to speech"
python tts.py
echo -en '\n'
echo "creating srt file for subtitles"
python subtitles.py
echo -en '\n'
echo "creating video"
ffmpeg -i background.mp4 -i output.wav -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920,subtitles=output.srt:force_style='Alignment=2'" -c:v h264_nvenc -preset fast -c:a aac -map 0:v:0 -map 1:a:0 -shortest -y output.mp4
echo "owarida!"
