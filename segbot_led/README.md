## Segbot LED Package

This ROS package contains code for controlling Pololu WS2812B-Based LED Strips.

### Configuring Metro Mini Microcontroller

* Install recent Arduino IDE if not already installed on machine.

* Add pololu-led-strip-arduino library to the Arduino IDE.

* Set Board Manager to Arduino UNO

* Open led_serial_driver.ino and upload to device.

### Configuring udev Rules

Retrieve the attributes of the microcontroller to create the proper udev rule for the specific device. 

* You will need to monitor udev events to determine the serial port name for the device. Execute the command: 

```
udevadm monitor
```

* Plug in the device and annotate what /dev/ name it was assigned.

* Execute the command below and replace the question marks with the name given to your device.

```
udevadm info --attribute-walk --name=/dev/?????
```

* Retrive the follwing attribute values and replace the values in 99-metromini.rules.

	* ATTRS{idVendor}
	* ATTRS{idProduct}
	* ATTRS{serial}

### Setting Up Segbot LED Configuration

To utilize the Segbot LED package you must configure the led segments of the robot in the launch file.
The package led animations are configured for use on the Segbots part of the BWI Project, but could 
be modified for other robot designs.

LED Strips must be set up in a similar style as shown below.

<img src="/segbot_led/images/front.JPG" alt="Front" width="300">
<img src="/segbot_led/images/back.JPG" alt="Back" width="300">
<img src="/segbot_led/images/left.JPG" alt="Left" width="300">
<img src="/segbot_led/images/right.JPG" alt="Right" width="300">

