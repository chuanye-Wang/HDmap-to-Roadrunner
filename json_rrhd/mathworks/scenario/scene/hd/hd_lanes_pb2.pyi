from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from mathworks.scenario.scene.hd import hd_lane_markings_pb2 as _hd_lane_markings_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TravelDir(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRAVEL_DIR_UNSPECIFIED: _ClassVar[TravelDir]
    TRAVEL_DIR_UNDIRECTED: _ClassVar[TravelDir]
    TRAVEL_DIR_FORWARD: _ClassVar[TravelDir]
    TRAVEL_DIR_BACKWARD: _ClassVar[TravelDir]
    TRAVEL_DIR_BIDIRECTIONAL: _ClassVar[TravelDir]

class LaneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LANE_TYPE_UNSPECIFIED: _ClassVar[LaneType]
    LANE_TYPE_DRIVING: _ClassVar[LaneType]
    LANE_TYPE_SHOULDER: _ClassVar[LaneType]
    LANE_TYPE_BORDER: _ClassVar[LaneType]
    LANE_TYPE_RESTRICTED: _ClassVar[LaneType]
    LANE_TYPE_PARKING: _ClassVar[LaneType]
    LANE_TYPE_CURB: _ClassVar[LaneType]
    LANE_TYPE_SIDEWALK: _ClassVar[LaneType]
    LANE_TYPE_CENTER_TURN: _ClassVar[LaneType]
    LANE_TYPE_BIKING: _ClassVar[LaneType]
    LANE_TYPE_ENTRY: _ClassVar[LaneType]
    LANE_TYPE_EXIT: _ClassVar[LaneType]
    LANE_TYPE_OFFRAMP: _ClassVar[LaneType]
    LANE_TYPE_ONRAMP: _ClassVar[LaneType]
    LANE_TYPE_STOP: _ClassVar[LaneType]
    LANE_TYPE_MEDIAN: _ClassVar[LaneType]
    LANE_TYPE_NONE: _ClassVar[LaneType]
TRAVEL_DIR_UNSPECIFIED: TravelDir
TRAVEL_DIR_UNDIRECTED: TravelDir
TRAVEL_DIR_FORWARD: TravelDir
TRAVEL_DIR_BACKWARD: TravelDir
TRAVEL_DIR_BIDIRECTIONAL: TravelDir
LANE_TYPE_UNSPECIFIED: LaneType
LANE_TYPE_DRIVING: LaneType
LANE_TYPE_SHOULDER: LaneType
LANE_TYPE_BORDER: LaneType
LANE_TYPE_RESTRICTED: LaneType
LANE_TYPE_PARKING: LaneType
LANE_TYPE_CURB: LaneType
LANE_TYPE_SIDEWALK: LaneType
LANE_TYPE_CENTER_TURN: LaneType
LANE_TYPE_BIKING: LaneType
LANE_TYPE_ENTRY: LaneType
LANE_TYPE_EXIT: LaneType
LANE_TYPE_OFFRAMP: LaneType
LANE_TYPE_ONRAMP: LaneType
LANE_TYPE_STOP: LaneType
LANE_TYPE_MEDIAN: LaneType
LANE_TYPE_NONE: LaneType

class Lane(_message.Message):
    __slots__ = ["id", "geometry", "travel_dir", "left_lane_boundary", "right_lane_boundary", "predecessors", "successors", "lane_type", "metadata"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DIR_FIELD_NUMBER: _ClassVar[int]
    LEFT_LANE_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    RIGHT_LANE_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    PREDECESSORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSORS_FIELD_NUMBER: _ClassVar[int]
    LANE_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.Vector3List
    travel_dir: TravelDir
    left_lane_boundary: _common_attributes_pb2.AlignedReference
    right_lane_boundary: _common_attributes_pb2.AlignedReference
    predecessors: _containers.RepeatedCompositeFieldContainer[_common_attributes_pb2.AlignedReference]
    successors: _containers.RepeatedCompositeFieldContainer[_common_attributes_pb2.AlignedReference]
    lane_type: LaneType
    metadata: _containers.RepeatedCompositeFieldContainer[_common_attributes_pb2.Metadata]
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.Vector3List, _Mapping]] = ..., travel_dir: _Optional[_Union[TravelDir, str]] = ..., left_lane_boundary: _Optional[_Union[_common_attributes_pb2.AlignedReference, _Mapping]] = ..., right_lane_boundary: _Optional[_Union[_common_attributes_pb2.AlignedReference, _Mapping]] = ..., predecessors: _Optional[_Iterable[_Union[_common_attributes_pb2.AlignedReference, _Mapping]]] = ..., successors: _Optional[_Iterable[_Union[_common_attributes_pb2.AlignedReference, _Mapping]]] = ..., lane_type: _Optional[_Union[LaneType, str]] = ..., metadata: _Optional[_Iterable[_Union[_common_attributes_pb2.Metadata, _Mapping]]] = ...) -> None: ...

class ParametricAttribution(_message.Message):
    __slots__ = ["span", "marking_reference"]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    MARKING_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    span: _common_attributes_pb2.ParametricRange
    marking_reference: _hd_lane_markings_pb2.MarkingReference
    def __init__(self, span: _Optional[_Union[_common_attributes_pb2.ParametricRange, _Mapping]] = ..., marking_reference: _Optional[_Union[_hd_lane_markings_pb2.MarkingReference, _Mapping]] = ...) -> None: ...

class LaneBoundary(_message.Message):
    __slots__ = ["id", "geometry", "parametric_attributes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    PARAMETRIC_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.Vector3List
    parametric_attributes: _containers.RepeatedCompositeFieldContainer[ParametricAttribution]
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.Vector3List, _Mapping]] = ..., parametric_attributes: _Optional[_Iterable[_Union[ParametricAttribution, _Mapping]]] = ...) -> None: ...

class LaneGroup(_message.Message):
    __slots__ = ["id", "geometry", "lanes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    LANES_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.Vector3List
    lanes: _containers.RepeatedCompositeFieldContainer[_common_attributes_pb2.AlignedReference]
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.Vector3List, _Mapping]] = ..., lanes: _Optional[_Iterable[_Union[_common_attributes_pb2.AlignedReference, _Mapping]]] = ...) -> None: ...
