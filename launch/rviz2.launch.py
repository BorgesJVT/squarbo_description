import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory('squarbo_description'), 
            'launch', 
            'squarbo_state_publisher.launch.py')))

    rviz_config_dir = os.path.join(
        get_package_share_directory('squarbo_description'),
        'rviz',
        'squarbo_model.rviz')

    rviz2_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_dir],
        output='screen')

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(state_publisher_cmd)
    ld.add_action(rviz2_cmd)

    return ld
