from setuptools import setup

package_name = 'turtlesim_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='تحكم بسيط في turtlesim باستخدام ROS2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'turtle_move = turtlesim_control.turtle_move:main',
        ],
    },
)
