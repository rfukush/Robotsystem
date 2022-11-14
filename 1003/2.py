#!/usr/bin/env python
import rospy, actionlib
from move_base_msgs.msg import *

if __name__ == '__main__':
    try:
        rospy.init_node('send_goal', anonymous=True)
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.pose.position.x=10;
        goal.target_pose.pose.position.y=20;
        goal.target_pose.pose.position.z=20;
        goal.target_pose.pose.orientation.w = 1
        rospy.loginfo("send goal")
        rospy.loginfo(goal)
        client.send_goal(goal)
        rospy.loginfo("wait for goal ...")
        ret = client.wait_for_result()
        rospy.loginfo("done")
    except rospy.ROSInterruptException: pass 