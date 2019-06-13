#!/usr/bin/env bash

echo "Installing requirements..."

pip3 install -r requirements.txt --user

echo "Installing audio playback requirements..."

apt install libops0 -y
apt install ffmpeg -y

echo "Setting credentials file up."

mv credentials--blank.py credentials.py

echo 'Done!'

echo 'Add your Discord TOKEN to the credentials file!'
echo 'Then to run execute "python3 main.py"'
