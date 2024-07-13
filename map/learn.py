import json
json_path = 'yizhuang_hdmap4.json'
save_path = 'learnmap'


class supper_map():
    def __init__(self, json_path, save_path) -> None:
        # print('init')
        self.map_json = self.load_map(json_path)
        pass

    def load_map(self,json_path):
        # print('load_map')
        with open(json_path, 'r') as json_file:
             map = json.load(json_file)
             return map
    
    def show(self):
        # show = self.map_json['LANE'].items()
        for lane_id, lane_info in self.map_json['LANE'].items():
            print(lane_id)
            print(lane_info)
        # print(f'看看读取出来的map什么样子{show}')


def main():

    Mymap = supper_map(json_path,save_path)

    Mymap.show()




if __name__ == '__main__':
    
    main()
    
    
