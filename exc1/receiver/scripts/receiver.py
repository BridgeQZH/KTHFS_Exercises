#!/usr/bin/env python
import rospy
import sys
# from std_msgs.msg import String
from std_msgs.msg import Int32, Float32, String

class simple_class:
    def __init__(self):
        self.sub = rospy.Subscriber("qiao",Int32,self.callback)
    def callback(self,data):
        self.pub = rospy.Publisher('result', Float32, queue_size=10)
        self.pub.publish(data.data/0.15)
        # turn this on, you can see the data on the receiver window
        # print(data.data/0.15)
    
if __name__ == '__main__':
    rospy.init_node('receiver', anonymous=True)
    obc = simple_class()
    rospy.spin()
