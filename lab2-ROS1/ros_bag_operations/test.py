import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os

#global count
 

def callback(data):
  try:
    cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
  except CvBridgeError as e:
    print(e)

  #cv2.imshow("123", cv_image)
  output_dir = "/media/basic/Transcend/Cone_rosbag/cpev09_part1/2018-09-04-11-18_cpev9/rosfile"
  cv2.imwrite(os.path.join(output_dir, str(data.header.stamp) + ".png"), cv_image)
  print "Wrote image ",  data.header.stamp
  #cv2.waitKey(33)




if __name__ == "__main__":

  #topic = "/pylon_camera_node/image_raw"
  topic = "/pylon_camera_node/image_raw"

  rospy.init_node('listener')
  rospy.Subscriber(topic, Image, callback)
  rospy.spin()
