from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.simulation import comparison_pb2 as _comparison_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PARAMETER_TYPE_UNSPECIFIED: _ClassVar[ParameterType]
    PARAMETER_TYPE_ACTOR: _ClassVar[ParameterType]
    PARAMETER_TYPE_BEHAVIOR: _ClassVar[ParameterType]
PARAMETER_TYPE_UNSPECIFIED: ParameterType
PARAMETER_TYPE_ACTOR: ParameterType
PARAMETER_TYPE_BEHAVIOR: ParameterType

class SpeedTarget(_message.Message):
    __slots__ = ["value", "range", "speed_reference"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    SPEED_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    value: float
    range: _comparison_pb2.DoubleRange
    speed_reference: SpeedReference
    def __init__(self, value: _Optional[float] = ..., range: _Optional[_Union[_comparison_pb2.DoubleRange, _Mapping]] = ..., speed_reference: _Optional[_Union[SpeedReference, _Mapping]] = ...) -> None: ...

class SpeedReference(_message.Message):
    __slots__ = ["reference_actor_id", "speed_comparison", "reference_sampling_mode", "rule"]
    REFERENCE_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SPEED_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SAMPLING_MODE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    reference_actor_id: str
    speed_comparison: _comparison_pb2.SpeedComparison
    reference_sampling_mode: _comparison_pb2.ReferenceSamplingMode
    rule: _comparison_pb2.ComparisonRule
    def __init__(self, reference_actor_id: _Optional[str] = ..., speed_comparison: _Optional[_Union[_comparison_pb2.SpeedComparison, str]] = ..., reference_sampling_mode: _Optional[_Union[_comparison_pb2.ReferenceSamplingMode, str]] = ..., rule: _Optional[_Union[_comparison_pb2.ComparisonRule, str]] = ...) -> None: ...

class LaneChangeTarget(_message.Message):
    __slots__ = ["value", "range", "lane_reference"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    LANE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    value: int
    range: _comparison_pb2.Int32Range
    lane_reference: LaneReference
    def __init__(self, value: _Optional[int] = ..., range: _Optional[_Union[_comparison_pb2.Int32Range, _Mapping]] = ..., lane_reference: _Optional[_Union[LaneReference, _Mapping]] = ...) -> None: ...

class LaneReference(_message.Message):
    __slots__ = ["reference_actor_id", "lane_comparison"]
    REFERENCE_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    LANE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    reference_actor_id: str
    lane_comparison: _comparison_pb2.LaneComparison
    def __init__(self, reference_actor_id: _Optional[str] = ..., lane_comparison: _Optional[_Union[_comparison_pb2.LaneComparison, str]] = ...) -> None: ...

class LateralOffsetTarget(_message.Message):
    __slots__ = ["offset_value"]
    OFFSET_VALUE_FIELD_NUMBER: _ClassVar[int]
    offset_value: float
    def __init__(self, offset_value: _Optional[float] = ...) -> None: ...

class DistanceTarget(_message.Message):
    __slots__ = ["distance_dimension_type", "distance_reference", "distance_type", "value", "range"]
    DISTANCE_DIMENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    distance_dimension_type: _comparison_pb2.DistanceDimensionType
    distance_reference: DistanceReference
    distance_type: _comparison_pb2.DistanceType
    value: float
    range: _comparison_pb2.DoubleRange
    def __init__(self, distance_dimension_type: _Optional[_Union[_comparison_pb2.DistanceDimensionType, str]] = ..., distance_reference: _Optional[_Union[DistanceReference, _Mapping]] = ..., distance_type: _Optional[_Union[_comparison_pb2.DistanceType, str]] = ..., value: _Optional[float] = ..., range: _Optional[_Union[_comparison_pb2.DoubleRange, _Mapping]] = ...) -> None: ...

class DistanceReference(_message.Message):
    __slots__ = ["actor_coordinate_system_type", "position_comparison", "measure_from", "rule", "point", "reference_actor_id"]
    ACTOR_COORDINATE_SYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    MEASURE_FROM_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    actor_coordinate_system_type: _comparison_pb2.ActorCoordinateSystemType
    position_comparison: _comparison_pb2.PositionComparison
    measure_from: _comparison_pb2.MeasureFrom
    rule: _comparison_pb2.DistanceComparison
    point: _geometry_pb2.Vector3
    reference_actor_id: str
    def __init__(self, actor_coordinate_system_type: _Optional[_Union[_comparison_pb2.ActorCoordinateSystemType, str]] = ..., position_comparison: _Optional[_Union[_comparison_pb2.PositionComparison, str]] = ..., measure_from: _Optional[_Union[_comparison_pb2.MeasureFrom, str]] = ..., rule: _Optional[_Union[_comparison_pb2.DistanceComparison, str]] = ..., point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., reference_actor_id: _Optional[str] = ...) -> None: ...

class ParameterReference(_message.Message):
    __slots__ = ["actor_id", "parameter_type", "parameter_name"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    parameter_type: ParameterType
    parameter_name: str
    def __init__(self, actor_id: _Optional[str] = ..., parameter_type: _Optional[_Union[ParameterType, str]] = ..., parameter_name: _Optional[str] = ...) -> None: ...
