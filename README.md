# squarbo_description
URDF model of Squarbo, a differential robot of ~10cm X 10cm.

## Instalation
``` bash
cd squarbo_ws/src
git clone https://github.com/BorgesJVT/squarbo_description/tree/main 
cd ..
colcon build
```

## Run
``` bash
ros2 launch squarbo_description rviz2.launch.py
```

<img src="/squarbo_rviz.png" width="800">

