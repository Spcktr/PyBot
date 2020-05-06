#!/usr/bin/env bash

echo "Installing requirements..."

pip3 install -r requirements.txt --user

echo "Installing audio playback requirements..."

apt install libops0 -y
apt install ffmpeg -y

 # credential setup

echo "Creating credentials file ..."
touch credentials.py
echo 'Done!'

# Token setup
read -p "What is your discord token?: " discord_token 
read -p "What is your Weather token?(if none hit return): " weather_token
echo "TOKEN='discord_token'" >> credentials.py
echo "WEATHER='weather_token'" >> credentials.py

echo "Set up is done."

## option for start or exit

PS3='Do you want to start your bot now?(1/2): '
options=("Yes" "No")
select opt in "${options[@]}"
do
    case $opt in
        "Yes")
            echo "Creating Service..."
            cp pybot.service /etc/systemd/system/
            echo "Setting up Service..."
            sudo systemctl daemon-reload
            echo "Bot Started..."
            sudo systemctl start pybot
            ;;
        "No")
            echo "Exiting Setup..."
            break
            ;;
    esac
done    
