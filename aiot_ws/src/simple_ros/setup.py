from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simple_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='test',
    maintainer_email='cjp8042000@gmail.com',
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
        "move_turtle = simple_ros.move_turtle:main"
        ],
    },
)
