#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def talker():
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.init_node('talker', anonymous=True)
  r = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    twist = Twist()
    twist.linear.x = 10
    twist.linear.y = 10
    twist.linear.z = 10
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 10
    pub.publish(twist)

if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException: pass