from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensorDetectionCoordinates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SENSOR_DETECTION_COORDINATES_UNSPECIFIED: _ClassVar[SensorDetectionCoordinates]
    SENSOR_DETECTION_COORDINATES_WORLD_CARTESIAN: _ClassVar[SensorDetectionCoordinates]
    SENSOR_DETECTION_COORDINATES_HOST_CARTESIAN: _ClassVar[SensorDetectionCoordinates]
    SENSOR_DETECTION_COORDINATES_SENSOR_CARTESIAN: _ClassVar[SensorDetectionCoordinates]
    SENSOR_DETECTION_COORDINATES_SENSOR_SPHERICAL: _ClassVar[SensorDetectionCoordinates]

class RayInteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RAY_INTERACTION_TYPE_UNSPECIFIED: _ClassVar[RayInteractionType]
    RAY_INTERACTION_TYPE_DESTINATION: _ClassVar[RayInteractionType]
    RAY_INTERACTION_TYPE_REFLECTION: _ClassVar[RayInteractionType]
    RAY_INTERACTION_TYPE_EDGE_DIFFRACTION: _ClassVar[RayInteractionType]
SENSOR_DETECTION_COORDINATES_UNSPECIFIED: SensorDetectionCoordinates
SENSOR_DETECTION_COORDINATES_WORLD_CARTESIAN: SensorDetectionCoordinates
SENSOR_DETECTION_COORDINATES_HOST_CARTESIAN: SensorDetectionCoordinates
SENSOR_DETECTION_COORDINATES_SENSOR_CARTESIAN: SensorDetectionCoordinates
SENSOR_DETECTION_COORDINATES_SENSOR_SPHERICAL: SensorDetectionCoordinates
RAY_INTERACTION_TYPE_UNSPECIFIED: RayInteractionType
RAY_INTERACTION_TYPE_DESTINATION: RayInteractionType
RAY_INTERACTION_TYPE_REFLECTION: RayInteractionType
RAY_INTERACTION_TYPE_EDGE_DIFFRACTION: RayInteractionType

class FieldOfView(_message.Message):
    __slots__ = ["azimuth", "elevation"]
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    azimuth: float
    elevation: float
    def __init__(self, azimuth: _Optional[float] = ..., elevation: _Optional[float] = ...) -> None: ...

class RangeLimits(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class RayIntersection(_message.Message):
    __slots__ = ["position", "distance", "normal", "target_id", "target_material", "ray_direction"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    RAY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    position: _geometry_pb2.Vector3
    distance: float
    normal: _geometry_pb2.Vector3
    target_id: str
    target_material: str
    ray_direction: _geometry_pb2.Vector3
    def __init__(self, position: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., distance: _Optional[float] = ..., normal: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., target_id: _Optional[str] = ..., target_material: _Optional[str] = ..., ray_direction: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class RayPath(_message.Message):
    __slots__ = ["start_position", "interactions"]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    start_position: _geometry_pb2.Vector3
    interactions: _containers.RepeatedCompositeFieldContainer[RayInteraction]
    def __init__(self, start_position: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., interactions: _Optional[_Iterable[_Union[RayInteraction, _Mapping]]] = ...) -> None: ...

class RayInteraction(_message.Message):
    __slots__ = ["interaction_type", "intersection"]
    INTERACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERSECTION_FIELD_NUMBER: _ClassVar[int]
    interaction_type: RayInteractionType
    intersection: RayIntersection
    def __init__(self, interaction_type: _Optional[_Union[RayInteractionType, str]] = ..., intersection: _Optional[_Union[RayIntersection, _Mapping]] = ...) -> None: ...
