# Getting started
## Install necessarry libraries
```console
sudo apt-get install python3
sudo apt-get install python3-rpi.gpio
sudo apt-get install python3-opencv

```
## Usage
GPIO connection is used here, as soon as the first board (MAIN) receives the command to take a photo, it immediately sends a signal to the second board (SLAVE) via GPIO, so the delay between frames becomes minimal

![alt text](https://github.com/podpolkovnik/sim_cam/blob/main/scheme.png)

---
After connecting, as shown in the picture, you need to run the script **main_board.py** on the first board
```console
python3 main_board.py

```
Then you need to run the script **slave_board.py** on the second board
```console
python3 slave_board.py

```
Then, in the terminal of the first board (MAIN), press the **"Enter"** button to take a photo. Photos are saved to the **"/home/pi"** folder
