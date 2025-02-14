# controlTower

This is a teleoperation control package that converts iBUS radio signals to ROS2 `geometry_msgs/Twist` messages for controlling robots. 

## Hardware
- Uses Turnigy TGY-i6S transmitter for control.
- Uses Turnigy TGY-iA6B receiver for iBUS signals.
- Runs on Raspberry Pi 5 for processing.
- Primary UART: Rx = pin 28, Tx = pin 27 on /dev/ttyAMA1
- Test UART: Rx = pin 15, Tx = pin 14 on /dev/ttyAMA0
- Uses Turnigy TGY-i6S transmitter for control.
- Uses Turnigy TGY-iA6B receiver for iBUS signals.
- Runs on Raspberry Pi 5 for processing.
- Uses Turnigy TGY-iA6B receiver for iBUS signals.
- Runs on Raspberry Pi 5 for processing.

## Features
- Reads iBUS signals from RC transmitters.
- Maps RC channels to `linear.x`, `linear.y`, and other ROS2 control fields.
- Publishes `Twist` messages over ROS2 for seamless robot teleoperation.

## Usage
- Install dependencies from `requirements.txt`.
- Run `ibus_decoder.py` to start reading RC signals.
- Integrate with the `controlTower_ros2` package to publish ROS2 commands.

## ROS2 Integration
- Uses `rclpy` and `geometry_msgs`.
- Easily extendable for additional ROS2 features.
