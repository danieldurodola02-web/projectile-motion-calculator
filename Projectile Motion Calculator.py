"""
Projectile Motion Calculator
Author:Durodola Daniel (Aspiring Physicist)
Description:Calculates time of flight,maximum height,range,and positions for a projectile 
"""
import math
g=9.8   # gravity in m/s^2

# User input
initial_velocity=float(input("Enter the initial velocity(m/s):"))
launch_angle=float(input("Enter the launch angle(in degrees):"))

#Converting the launch angle from degrees to radians for Python math functions
launch_angle_rad=math.radians(launch_angle)

#Calculations
time_of_flight=(2*initial_velocity*math.sin(launch_angle_rad))/g
maximum_height=((initial_velocity*math.sin(launch_angle_rad))**2)/(2*g)
Range=((initial_velocity**2)*math.sin(2*launch_angle_rad))/g

#The position at specific time
t=float(input("Enter a time in seconds to get position:"))
x=(initial_velocity*math.cos(launch_angle_rad))*t
y=((initial_velocity*math.sin(launch_angle_rad))*t)-(0.5*g*(t**2))

if t>time_of_flight:
    print('\nThe projectile has already landed at this time.')
    x=Range
    y=0

#Displaying the results
print("\n...PROJECTILE MOTION RESULTS...")
#I would love to use the f-string
print(f"Time of flight:{time_of_flight:.2f} seconds")
print(f"Maximum height:{maximum_height:.2f} meters")
print(f"Range:{Range:.2f} meters")
print(f"position at t={t:.2f}s: x={x:.2f} meters, y={y:.2f} meters")

# my trajectory table of the projectile's positions at different times
print("\nTime (s)| X (m)| Y (m)")
print('-'*25)  #just to draw a line under the heading to make my table look neat
step=0.5   #time interval for each row in the table
current_time=0

# Loop until the projectile reaches the ground
while current_time<=time_of_flight:
    x_position=(initial_velocity*math.cos(launch_angle_rad))*current_time
    y_position=(initial_velocity*math.sin(launch_angle_rad)*current_time)-(0.5*g*(current_time**2))
    if y_position<0:
        y_position=0 #to avoid negative distance after landing
    print(f"{current_time:6.2f} | {x_position:6.2f} | {y_position:6.2f}")
    current_time+=step
print("\nCalculation complete")

# Done




