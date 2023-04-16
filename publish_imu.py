#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Header
from geometry_msgs.msg import Vector3

def imu_data_generator(time):

    imu=Imu()
    imu.header = Header()

    # give values to linear and angular accelaration and add time to the values to make it time dependent.
    imu.linear_acceleration = Vector3(2.5, 0+time, -9.8)
    imu.angular_velocity = Vector3(1, 1, 1 + time)

    # set quarternion to identity
    imu.orientation.x = 0
    imu.orientation.y = 0
    imu.orientation.z = 0
    imu.orientation.w = 1

    return imu


def publisher_script():
    rospy.init_node('imu_publisher')
    imu_pub = rospy.Publisher('/imu', Imu, queue_size=10)
    rate = rospy.Rate(10) # publish at 10Hz

    start_time = rospy.Time.now()
    while (rospy.Time.now() - start_time).to_sec() < 10:
        time = (rospy.Time.now() - start_time).to_sec()
        imu=imu_data_generator(time)
        # publish IMU data
        imu.header.stamp = rospy.Time.now()
        imu_pub.publish(imu)
        rate.sleep()    

if __name__ == '__main__':
    try:
        publisher_script()
    except rospy.ROSInterruptException:
        pass
