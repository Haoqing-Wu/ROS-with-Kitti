#!/usr/bin/env python
import os
from data_utils import *
from publish_utils import *

DATA_PATH = '/home/tf77wwl/ROS-with-Kitti/data/2011_09_26/2011_09_26_drive_0005_sync/'

if __name__ == '__main__':
    frame = 0
    rospy.init_node('kitti_node', anonymous=True)
    cam_pub = rospy.Publisher('kitti_cam', Image, queue_size=10)
    pcl_pub = rospy.Publisher('kitti_point_cloud', PointCloud2, queue_size=10)
    ego_pub = rospy.Publisher('kitti_ego_car', MarkerArray, queue_size=10)
    imu_pub = rospy.Publisher('kitti_imu', Imu, queue_size=10)
    gps_pub = rospy.Publisher('kitti_gps', NavSatFix, queue_size=10)
    bridge = CvBridge()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        image = read_camera(os.path.join(DATA_PATH, 'image_02/data/%010d.png'%frame))
        publish_camera(cam_pub, bridge, image)

        point_cloud = read_point_cloud(os.path.join(DATA_PATH, 'velodyne_points/data/%010d.bin'%frame))
        publish_point_cloud(pcl_pub, point_cloud)

        publish_ego_car(ego_pub)
        
        imu_data = read_imu(os.path.join(DATA_PATH, 'oxts/data/%010d.txt'%frame))
        publish_imu(imu_pub, imu_data)
        publish_gps(gps_pub, imu_data)
        
        rospy.loginfo("Camera image and point cloud published")
        frame += 1
        frame %= 154
        rate.sleep()

