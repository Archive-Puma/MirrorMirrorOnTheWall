#! /bin/bash

echo "___  ____                    ___  ____"
echo "|  \/  (_)                   |  \/  (_)"
echo "| .  . |_ _ __ _ __ ___  _ __| .  . |_ _ __ _ __ ___  _ __ "
echo "| |\/| | | '__| '__/ _ \| '__| |\/| | | '__| '__/ _ \| '__|"
echo "| |  | | | |  | | | (_) | |  | |  | | | |  | | | (_) | |"
echo "\_|  |_/_|_|  |_|  \___/|_|  \_|  |_/_|_|  |_|  \___/|_|"
echo "   _____          _        _ _       _   _"
echo "  |_   _|        | |      | | |     | | (_)"
echo "    | | _ __  ___| |_ __ _| | | __ _| |_ _  ___  _ __"
echo "    | || '_ \\/ __| __/ _\` | | |/ _\` | __| |/ _ \\| '_ \\"
echo "   _| || | | \__ \ || (_| | | | (_| | |_| | (_) | | | |"
echo "   \___/_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|"
echo

if [ $UID != '0' ]; then
  echo "You must be root!"
else
  apt-get install -y --force-yes build-essential
  apt-get install -y --force-yes cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
  if [ false ]; then
    echo "NO PYTHON3 VERSION YET"
  else
    apt-get install -y --force-yes python3-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
    apt-get install -y --force-yes python3-opencv
    apt-get install -y --force-yes python3-matplotlib
  fi
  apt-get autoremove -y
  apt-get clean -y
fi
