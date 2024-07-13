#### OpenDRIVE数据结构的解读
oxdr文件道路的详细信息，包含了道路的几何形状、车道、限速等。

文件头部 (<header>)
revMajor 和 revMinor: OpenDRIVE版本号，表示这是版本1.4。
name: 道路的名称（此处为空）。
version: 文件版本号。
date: 文件生成的日期和时间。
north, south, east, west: 道路覆盖的地理边界。
vendor: 生成文件的软件，此处为MathWorks。
userData: 用户数据，包含生成文件的软件版本信息。
道路定义 (<road>)
name: 道路名称“Road 0”。
length: 道路长度，单位为米。
id: 道路的唯一标识符。
junction: 表示道路是否属于一个路口（-1表示不属于任何路口）。
道路类型 (<type>)
s: 道路类型的起始位置。
type: 道路类型，此处为“town”。
speed: 道路限速，单位为英里每小时（mph），最大速度为40mph。
道路平面视图 (<planView>)
geometry: 几何形状定义。
s: 几何形状的起始位置。
x, y: 几何形状起点的坐标。
hdg: 几何形状的起始方向角。
length: 几何形状的长度。
line: 表示这段几何形状为直线。
高程配置 (<elevationProfile>)
elevation: 高程信息。
s, a, b, c, d: 高程的多项式参数，表示高程随道路长度的变化。
横向配置 (<lateralProfile>)
superelevation: 道路的横向倾斜信息。
s, a, b, c, d: 横向倾斜的多项式参数。
shape: 横断面形状。
s, t, a, b, c, d: 横断面形状的多项式参数。
车道信息 (<lanes>)
laneOffset: 车道偏移。
s, a, b, c, d: 车道偏移的多项式参数。
laneSection: 车道区段。
s: 车道区段的起始位置。
singleSide: 是否单侧车道（false表示双侧）。
左侧车道 (<left>)
lane: 车道信息。
id: 车道ID，正数表示左侧车道。
type: 车道类型（如sidewalk、shoulder、driving等）。
level: 车道是否平坦（false表示不平坦）。
width: 车道宽度。
sOffset: 宽度的起始位置。
a, b, c, d: 宽度的多项式参数。
roadMark: 道路标记。
sOffset: 标记的起始位置。
type: 标记类型（如none、curb等）。
width, material, weight, color, laneChange: 标记的属性。
speed: 车道限速。
sOffset: 限速的起始位置。
max: 最大速度。
unit: 速度单位。
height: 车道高度。
sOffset: 高度的起始位置。
inner, outer: 内侧和外侧高度。
userData: 用户数据。
vectorLane: 车道的额外信息。
sOffset: 额外信息的起始位置。
laneId: 车道的唯一标识符。
travelDir: 行驶方向。
中央车道 (<center>)
lane: 中央车道信息。
id: 车道ID，0表示中央车道。
type: 车道类型。
roadMark: 道路标记。
右侧车道 (<right>)
lane: 车道信息。
id: 车道ID，负数表示右侧车道。
type: 车道类型。
width, roadMark, speed, height, userData: 同左侧车道类似。
用户数据 (<userData>)
vectorLaneSection: 车道区段的额外信息。
carriageway: 道路的额外信息。
rightBoundary, leftBoundary: 右侧和左侧边界。
这个OpenDRIVE文件详细描述了道路的几何形状、车道配置和限速信息，适用于仿真环境中的道路建模和交通仿真。