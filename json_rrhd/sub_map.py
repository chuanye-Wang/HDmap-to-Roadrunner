'''
created by zhongjiaru in 2023.08
import the yizhuang hd maps into Road Runner
'''
import json
import mathworks.scenario.scene.hd.hd_map_pb2 as hd_map_pb2
import mathworks.scenario.scene.hd.hd_map_header_pb2 as hd_map_header_pb2
from mathworks.scenario.scene.hd.hd_lanes_pb2 import TravelDir, LaneType
from mathworks.scenario.scene.hd.common_attributes_pb2 import Alignment
from shapely.geometry import Polygon
## add this official package
from google.protobuf.internal import encoder

LaneType_mapping = {
        'BIKING': LaneType.LANE_TYPE_BIKING,
        'CITY_DRIVING': LaneType.LANE_TYPE_DRIVING,
        'LEFT_TURN_WAITING_ZONE': LaneType.LANE_TYPE_DRIVING,
        'ROUNDABOUT': LaneType.LANE_TYPE_DRIVING,
        'EMERGENCY_LANE': LaneType.LANE_TYPE_SHOULDER,
}

TravelDir_mapping = {
        'FORWARD': TravelDir.TRAVEL_DIR_FORWARD,
}

class Map():
        def __init__(self, map_path) -> None:
                # just  pay attention to 'LANE'
                self.map_info = self.load_map(map_path)
                self.lanes_info, self.juncs_info= self.reform_info()
                self.remove_containlanes()

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
                        polygon = lb_geometry + rb_geometry
                        info['polygon'] = Polygon(polygon)

                        lanes_info[lane_id] = info

                juncs_info = {}
                for junc_id, junc_info in self.map_info['JUNCTION'].items():
                        info = {}
                        info['junc_id'] = junc_id
                        polygon = self.convert_points(junc_info['polygon'])
                        info['polygon'] = polygon
                        info['polygon_inter'] = Polygon(polygon)

                        juncs_info[junc_id] = info

                choosed_lanes = ['15641486_1_-1', '15641486dup1_1_-1', '15678097a_1_-1', 
                                                        '15678098a_1_-1', '15651261_1_-1', '15651260_1_-1', '15651259_1_-1']
                choosed_junctions = ['15688893']

                choosed_lanes_info = {}
                choosed_juncs_info = {}
                for lane_id in choosed_lanes:
                        choosed_lanes_info[lane_id] = lanes_info[lane_id]

                for junc_id in choosed_junctions:
                        choosed_juncs_info[junc_id] = juncs_info[junc_id]
                return choosed_lanes_info, choosed_juncs_info

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

                        if lane_id == '15651260_1_-1':
                                print(lane_info['geometry'])
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

                for junc_id, junc_info in self.juncs_info.items():
                        junction = my_model.junctions.add()
                        junction.id = junc_id
                        polygon = junction.geometry.polygons.add()
                        for p in junc_info['polygon']:
                                point = polygon.exterior_ring.values.add()
                                point.x = p[0]
                                point.y = p[1]
                        for lane_id in junc_info['lanes']:
                                lane = junction.lanes.add()
                                lane.id = lane_id

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

                # Add static objects to the model
                # Define pole type of static object
                staticObjectType1 = my_model.static_object_types.add()
                staticObjectTypeID1 = "StaticObjectType1"
                staticObjectType1.id = staticObjectTypeID1
                staticObjectType1_asset_path = staticObjectType1.asset_path
                staticObjectType1_asset_path.asset_path = "Assets/Props/Trees/.fbx"

                # Add pole to the model
                tfd_offset = [-40251.76572214719, 326531.9706723457]
                pole = [416766, 4732399]
                pole[0] = pole[0] - tfd_offset[0]
                pole[1] = pole[1] - tfd_offset[1]
                so1 = my_model.static_objects.add()
                so1.id = "Pole1"
                so1Geometry = so1.geometry
                so1center = so1Geometry.center
                so1center.x = pole[0]
                so1center.y = pole[1]
                so1center.z = 1.4
                so1dimension = so1Geometry.dimension
                so1dimension.length = 1
                so1dimension.width = 1
                so1dimension.height = 3.3 / 2.0
                so1geoOrientation = so1Geometry.geo_orientation
                so1geoAngle = so1geoOrientation.geo_angle
                so1geoAngle.roll = 0
                so1geoAngle.pitch = 0
                so1geoAngle.heading = 0
                so1TypeRef = so1.object_type_ref
                so1TypeRef.id = staticObjectTypeID1

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
        
        def remove_containlanes(self):
                del_lanes = []
                for junc_id, junc_info in self.juncs_info.items():
                        junc_poly = junc_info['polygon_inter']
                        connect_lanes = []
                        for lane_id, lane_info in self.lanes_info.items():
                                lane_poly = lane_info['polygon']
                                # if junc_poly.contains(lane_poly):
                                #         del_lanes.append(lane_id)
                                #         continue
                                if junc_poly.intersects(lane_poly):
                                        connect_lanes.append(lane_id)
                        junc_info['lanes'] = connect_lanes

                for k in del_lanes:
                        del self.lanes_info[k]
                

        def save_map(self, model, save_path):
                header_message = hd_map_header_pb2.Header()

                # Set the author of the file
                header_message.author = "zjr"

                # Set the projection of the file
                header_message.projection.projection = "+proj=tmerc +lat_0=0 +lon_0=117 +k=1 +x_0=500000 +y_0=0 +datum=WGS84 +units=m"

                min_x, min_y, max_x, max_y = self.get_extremes()
                print((min_x+max_x)/2, (min_y+max_y)/2)
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
        map = Map(map_path)
        model = map.build_map()
        map.save_map(model, save_path)

if __name__ == '__main__':
        map_path = 'C:/Users/55350/Desktop/maps/yizhuang_hdmap4.json'
        # save_path = '../../outp_map/map4.rrhd'
        save_path = 'C:/Users/55350/Desktop/yizhuang-hdmap/Assets/z_map/map4.rrhd'
        main(map_path, save_path)
        print(f'文件已成功生成在： {save_path}')

