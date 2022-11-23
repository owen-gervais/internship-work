# Ultrasonic_Sensor_Room_Mapping_Onshape
This code was a demo to generate a low fidelity point cloud of a room using the EV3 Ultrasonic Sensor. 

## How the Code Works:
**main.py** commands the EV3 to rotate in a circle collecting around 200 data points of Ultrasonic data. It does the necessary calculations for positions and the script outputs two arrays of x and y position data.

**FormatFS.py** takes the generated x and y position data and generates a FeatureScript so that the user can create a FeatureStudio in Onshape and get a low fidelity representation of the room. 

## Running this Repo:
I recommend running all of this code from the command line because the main.py is a micropython script, which can be run by
```bash
brickrun -r --pybricks-micropython main.py
```
After that runs you can edit the **FormatFS.py** so that the x and y positions are input
```bash
python3.5 FormatFS.py
```
You can then just copy the result of **FormatFS.py** into an empty FeatureStudio and your room should be visible in you Onshape Part Studio!
