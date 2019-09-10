#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int32, Float32, String

def broadcast():
    pub = rospy.Publisher('qiao', Int32, queue_size=10)
    rospy.init_node('broadcast', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    i = 0
    while not rospy.is_shutdown():
        pub.publish(3+4*i) #suppose k = 3
        rospy.loginfo(3+4*i)
        i = i + 1
        rate.sleep()
        
if __name__ == '__main__':
    try:
        broadcast()
    except rospy.ROSInterruptException:
        pass
