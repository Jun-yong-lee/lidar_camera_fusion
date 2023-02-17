#!/usr/bin/env python

import rospy
import time
import math as mt
from sensor_msgs.msg import LaserScan

def lidar_callback(data):
    global lidar_points
    lidar_points = data.ranges

lidar_points = None

rospy.init_node('camera_lidar_fusion', anonymous=True)
rospy.Subscriber("/scan", LaserScan, lidar_callback, queue_size=1)

while not rospy.is_shutdown():
    if lidar_points == None:
        continue

    xyz = []
    for idx, value in enumerate(lidar_points):
        rtn = []
        idx_ = idx - 90
        if (lidar_points[idx] != 0.0):
            rtn.append(lidar_points[idx] * mt.sin(idx_ * 0.8571428571)) # x
            rtn.append(lidar_points[idx] * mt.cos(idx_ * 0.8571428571)) # y
            rtn.append(1) # z
        xyz.append(rtn)

    print(xyz)
    #print(set(xyz))
    time.sleep(3.0)
    print(len(lidar_points))
    print(len(rtn))

# r * sin @ = x
# 
# r * cos @ = y

# 360/420 = 0.8571428571
