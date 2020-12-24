#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from datetime import datetime

def callback(data):
  now = datetime.now()
  data.data = data.data + ' ' + now.strftime("%H:%M:%S")
  rospy.loginfo('%s', data.data)

def listener():
  rospy.init_node('listener', anonymous=True)

  rospy.Subscriber('chatter', String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
