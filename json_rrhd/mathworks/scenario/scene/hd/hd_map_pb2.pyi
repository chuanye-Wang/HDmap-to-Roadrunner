from mathworks.scenario.scene.hd import hd_lanes_pb2 as _hd_lanes_pb2
from mathworks.scenario.scene.hd import hd_lane_markings_pb2 as _hd_lane_markings_pb2
from mathworks.scenario.scene.hd import hd_junctions_pb2 as _hd_junctions_pb2
from mathworks.scenario.scene.hd import hd_barriers_pb2 as _hd_barriers_pb2
from mathworks.scenario.scene.hd import hd_signs_pb2 as _hd_signs_pb2
from mathworks.scenario.scene.hd import hd_static_objects_pb2 as _hd_static_objects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HDMap(_message.Message):
    __slots__ = ["lanes", "lane_boundaries", "lane_groups", "lane_markings", "junctions", "barrier_types", "barriers", "sign_types", "signs", "static_object_types", "static_objects"]
    LANES_FIELD_NUMBER: _ClassVar[int]
    LANE_BOUNDARIES_FIELD_NUMBER: _ClassVar[int]
    LANE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    LANE_MARKINGS_FIELD_NUMBER: _ClassVar[int]
    JUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    BARRIER_TYPES_FIELD_NUMBER: _ClassVar[int]
    BARRIERS_FIELD_NUMBER: _ClassVar[int]
    SIGN_TYPES_FIELD_NUMBER: _ClassVar[int]
    SIGNS_FIELD_NUMBER: _ClassVar[int]
    STATIC_OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    STATIC_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    lanes: _containers.RepeatedCompositeFieldContainer[_hd_lanes_pb2.Lane]
    lane_boundaries: _containers.RepeatedCompositeFieldContainer[_hd_lanes_pb2.LaneBoundary]
    lane_groups: _containers.RepeatedCompositeFieldContainer[_hd_lanes_pb2.LaneGroup]
    lane_markings: _containers.RepeatedCompositeFieldContainer[_hd_lane_markings_pb2.LaneMarking]
    junctions: _containers.RepeatedCompositeFieldContainer[_hd_junctions_pb2.Junction]
    barrier_types: _containers.RepeatedCompositeFieldContainer[_hd_barriers_pb2.BarrierTypeDefinition]
    barriers: _containers.RepeatedCompositeFieldContainer[_hd_barriers_pb2.Barrier]
    sign_types: _containers.RepeatedCompositeFieldContainer[_hd_signs_pb2.SignTypeDefinition]
    signs: _containers.RepeatedCompositeFieldContainer[_hd_signs_pb2.Sign]
    static_object_types: _containers.RepeatedCompositeFieldContainer[_hd_static_objects_pb2.StaticObjectTypeDefinition]
    static_objects: _containers.RepeatedCompositeFieldContainer[_hd_static_objects_pb2.StaticObject]
    def __init__(self, lanes: _Optional[_Iterable[_Union[_hd_lanes_pb2.Lane, _Mapping]]] = ..., lane_boundaries: _Optional[_Iterable[_Union[_hd_lanes_pb2.LaneBoundary, _Mapping]]] = ..., lane_groups: _Optional[_Iterable[_Union[_hd_lanes_pb2.LaneGroup, _Mapping]]] = ..., lane_markings: _Optional[_Iterable[_Union[_hd_lane_markings_pb2.LaneMarking, _Mapping]]] = ..., junctions: _Optional[_Iterable[_Union[_hd_junctions_pb2.Junction, _Mapping]]] = ..., barrier_types: _Optional[_Iterable[_Union[_hd_barriers_pb2.BarrierTypeDefinition, _Mapping]]] = ..., barriers: _Optional[_Iterable[_Union[_hd_barriers_pb2.Barrier, _Mapping]]] = ..., sign_types: _Optional[_Iterable[_Union[_hd_signs_pb2.SignTypeDefinition, _Mapping]]] = ..., signs: _Optional[_Iterable[_Union[_hd_signs_pb2.Sign, _Mapping]]] = ..., static_object_types: _Optional[_Iterable[_Union[_hd_static_objects_pb2.StaticObjectTypeDefinition, _Mapping]]] = ..., static_objects: _Optional[_Iterable[_Union[_hd_static_objects_pb2.StaticObject, _Mapping]]] = ...) -> None: ...
