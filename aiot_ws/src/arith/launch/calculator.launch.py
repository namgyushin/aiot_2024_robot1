import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    param_dir = LaunchConfiguration('param_dir',
                                    default=os.path.join(
                                        get_package_share_directory('arith'),
                                        'param',
                                        'calculator.yaml'))
    return LaunchDescription([
        DeclareLaunchArgument('param_dir',
                              default_value=param_dir,
                              description="simple parameter"),
        Node(package="arith",
             executable="argument",
             parameters=[param_dir]),
        Node(package="arith",
             executable="calculator",
             parameters=[param_dir]),
        Node(package="arith",
             executable="operator",
             parameters=[param_dir]),
        ])