#!/usr/bin/env python
# This file is used to see the data published to the result topic
import rospy
from std_msgs.msg import Float32

def callback(data):
    print(round(data.data,2))
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("result", Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()