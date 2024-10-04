#!/bin/bash

read -p "enter the link of the blog: " link
read -p "enter the title of video: " title

link_file="../links.txt"
intro_file="intro.txt"

echo "$link" >"$link_file"
echo "$title" >"$intro_file"
