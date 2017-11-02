<img src="https://cdn.rawgit.com/CosasDePuma/MirrorMirrorOnTheWall/7a013b72/.img/magicmirror%20(by%20elicoronel16).png" align="right" width="300">

# Mirror, Mirror on the Wall ...
[![Python Version](https://img.shields.io/badge/python-2.7.13-yellow.svg?style=flat)](https://www.python.org/downloads/release/python-2713/) ![Made with Love](https://img.shields.io/badge/made%20with-<3-red.svg?style=flat) [![License](https://img.shields.io/github/license/CosasDePuma/MirrorMirrorOnTheWall.svg)](https://github.com/CosasDePuma/MirrorMirrorOnTheWall/blob/master/LICENSE)

:vhs: Clone me!
----
Clone or download the Github project
```bash
git clone https://github.com/cosasdepuma/mirrormirrorinthewall.git
```

:memo: Installation
----
Install the dependencies using the script:

```sh
sh setup/requirements.txt
bash setup/requirements.txt
```

If error `You must be root!` appears, try with *sudo*:

```bash
sudo sh setup/requirements.txt
sudo bash setup/requirements.txt
```

:camera: Create the Database
----

Make a new folder inside *data/* called *photos*:

```bash
mkdir -vp data/photos
```

Run the *createdb* python script:
```python
python createdb.py
```

Press `R` to record a new emotion or to stop recording.
Press `Q` or `Ctrl+C` to exit the program.

:chart_with_upwards_trend: Train the Recognizer
----
Make a new folder inside *data/* called *recognizer*:

```bash
mkdir -vp data/recognizer
```

Run the *trainer* python script:
```python
python trainer.py
```

:see_no_evil: Run the program!
----
Run the *recognizer* python script:
```python
python recognizer.py
```

Press `Q` or `Ctrl+C` to exit the program.

Issues
----
If **python <script>.py** does not work, try running:

```python
python2 <script>.py
```

Please contact with [Kike Puma](https://linkedin.com/in/kikepuma) if you need more information.
