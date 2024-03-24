import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/broj',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Int32, '/kvadrat_broja', 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        dobiveni_broj = msg.data
        kvadrat_broja = dobiveni_broj ** 2
        kvadrat_msg = Int32()
        kvadrat_msg.data = kvadrat_broja
        self.publisher_.publish(kvadrat_msg)
        #self.get_logger().info('Kvadrat primljenog broja: %d' % kvadrat_broja)	# za troobleshootanje je trebalo

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

