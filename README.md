# ROS-with-Kitti
 ## New Package Setup
 - Environment: WSL2 + Ubuntu20.04 + ROS Noetic
 - Dataset: Kitti Raw Data https://www.cvlibs.net/datasets/kitti/raw_data.php
 - Download the data [synced+rectified data] and calibration file [calibration] and extract in the folder structure like
   - /catkin_ws
   - /data
     - /2011_09_26
       - /2011_09_26_drive_xxxx_sync
         - /image_00
         - /image_01
         - /image_02
         - /image_03
         - /oxts
         - velodyne_points
       - calib_cam_to_cam
       - calib_imu_to_cam
       - calib_velo_to_cam
- Create package 
    ```bash
    ~/ROS-with-Kitti/catkin_ws/src$ catkin_create_pkg kitti_tutorial rospy
    ```
- Create cmake
    ```bash
     ~/ROS-with-Kitti/catkin_ws$ catkin_make
    ```
- Create the .py of the test project in the package /src folder and make it executable
    ```bash
    ~/ROS-with-Kitti/catkin_ws/src/kitti_tutorial/src$ chmod +x kitti.py
    ```
- Run the script of ros topic
    ```bash
    ~/ROS-with-Kitti/catkin_ws/src/kitti_tutorial/src$ rosrun kitti_tutorial kitti.py
    ```
- If using WSL, I use Xlaunch to forward visualization like rviz and gazebo to Windows display
  - Install Xlaunch
  - Add these lines under .bashrc
    ```bash
    export GAZEBO_IP=127.0.0.1
    export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
    export LIBGL_ALWAYS_INDIRECT=0
    ```
