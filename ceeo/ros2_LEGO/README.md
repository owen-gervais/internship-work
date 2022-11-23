# ROS2 and Gazebo Integration with Onshape-to-Robot Generated sdfs

Utilizing the built LEGO SPIKE Prime Models, I used the Onshape-to-Robot plugin to export Robotic Assemblies to sdf's and imports
and into Gazebo for simulation.

Click here to see a video of this [demo](https://www.youtube.com/watch?v=SlG5cxGIg5A&feature=youtu.be) 

## Installation of ROS2

This the step by step process of installing the required componnents to run this simulation. 
Running on an Ubuntu 20.04 LTS system, you can follow this [ROS2](https://index.ros.org/doc/ros2/Installation/Foxy/Linux-Install-Debians/) install tutorial in order to install Foxy, which is what this demo is built on. 

If you run into the need to run python3-rosdep, You may need to install the rosdep package with the terminal command below

```bash
sudo apt-get install python3-rosdep
```

## Installation of Gazebo 11

In order to run this simulation, you need to have a standalone install of [Gazebo 11](http://gazebosim.org/tutorials?tut=install_ubuntu).
All new versions of ROS1 and ROS2, i.e. Noetic and Foxy currently, target Gazebo 11. 

## Installlation of gazebo_ros Package
The documentation has not been updated for the Foxy release but the package has been released to the public. You can install this package using the the command.
```bash
sudo apt install ros-foxy-gazebo-ros-pkgs
```
A good way to make sure everything is working well right now is to follow the final tutorial on this [Gazebo page](http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)

## Running this Demo:
In the installation of ROS2 you may have sourced ROS2 foxy from your .bashrc, if not you will need to enter the command
```bash
source /opt/ros/foxy/setup.bash
```
in every Terminal window you open so that the path variables are correctly set

**Follow these steps to run:**
1. Download the supplied the robot.sdf, this model has the gazebo_ros diff_drive plugin already formatted so you should be able to control this demo by publishing to its active topics. 
2. Open two terminal windows and source the ros2/foxy installation in each as described above
3. **cd** to the folder where the robot.sdf was downloaded in both terminals
3. In the first terminal window, start the gazebo environment by running this bash command,
```bash
gazebo --verbose -s libgazebo_ros_factory.so
```
4. Once your gazebo environment is up and running, open the second terminal window and spawn the robot.sdf in your environment using this ros command
```bash
ros2 run gazebo_ros spawn_entity.py -entity diff_SPIKE -file robot.sdf
```
5. Once your robot has been spawned into the environment you can check to see the active topics being published by issuing the command
```bash
ros2 topic list
```
6. You will be able control this robot by publishing to the /cmd_demo topic using the Twist msg. Here is a sample command to send in your second terminal.
```bash
ros2 topic pub /demo/cmd_demo geometry_msgs/Twist '{angular: {z: 6.0}}' -1
```
If everything is running correctly you should see the robot rotating around the z axis quite fast!

