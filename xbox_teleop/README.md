# XBox Teleop

## Setup

Install the necessary packages with:
````bash
# On Ubunutu
$ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
````

## Usage

Launch the Xbox USB Gamepad Userspace Driver with:
```bash
$ sudo xboxdrv --silent
# If you get a LIBUSB_ERROR_BUSY error, fix it with:
# sudo rmmod xpad
```

Run *xbox_remapper.launch* with: 
```bash
$ roslaunch topic_remapper xbox_teleop.launch
```

This launches both the xbox_teleop node and the teleoperation package for the XBox controller.
