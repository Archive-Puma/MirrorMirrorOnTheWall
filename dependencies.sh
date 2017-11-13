if [ $UID != '0' ]; then
  echo "You must be root!"
else

  # OPENCV
  apt-get install -y --force-yes build-essential
  apt-get install -y --force-yes cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

  apt-get install -y --force-yes python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
  apt-get install -y --force-yes python-matplotlib
  apt-get install -y --force-yes python-opencv

  apt-get autoremove -y
  apt-get clean -y
fi
