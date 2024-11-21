import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'move_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/urdf', glob(os.path.join('urdf', '*.*'))),
        ('share/' + package_name + '/rviz', glob(os.path.join('rviz', '*.rviz'))),
        ('share/' + package_name + '/meshes', glob(os.path.join('meshes', '*.*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lmc',
    maintainer_email='namgyushin@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_circle = move_turtle.move_circle:main',
            'move_rect = move_turtle.move_rect:main',
            'follow_wall = move_turtle.follow_wall:main',
            'follow_wall_tf = move_turtle.follow_wall_tf:main',
            'follow_waypoints = move_turtle.follow_waypoints:main',
            'follow_waypoints_loop = move_turtle.follow_waypoints_loop:main'
            'follow_ar_marker = move_turtle.follow_ar_marker:main',
            'led_server = move_turtle.led_server:main',
            'servo_server = move_turtle.servo_server:main',
            'servo_sub = move_turtle.servo_sub:main',
            'arduino_led = move_turtle.arduino_led:main',
            'arduino_switch = move_turtle.arduino_switch:main',
            'arduino_servo = move_turtle.arduino_servo:main',
            'arduino_lcd = move_turtle.arduino_lcd:main',
            'patrol_manipulator = move_turtle.patrol_manipulator:main',
        ],
    },
)
