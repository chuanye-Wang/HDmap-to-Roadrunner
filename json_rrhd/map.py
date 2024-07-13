'''
created by zhongjiaru in 2023.08
import the yizhuang hd maps into Road Runner
'''
import json
import mathworks.scenario.scene.hd.hd_map_pb2 as hd_map_pb2
import mathworks.scenario.scene.hd.hd_map_header_pb2 as hd_map_header_pb2
from mathworks.scenario.scene.hd.hd_lanes_pb2 import TravelDir, LaneType
from mathworks.scenario.scene.hd.common_attributes_pb2 import Alignment

## add this official package
from google.protobuf.internal import encoder

LaneType_mapping = {
        'BIKING': LaneType.LANE_TYPE_BIKING,
        'CITY_DRIVING': LaneType.LANE_TYPE_DRIVING,
        'LEFT_TURN_WAITING_ZONE': LaneType.LANE_TYPE_DRIVING,
        'ROUNDABOUT': LaneType.LANE_TYPE_DRIVING, # 环形交叉路口
        'EMERGENCY_LANE': LaneType.LANE_TYPE_SHOULDER,  # 应急通道
}

TravelDir_mapping = {
        'FORWARD': TravelDir.TRAVEL_DIR_FORWARD,
}

class Map():
        def __init__(self, map_path, save_path) -> None:
                # just  pay attention to 'LANE'
                self.map_info = self.load_map(map_path)

                # self.lanes_info, self.juncs_info= self.reform_info()
                self.lanes_info = self.reform_info()

        def load_map(self, map_path):
                '''
                load map from .json file
                '''
                with open(map_path, 'r') as load_f:
                        my_json = json.load(load_f)
                return my_json
        
        def test(self):
                l = []
                for id, info in self.map_info.items():
                        if len(info['centerline']) != len(info['right_boundary']):
                                l.append(id)
                print(l)

        def find_missing_pre_suc(self):
                for lane_id, lane_info in self.map_info.items():
                        for pre in lane_info['predecessors']:
                                if pre not in self.map_info:
                                        print('{} not have pre {}'.format(lane_id, pre))
                        for suc in lane_info['successors']:
                                if suc not in self.map_info:
                                        print('{} not have suc {}'.format(lane_id, suc))


        def reform_info(self):
                '''
                reform map_info to road runner
                '''
                lanes_info = {}
                for lane_id, lane_info in self.map_info['LANE'].items():
                        info = {}
                        info['lane_id'] = lane_id
                        info['type'] = LaneType_mapping[lane_info['lane_type']]
                        info['direction'] = TravelDir_mapping['FORWARD']
                        centerline = self.convert_points(lane_info['centerline'])
                        info['geometry'] = centerline
                        info['predecessors'] = lane_info['predecessors']
                        info['successors'] = lane_info['successors']
                        info['left_boundary_id'] =  lane_id + '_lb'
                        info['right_boundary_id'] = lane_id + '_rb'
                        lb_geometry = self.convert_points(lane_info['left_boundary'])
                        rb_geometry = self.convert_points(lane_info['right_boundary'])
                        info['left_boundary_geometry'] = lb_geometry
                        info['right_boundary_geometry'] = rb_geometry

                        lanes_info[lane_id] = info

                # juncs_info = {}
                # for junc_id, junc_info in self.map_info['JUNCTION'].items():
                #         info = {}
                #         info['junc_id'] = junc_id
                #         polygon = self.convert_points(junc_info['polygon'])
                #         info['polygon'] = polygon

                #         juncs_info[junc_id] = info

                # return lanes_info, juncs_info
                return lanes_info

        def convert_points(self, points):
                tfd_offset = [-40251.76572214719, 326531.9706723457]
                result = []
                for p in points:
                        x, y = p.split(', ')
                        x = float(x[1:])
                        y = float(y[:-1])
                        x = x - tfd_offset[0]
                        y = y- tfd_offset[1]
                        result.append((x, y))
                # print(result)
                return result
        
        def build_map(self):
                my_model = hd_map_pb2.HDMap()

                for lane_id, lane_info in self.lanes_info.items():
                        lane = my_model.lanes.add()
                        lane.id = lane_id

                        lane_geometry = lane.geometry
                        for p in lane_info['geometry']:
                                point = lane_geometry.values.add()
                                point.x = p[0]
                                point.y = p[1]

                        lane.lane_type = lane_info['type']
                        lane.travel_dir = lane_info['direction']

                for lane_id, lane_info in self.lanes_info.items():
                        left_boundary = my_model.lane_boundaries.add()
                        left_boundary.id = lane_info['left_boundary_id']
                        lb_geometry = left_boundary.geometry

                        for p in lane_info['left_boundary_geometry']:
                                point = lb_geometry.values.add()
                                point.x = p[0]
                                point.y = p[1]

                        right_boundary = my_model.lane_boundaries.add()
                        right_boundary.id = lane_info['right_boundary_id']
                        rb_geometry = right_boundary.geometry
                        for p in lane_info['right_boundary_geometry']:
                                point = rb_geometry.values.add()
                                point.x = p[0]
                                point.y = p[1]

                # for junc_id, junc_info in self.juncs_info.items():
                #         junction = my_model.junctions.add()
                #         junction.id = junc_id
                #         polygon = junction.geometry.polygons.add()
                #         for p in junc_info['polygon']:
                #                 point = polygon.exterior_ring.values.add()
                #                 point.x = p[0]
                #                 point.y = p[1]

                for lane in my_model.lanes:
                        lane_id = lane.id
                        lane_info = self.lanes_info[lane_id]
                        lb_id = lane_info['left_boundary_id']
                        rb_id = lane_info['right_boundary_id']

                        referenceBoundary1 = lane.left_lane_boundary
                        referenceBoundary1.reference.id = lb_id
                        referenceBoundary1.alignment = Alignment.ALIGNMENT_FORWARD

                        referenceBoundary2 = lane.right_lane_boundary
                        referenceBoundary2.reference.id = rb_id
                        referenceBoundary2.alignment = Alignment.ALIGNMENT_FORWARD

                        
                        if len(lane_info['predecessors']) >=1:
                                for pre in lane_info['predecessors']:
                                        if pre not in self.lanes_info:
                                                continue
                                        predecessor = lane.predecessors.add()
                                        predecessor.reference.id = pre
                                        predecessor.alignment = Alignment.ALIGNMENT_FORWARD
                        
                        if len(lane_info['successors']) >= 1:
                                for suc in lane_info['successors']:
                                        if suc not in self.lanes_info:
                                                continue
                                        successor = lane.successors.add()
                                        successor.reference.id = suc
                                        successor.alignment = Alignment.ALIGNMENT_FORWARD
                return my_model

        def get_extremes(self):
                min_x = min_y = float("inf")
                max_x = max_y = float("-inf")

                for lane_id, lane_info in self.lanes_info.items():
                        for p in lane_info['geometry']:
                                if p[0] < min_x:
                                        min_x = p[0]
                                elif p[0] > max_x:
                                        max_x = p[0]
                                
                                if p[1] < min_y:
                                        min_y = p[1]
                                elif p[1] > max_y:
                                        max_y = p[1]
                        for p in lane_info['left_boundary_geometry']:
                                if p[0] < min_x:
                                        min_x = p[0]
                                elif p[0] > max_x:
                                        max_x = p[0]
                                
                                if p[1] < min_y:
                                        min_y = p[1]
                                elif p[1] > max_y:
                                        max_y = p[1]
                        for p in lane_info['right_boundary_geometry']:
                                if p[0] < min_x:
                                        min_x = p[0]
                                elif p[0] > max_x:
                                        max_x = p[0]
                                
                                if p[1] < min_y:
                                        min_y = p[1]
                                elif p[1] > max_y:
                                        max_y = p[1]
                
                return min_x, min_y, max_x, max_y
        
        def save_map(self, model, save_path):
                header_message = hd_map_header_pb2.Header()

                # Set the author of the file
                header_message.author = "zzz"

                # Set the projection of the file
                header_message.projection.projection = "+proj=tmerc +lat_0=0 +lon_0=117 +k=1 +x_0=500000 +y_0=0 +datum=WGS84 +units=m"

                min_x, min_y, max_x, max_y = self.get_extremes()
                # Set the geographic boundary of the file
                geo_bounds = header_message.geographic_boundary.bounds
                geo_bounds.max.x = max_x
                geo_bounds.max.y = max_y
                geo_bounds.max.z = 0
                geo_bounds.min.x = min_x
                geo_bounds.min.y = min_y
                geo_bounds.min.z = 0

                # Write the RRHD file to disk
                self.write_to_rr_hd(save_path, header_message, model)

        def write_to_rr_hd(self, filepath, header_message, hd_map):
                size = header_message.ByteSize()
                with open(filepath, "wb") as file:
                        file.write(encoder._VarintBytes(size))
                        file.write(header_message.SerializeToString())
                        file.write(hd_map.SerializeToString())


def main(map_path, save_path):
        map = Map(map_path, save_path)
        model = map.build_map()
        map.save_map(model, save_path)

if __name__ == '__main__':
        map_path = '../box_json/filtered_lanes.json'
        save_path = 'filtered_map4.rrhd'
        
        # map_path = '../map/yizhuang_hdmap4.json'
        # save_path = '../../outp_map/map9.rrhd'
        
        main(map_path, save_path)
        print(f'文件已成功生成在： {save_path}')

