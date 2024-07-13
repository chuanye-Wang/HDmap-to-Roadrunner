from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReferenceSamplingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFERENCE_SAMPLING_MODE_UNSPECIFIED: _ClassVar[ReferenceSamplingMode]
    REFERENCE_SAMPLING_MODE_AT_ACTION_START: _ClassVar[ReferenceSamplingMode]
    REFERENCE_SAMPLING_MODE_CONTINUOUS: _ClassVar[ReferenceSamplingMode]

class SpeedComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SPEED_COMPARISON_UNSPECIFIED: _ClassVar[SpeedComparison]
    SPEED_COMPARISON_ABSOLUTE: _ClassVar[SpeedComparison]
    SPEED_COMPARISON_SAME_AS: _ClassVar[SpeedComparison]
    SPEED_COMPARISON_FASTER_THAN: _ClassVar[SpeedComparison]
    SPEED_COMPARISON_SLOWER_THAN: _ClassVar[SpeedComparison]
    SPEED_COMPARISON_FROM_PATH: _ClassVar[SpeedComparison]

class LaneComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LANE_COMPARISON_UNSPECIFIED: _ClassVar[LaneComparison]
    LANE_COMPARISON_SAME_AS: _ClassVar[LaneComparison]
    LANE_COMPARISON_LEFT_OF: _ClassVar[LaneComparison]
    LANE_COMPARISON_RIGHT_OF: _ClassVar[LaneComparison]

class LateralOffsetDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LATERAL_OFFSET_DIRECTION_UNSPECIFIED: _ClassVar[LateralOffsetDirection]
    LATERAL_OFFSET_DIRECTION_TO_LEFT: _ClassVar[LateralOffsetDirection]
    LATERAL_OFFSET_DIRECTION_TO_RIGHT: _ClassVar[LateralOffsetDirection]
    LATERAL_OFFSET_DIRECTION_TO_CENTER: _ClassVar[LateralOffsetDirection]

class PositionComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POSITION_COMPARISON_UNSPECIFIED: _ClassVar[PositionComparison]
    POSITION_COMPARISON_SAME_AS: _ClassVar[PositionComparison]
    POSITION_COMPARISON_AHEAD_OF: _ClassVar[PositionComparison]
    POSITION_COMPARISON_BEHIND: _ClassVar[PositionComparison]
    POSITION_COMPARISON_EITHER: _ClassVar[PositionComparison]

class DistanceComparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DISTANCE_COMPARISON_UNSPECIFIED: _ClassVar[DistanceComparison]
    DISTANCE_COMPARISON_GREATER_THAN: _ClassVar[DistanceComparison]
    DISTANCE_COMPARISON_LESS_THAN: _ClassVar[DistanceComparison]
    DISTANCE_COMPARISON_EQUAL_TO: _ClassVar[DistanceComparison]

class DistanceDimensionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DISTANCE_DIMENSION_TYPE_UNSPECIFIED: _ClassVar[DistanceDimensionType]
    DISTANCE_DIMENSION_TYPE_LONGITUDINAL: _ClassVar[DistanceDimensionType]
    DISTANCE_DIMENSION_TYPE_LATERAL: _ClassVar[DistanceDimensionType]
    DISTANCE_DIMENSION_TYPE_EUCLIDEAN: _ClassVar[DistanceDimensionType]

class DistanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DISTANCE_TYPE_UNSPECIFIED: _ClassVar[DistanceType]
    DISTANCE_TYPE_SPACE: _ClassVar[DistanceType]
    DISTANCE_TYPE_TIME: _ClassVar[DistanceType]

