# pepper-demo
## Daily Use
Here are gathered key points to interact with Pepper:
- [Turning Pepper on](./aldeb-doc-2.5.11.14/family/pepper_user_guide/turn_on_pep.html)
- [Interacting with Pepper](./aldeb-doc-2.5.11.14/family/pepper_user_guide/interacting_pep.html)
- [Launching / exiting an Activity](./aldeb-doc-2.5.11.14/family/pepper_user_guide/activity_pep.html)
- [Putting Pepper to sleep](./aldeb-doc-2.5.11.14/family/pepper_user_guide/sleep_pep.html)
- [Switching Autonomous life on and off](./aldeb-doc-2.5.11.14/family/pepper_user_guide/freeze_pep.html)
- [Turning Pepper off](./aldeb-doc-2.5.11.14/family/pepper_user_guide/turn_off_pep.html)
- [Requesting technical information](./aldeb-doc-2.5.11.14/family/pepper_user_guide/request_pep.html)
- [Charging the battery](./aldeb-doc-2.5.11.14/family/pepper_user_guide/battery-charging_pep.html)

For more information, please visit [here](./aldeb-doc-2.5.11.14/family/pepper_user_guide/interacting.html).

## Run Demos
1. Turn pepper on
2. ...

TBD



## For developers
### Pepper Device Info
- IP Address: 
- MAC Address:

TBD 

### Choregraphe-suite-2.5.10.7
Download [choregraphe-suite-2.5.10.7-linux64](https://drive.google.com/file/d/16h7xRx261XC9tK4yoNY1_Avj20tYhjY5/view?usp=sharing)

If you face the following error on installing Choregraphe, 

```
/opt/Softbank Robotics/Choregraphe Suite 2.5/bin/../lib/../lib/../lib/libz.so.1: 
version `ZLIB_1.2.9' not found (required by /usr/lib/x86_64-linux-gnu/libpng16.so.16)
```

run below

```
cd "/opt/Softbank Robotics/Choregraphe Suite 2.5/lib/"
sudo mv libz.so.1 libz.so.1.old
sudo ln -s /lib/x86_64-linux-gnu/libz.so.1
```


### Pynaoqi-2.5.7.1
Download [pynaoqi-python2.7-2.5.7.1-linux64](https://drive.google.com/file/d/1ZWqaU_Nl8o9mUi5FKYq-1XmsfRwDUgX3/view?usp=drive_link)



