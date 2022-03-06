## MAPF Visualizer

### 设计要求
（1）场景
  根据MAPF的输出结果，显示栅格地图、多智能体的编号、每个时刻的位置和目标位置。

（2）输入
|名称|描述|数据结构|
|-|-|-|
|map|静态地图|array: map[width] [length]|
|paths|所有路径|list: paths[k] [len]|

（3）内部数据
|名称|描述|数据结构|
|-|-|-|
|map|静态地图|array: map[width] [length]|
|agent|智能体数据|agent-(number,color,start,end,path,path_length,k-robust,size_l,size_w,arrival)|
|time|时间|float|

### 功能
（1）读取输入数据map和paths


（2）展示每个时刻的多智能体的位置


（3）对每个时刻的所有智能体位置做检查，包括是否处于障碍物位置、多个智能体是否处于相同位置



