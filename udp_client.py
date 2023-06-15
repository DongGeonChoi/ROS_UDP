import rospy
from std_msgs.msg import *


class Udp_client:
    def __init__(self):
        rospy.init_node("listener", anonymous=True)
        rospy.Subscriber("/udp_server", String, self.udp_CB)
        self.data = ""

    def udp_CB(self, data):
        list_1 = str(data).split(",")
        for st in list_1:
            print(st)

    def main(self):
        pass


if __name__ == "__main__":
    try:
        udp_client = Udp_client()
        while not rospy.is_shutdown():
            udp_client.main()
    except rospy.ROSInterruptException:
        pass
