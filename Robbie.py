# Importing necessary modules
from spike import PrimeHub, MotorPair, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds

# Initialize components
hub = PrimeHub()
motor_pair = MotorPair('A', 'E')  # Motors connected to ports A and E
color_sensor = ColorSensor('C')  # Color sensor in port C
distance_sensor = DistanceSensor('D')  # Distance sensor in port D

# Start the program
motor_pair.set_default_speed(25)
motor_pair.move_tank_for_rotations(75, 'cm')  # Move forward for 75 cm

if distance_sensor.get_distance_cm() < 10:
    motor_pair.set_default_speed(0)  # Stop if an obstacle is closer than 10 cm
else:
    while True:
        if color_sensor.get_color() == 'black':
            break
        if color_sensor.get_color() == 'red':
            motor_pair.start(30)
        else:
            motor_pair.start(30)
        
        if distance_sensor.get_distance_cm() < 10:
            motor_pair.set_default_speed(0)
            break

motor_pair.set_default_speed(20)
motor_pair.move_tank_for_time(1.5, 'seconds')  # Move forward for 1.5 seconds

while True:
    if color_sensor.get_color() == 'black':
        break
    if color_sensor.get_color() == 'red':
        motor_pair.start(30)
    else:
        motor_pair.start(30)
    
    if distance_sensor.get_distance_cm() < 10:
        motor_pair.set_default_speed(0)
        break

motor_pair.set_default_speed(25)
motor_pair.move_tank_for_time(1, 'seconds')  # Move for 1 second

while True:
    if color_sensor.get_color() == 'black':
        break
    if color_sensor.get_color() == 'red':
        motor_pair.start(30)
    else:
        motor_pair.start(30)
    
    if distance_sensor.get_distance_cm() < 10:
        motor_pair.set_default_speed(0)
        break

motor_pair.start(30)
motor_pair.move_tank_for_distance(18, 'cm')  # Move for 18 cm
motor_pair.move_tank_for_distance(22, 'cm')  # Move for 22 cm
wait_for_seconds(1)

motor_pair.move_tank_for_distance(22, 'cm')  # Move for 22 cm
wait_for_seconds(1)

while True:
    motor_pair.move_right_for_rotations(1, 62)  # Move right for 1 rotation
    wait_for_seconds(1)
    motor_pair.move_tank_for_distance(22, 'cm')  # Move for 22 cm
    wait_for_seconds(1)