class MeasureFrom(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MEASURE_FROM_UNSPECIFIED: _ClassVar[MeasureFrom]
    MEASURE_FROM_BOUNDING_BOXES: _ClassVar[MeasureFrom]
    MEASURE_FROM_ORIGINS: _ClassVar[MeasureFrom]

class ActorCoordinateSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ACTOR_COORDINATE_SYSTEM_TYPE_UNSPECIFIED: _ClassVar[ActorCoordinateSystemType]
    ACTOR_COORDINATE_SYSTEM_TYPE_LANE: _ClassVar[ActorCoordinateSystemType]
    ACTOR_COORDINATE_SYSTEM_TYPE_POSE: _ClassVar[ActorCoordinateSystemType]

class ComparisonRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPARISON_RULE_UNSPECIFIED: _ClassVar[ComparisonRule]
    COMPARISON_RULE_EQUAL_TO: _ClassVar[ComparisonRule]
    COMPARISON_RULE_GREATER_THAN: _ClassVar[ComparisonRule]
    COMPARISON_RULE_LESS_THAN: _ClassVar[ComparisonRule]
    COMPARISON_RULE_GREATER_OR_EQUAL: _ClassVar[ComparisonRule]
    COMPARISON_RULE_LESS_OR_EQUAL: _ClassVar[ComparisonRule]
    COMPARISON_RULE_NOT_EQUAL_TO: _ClassVar[ComparisonRule]
REFERENCE_SAMPLING_MODE_UNSPECIFIED: ReferenceSamplingMode
REFERENCE_SAMPLING_MODE_AT_ACTION_START: ReferenceSamplingMode
REFERENCE_SAMPLING_MODE_CONTINUOUS: ReferenceSamplingMode
SPEED_COMPARISON_UNSPECIFIED: SpeedComparison
SPEED_COMPARISON_ABSOLUTE: SpeedComparison
SPEED_COMPARISON_SAME_AS: SpeedComparison
SPEED_COMPARISON_FASTER_THAN: SpeedComparison
SPEED_COMPARISON_SLOWER_THAN: SpeedComparison
SPEED_COMPARISON_FROM_PATH: SpeedComparison
LANE_COMPARISON_UNSPECIFIED: LaneComparison
LANE_COMPARISON_SAME_AS: LaneComparison
LANE_COMPARISON_LEFT_OF: LaneComparison
LANE_COMPARISON_RIGHT_OF: LaneComparison
LATERAL_OFFSET_DIRECTION_UNSPECIFIED: LateralOffsetDirection
LATERAL_OFFSET_DIRECTION_TO_LEFT: LateralOffsetDirection
LATERAL_OFFSET_DIRECTION_TO_RIGHT: LateralOffsetDirection
LATERAL_OFFSET_DIRECTION_TO_CENTER: LateralOffsetDirection
POSITION_COMPARISON_UNSPECIFIED: PositionComparison
POSITION_COMPARISON_SAME_AS: PositionComparison
POSITION_COMPARISON_AHEAD_OF: PositionComparison
POSITION_COMPARISON_BEHIND: PositionComparison
POSITION_COMPARISON_EITHER: PositionComparison
DISTANCE_COMPARISON_UNSPECIFIED: DistanceComparison
DISTANCE_COMPARISON_GREATER_THAN: DistanceComparison
DISTANCE_COMPARISON_LESS_THAN: DistanceComparison
DISTANCE_COMPARISON_EQUAL_TO: DistanceComparison
DISTANCE_DIMENSION_TYPE_UNSPECIFIED: DistanceDimensionType
DISTANCE_DIMENSION_TYPE_LONGITUDINAL: DistanceDimensionType
DISTANCE_DIMENSION_TYPE_LATERAL: DistanceDimensionType
DISTANCE_DIMENSION_TYPE_EUCLIDEAN: DistanceDimensionType
DISTANCE_TYPE_UNSPECIFIED: DistanceType
DISTANCE_TYPE_SPACE: DistanceType
DISTANCE_TYPE_TIME: DistanceType
MEASURE_FROM_UNSPECIFIED: MeasureFrom
MEASURE_FROM_BOUNDING_BOXES: MeasureFrom
MEASURE_FROM_ORIGINS: MeasureFrom
ACTOR_COORDINATE_SYSTEM_TYPE_UNSPECIFIED: ActorCoordinateSystemType
ACTOR_COORDINATE_SYSTEM_TYPE_LANE: ActorCoordinateSystemType
ACTOR_COORDINATE_SYSTEM_TYPE_POSE: ActorCoordinateSystemType
COMPARISON_RULE_UNSPECIFIED: ComparisonRule
COMPARISON_RULE_EQUAL_TO: ComparisonRule
COMPARISON_RULE_GREATER_THAN: ComparisonRule
COMPARISON_RULE_LESS_THAN: ComparisonRule
COMPARISON_RULE_GREATER_OR_EQUAL: ComparisonRule
COMPARISON_RULE_LESS_OR_EQUAL: ComparisonRule
COMPARISON_RULE_NOT_EQUAL_TO: ComparisonRule

class DoubleRange(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ...) -> None: ...

class Int32Range(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
