#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node=Node("py_node1")
    node.get_logger().info("coucou node1")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main()