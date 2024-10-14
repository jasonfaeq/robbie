# LEGO Spike Prime Robot Project

![LEGO Spike Prime Logo](Team%20Logo.png)

This project is for building and programming a LEGO Spike Prime robot that can detect objects, follow lines using a color sensor, and perform simple navigation tasks. The robot uses Python code to achieve the following features:
- Object detection using distance sensors
- Line following using color sensors
- Movement control with motors

## Installation

To run this project, you will need to install the LEGO Spike Prime software and connect your robot with motors and sensors to the correct ports. You'll also need the following components:
- LEGO Spike Prime kit
- Motors connected to ports A and E
- Color sensor connected to port C
- Distance sensor connected to port D

Once your hardware is set up, clone this repository and upload the Python code to your Spike Prime hub.

## Hardware Requirements
LEGO Spike Prime Hub
Motor A and Motor E for movement
Color Sensor C for line detection
Distance Sensor D for obstacle detection

## How it Works
The robot moves forward and detects obstacles using the distance sensor. If an obstacle is detected within 10 cm, it stops.
The color sensor detects red or black lines. It uses this information to follow the correct path.
The robot performs specific maneuvers based on the programmed sequence of movement commands.

## Code Explanation
This project uses the LEGO Spike Prime spike module to control the motors, sensors, and hub. Below is a high-level overview of the main functionality:
Object Detection: The robot stops if it detects an obstacle closer than 10 cm using the distance sensor.
Line Following: The color sensor detects red and black lines to navigate through the course.
Movement Control: The robot moves forward, turns, and adjusts its speed based on sensor inputs.

## Usage
To run this project:
Set up your LEGO Spike Prime kit as described above.
Upload the Python code from this repository to your Spike Prime hub.
Turn on your robot, and it will automatically start performing the programmed tasks.
