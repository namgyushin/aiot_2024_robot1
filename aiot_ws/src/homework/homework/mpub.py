import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSDurabilityPolicy,
    QoSHistoryPolicy,
    QoSProfile,
    QoSReliabilityPolicy,
)
from std_msgs.msg import String


class Message_pub(Node):
    def __init__(self):
        super().__init__("mpub")
        self.qos_profile = QoSProfile(history=QoSHistoryPolicy.KEEP_ALL,
                                      reliability=QoSReliabilityPolicy.RELIABLE,
                                      durability=QoSDurabilityPolicy.TRANSIENT_LOCAL)
        self.create_timer(1, self.print_message)
        self.pub = self.create_publisher(String, "message", self.qos_profile)
        self.number = 0

    def print_message(self):
        msg = String()
        msg.data = f"this is message from mpub! + {self.number}"
        self.pub.publish(msg)
        print(msg.data)
        self.number += 1

def main():
    rclpy.init()
    node = Message_pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()