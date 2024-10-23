from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'simple_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob(os.path.join('param', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lmc',
    maintainer_email='namgyushin@naver.com',
    description='simple_ros demo',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hello = simple_ros.hello:main",
            "hello_class = simple_ros.hello_class:main",
            "hello_sub = simple_ros.hello_sub:main",
            "hello_pub = simple_ros.hello_pub:main",
            "time_pub = simple_ros.time_pub:main",
            "move_turtle = simple_ros.move_turtle:main",
            "move_turtle_time = simple_ros.move_turtle_time:main",
            "move_turtle_ns = simple_ros.move_turtle_ns:main",
            "move_turtle_time_ns = simple_ros.move_turtle_time_ns:main",
            "service_server = simple_ros.service_server:main",
            "service_client = simple_ros.service_client:main",
            "user_int_pub = simple_ros.user_int_pub:main",
            "service_server_int = simple_ros.service_server_int:main",
            "simple_parameter = simple_ros.simple_parameter:main"
        ],
    },
)
