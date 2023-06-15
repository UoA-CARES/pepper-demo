# pepper-demo

Read the Pepper Documentation [here](http://doc.aldebaran.com/2-5/home_pepper.html). 

# Important Notice

## Pepper's head 
After usage, please ensure to turn off Pepper completely and position its head in an upright position. Failure to do so may result in damage to Pepper's neck.

<img src='images/pepper_rest_head_down.jpg' height='200'> >>>>>
<img src='images/pepper_rest_head_up.jpg' height='200'>

## Detaching the Charger
Always ensure that Pepper is turned off before disconnecting the charger. It is important not to disconnect the charger while Pepper is powered on.

# Daily Use
Here are convenient links to engage with Pepper quickly:
- [Turning Pepper on](http://doc.aldebaran.com/2-5/family/pepper_user_guide/turn_on_pep.html)
- [Interacting with Pepper](http://doc.aldebaran.com/2-5/family/pepper_user_guide/interacting_pep.html)
- [Launching / exiting an Activity](http://doc.aldebaran.com/2-5/family/pepper_user_guide/activity_pep.html)
- [Putting Pepper to sleep](http://doc.aldebaran.com/2-5/family/pepper_user_guide/sleep_pep.html)
- [Switching Autonomous life on and off](http://doc.aldebaran.com/2-5/family/pepper_user_guide/freeze_pep.html)
- [Turning Pepper off](http://doc.aldebaran.com/2-5/family/pepper_user_guide/turn_off_pep.html)
- [Requesting technical information](http://doc.aldebaran.com/2-5/family/pepper_user_guide/request_pep.html)
- [Charging the battery](http://doc.aldebaran.com/2-5/family/pepper_user_guide/battery-charging_pep.html)

To access further information, kindly visit [this link](http://doc.aldebaran.com/2-5/family/pepper_user_guide/interacting.html).



# Running Demos

Follow these steps to run demos with Pepper:

1. Turn on Pepper.
2. Wait for Pepper to finish the initialization motion.
3. Touch the tablet located on Pepper's chest.
4. Select the desired app to demonstrate.


# For developers
Read the NAOqi documentation [here](http://doc.aldebaran.com/2-5/index_dev_guide.html)

## Pepper Device Info
- Pepper version: 1.8
- IP Address: 172.22.1.21 (SSID: UoA-Device)


## Installing Choregraphe Suite
To install Choregraphe Suite, follow these steps:
1. Download [choregraphe-suite-2.5.10.7-linux64](https://drive.google.com/file/d/16h7xRx261XC9tK4yoNY1_Avj20tYhjY5/view?usp=sharing)
2. Unzip the downloaded file.
3. Run Choregraphe.
```
cd choregraphe-suite-2.5.10.7-linux64
./choregraphe
```

If you encounter the following error while running Choregraphe, 

```
/opt/Softbank Robotics/Choregraphe Suite 2.5/bin/../lib/../lib/../lib/libz.so.1: 
version `ZLIB_1.2.9' not found (required by /usr/lib/x86_64-linux-gnu/libpng16.so.16)
```

please execute the steps below:

```
cd "/opt/Softbank Robotics/Choregraphe Suite 2.5/lib/"
sudo mv libz.so.1 libz.so.1.old
sudo ln -s /lib/x86_64-linux-gnu/libz.so.1
```


## Setup python environment
[Install miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) and create a conda environment. 
```
conda create -n pepper27 python=2.7
conda activate pepper27
```
In order to install pynaoqi, download [pynaoqi-python2.7-2.5.7.1-linux64](https://drive.google.com/file/d/1ZWqaU_Nl8o9mUi5FKYq-1XmsfRwDUgX3/view?usp=drive_link), and unzip it into userhome(/home/username)

Then, add the path to PYTHONPATH to use naoqi in your script.

```
export PYTHONPATH=${PYTHONPATH}:/home/username/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages
```
Or you can add the path in the script. 
```
import sys
sys.path.insert(0, '~/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages')
```

Try to import naoqi.
```
import naoqi
```
If there is no error, it's ready to use the sdk. 

# References
[Aldebaran Docs](http://doc.aldebaran.com/index.html)
