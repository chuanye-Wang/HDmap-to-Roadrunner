from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicsDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DYNAMICS_DIMENSION_UNSPECIFIED: _ClassVar[DynamicsDimension]
    DYNAMICS_DIMENSION_RATE: _ClassVar[DynamicsDimension]
    DYNAMICS_DIMENSION_TIME: _ClassVar[DynamicsDimension]
    DYNAMICS_DIMENSION_DISTANCE: _ClassVar[DynamicsDimension]

class DynamicsShape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DYNAMICS_SHAPE_UNSPECIFIED: _ClassVar[DynamicsShape]
    DYNAMICS_SHAPE_LINEAR: _ClassVar[DynamicsShape]
    DYNAMICS_SHAPE_CUBIC: _ClassVar[DynamicsShape]
    DYNAMICS_SHAPE_STEP: _ClassVar[DynamicsShape]
DYNAMICS_DIMENSION_UNSPECIFIED: DynamicsDimension
DYNAMICS_DIMENSION_RATE: DynamicsDimension
DYNAMICS_DIMENSION_TIME: DynamicsDimension
DYNAMICS_DIMENSION_DISTANCE: DynamicsDimension
DYNAMICS_SHAPE_UNSPECIFIED: DynamicsShape
DYNAMICS_SHAPE_LINEAR: DynamicsShape
DYNAMICS_SHAPE_CUBIC: DynamicsShape
DYNAMICS_SHAPE_STEP: DynamicsShape

class TransitionDynamics(_message.Message):
    __slots__ = ["dimension", "shape", "value"]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    dimension: DynamicsDimension
    shape: DynamicsShape
    value: float
    def __init__(self, dimension: _Optional[_Union[DynamicsDimension, str]] = ..., shape: _Optional[_Union[DynamicsShape, str]] = ..., value: _Optional[float] = ...) -> None: ...

class TimeTransitionDynamics(_message.Message):
    __slots__ = ["shape", "time_value"]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    shape: DynamicsShape
    time_value: float
    def __init__(self, shape: _Optional[_Union[DynamicsShape, str]] = ..., time_value: _Optional[float] = ...) -> None: ...

class DynamicConstraints(_message.Message):
    __slots__ = ["dynamic_limit"]
    DYNAMIC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    dynamic_limit: DynamicLimit
    def __init__(self, dynamic_limit: _Optional[_Union[DynamicLimit, _Mapping]] = ...) -> None: ...

class DynamicLimit(_message.Message):
    __slots__ = ["max_speed", "max_acceleration", "max_deceleration"]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    MAX_ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DECELERATION_FIELD_NUMBER: _ClassVar[int]
    max_speed: float
    max_acceleration: float
    max_deceleration: float
    def __init__(self, max_speed: _Optional[float] = ..., max_acceleration: _Optional[float] = ..., max_deceleration: _Optional[float] = ...) -> None: ...
