import socket
import rospy
from std_msgs.msg import *


class Udp_server:
    def __init__(self):
        rospy.init_node("udp_node", anonymous=True)
        self.pub = rospy.Publisher("/udp_server", String, queue_size=10)

    def main(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        HOST = ""
        PORT = 61557
        server_sock.bind((HOST, PORT))

        while True:
            data = server_sock.recvfrom(1024)
            udp_data = str(data).split(",")
            print("Client >> " + str(udp_data))
            self.pub.publish(str(data))


if __name__ == "__main__":
    try:
        udp_server = Udp_server()
        while not rospy.is_shutdown():
            udp_server.main()
    except rospy.ROSInterruptException:
        pass
