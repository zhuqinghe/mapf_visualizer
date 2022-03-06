## MAPF Visualizer

### 0 依赖/Dependency
Python3, Numpy

Pygame(展示/display)

PIL,opencv(将结果保存为视频/save result as video)

```
python visualizer.py -m ../input/random-32-32-20.map -p ../input/paths.txt -s True -sm gif
```

### 1 设计/Design
#### (1)概述/Abstract

根据输入地图、MAPF算法结果（路径列表），显示栅格地图、多智能体的编号、每个时刻的位置和目标位置。

Visualize gridmap and number, current and target position of agents based on input map and MAPF algorithm solution(list of paths). 

<div align=center>
<img src="50-agent_48-setp.gif" width="60%" height="60%">
</div>

#### (2)数据/Data
|变量/variable|描述/description|数据结构/datastructure|
|-|-|-|
|map|静态地图/static map|array: map[width] [length]|
|paths|所有路径/all path|list: paths[k] [len]|
|time|时间/time|float|
|agent|智能体类/class agent||

### 2 功能/Function
(1)读取输入数据random.map和paths.txt。Read random.map and paths.txt into map and paths variable.

(2)展示每个时刻的多智能体的位置和目标位置。Display position and target of agents for each timestep.

(3)对每个时刻的智能体做碰撞检查，包括与障碍物或其他智能体碰撞。
Check potential collisiosn of agents for each timestep, including collisions with obstacles and other agents. 

(4)将展示结果保存为视频。
Save the display result as video.

### 3 待开发/TODO
(1) 对k-robust问题和大尺寸智能体MAPF算法结果进行展示。Display k-robust and large-size MAPF solution.



