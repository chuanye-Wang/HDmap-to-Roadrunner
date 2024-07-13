import json

# 定义范围
x_min = 417712.819055685
x_max = 417983.059747824
y_min = 4731530.90724919
y_max = 4731810.92678807

# 从文件中读取数据
with open('../map/yizhuang_hdmap4.json', 'r') as file:
    data = json.load(file)

def is_within_range(coord, x_min, x_max, y_min, y_max):
    x, y = map(float, coord.strip("()").split(", "))
    return x_min <= x <= x_max and y_min <= y <= y_max

def check_lane_within_range(lane_data, x_min, x_max, y_min, y_max):
    for coord_list in ["centerline", "left_boundary", "right_boundary"]:
        for coord in lane_data.get(coord_list, []):
            if is_within_range(coord, x_min, x_max, y_min, y_max):
                return True
    return False

# 筛选在范围内的道路ID并保留信息
filtered_data = {
    "LANE": {lane_id: lane_data for lane_id, lane_data in data['LANE'].items() if check_lane_within_range(lane_data, x_min, x_max, y_min, y_max)}
}

# 将过滤后的数据写入新的JSON文件
output_filename = 'filtered_lanes.json'
with open(output_filename, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=4)

print(f"Filtered lane data has been saved to {output_filename}")