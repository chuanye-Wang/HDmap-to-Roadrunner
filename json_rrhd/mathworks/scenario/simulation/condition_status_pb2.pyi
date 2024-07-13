from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConditionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONDITION_STATE_UNSPECIFIED: _ClassVar[ConditionState]
    CONDITION_STATE_NOT_YET_EVALUATED: _ClassVar[ConditionState]
    CONDITION_STATE_UNSATISFIED: _ClassVar[ConditionState]
    CONDITION_STATE_SATISFIED: _ClassVar[ConditionState]
CONDITION_STATE_UNSPECIFIED: ConditionState
CONDITION_STATE_NOT_YET_EVALUATED: ConditionState
CONDITION_STATE_UNSATISFIED: ConditionState
CONDITION_STATE_SATISFIED: ConditionState

class ConditionStatus(_message.Message):
    __slots__ = ["id", "condition_state", "duration_conditon_status", "simulation_time_condition_status", "distance_condition_status", "actor_speed_condition_status", "collision_condition_status", "actor_lane_condition_status", "or_condition_status", "lateral_offset_condition_status", "phase_state_condition_status", "and_condition_status", "event_condition_status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_STATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_CONDITON_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_TIME_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_SPEED_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    COLLISION_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_LANE_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    OR_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    LATERAL_OFFSET_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    PHASE_STATE_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    AND_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    condition_state: ConditionState
    duration_conditon_status: DurationConditionStatus
    simulation_time_condition_status: SimulationTimeConditionStatus
    distance_condition_status: DistanceConditionStatus
    actor_speed_condition_status: ActorSpeedConditionStatus
    collision_condition_status: CollisionConditionStatus
    actor_lane_condition_status: ActorLaneConditionStatus
    or_condition_status: OrConditionStatus
    lateral_offset_condition_status: LateralOffsetConditionStatus
    phase_state_condition_status: PhaseStateConditionStatus
    and_condition_status: AndConditionStatus
    event_condition_status: EventConditionStatus
    def __init__(self, id: _Optional[str] = ..., condition_state: _Optional[_Union[ConditionState, str]] = ..., duration_conditon_status: _Optional[_Union[DurationConditionStatus, _Mapping]] = ..., simulation_time_condition_status: _Optional[_Union[SimulationTimeConditionStatus, _Mapping]] = ..., distance_condition_status: _Optional[_Union[DistanceConditionStatus, _Mapping]] = ..., actor_speed_condition_status: _Optional[_Union[ActorSpeedConditionStatus, _Mapping]] = ..., collision_condition_status: _Optional[_Union[CollisionConditionStatus, _Mapping]] = ..., actor_lane_condition_status: _Optional[_Union[ActorLaneConditionStatus, _Mapping]] = ..., or_condition_status: _Optional[_Union[OrConditionStatus, _Mapping]] = ..., lateral_offset_condition_status: _Optional[_Union[LateralOffsetConditionStatus, _Mapping]] = ..., phase_state_condition_status: _Optional[_Union[PhaseStateConditionStatus, _Mapping]] = ..., and_condition_status: _Optional[_Union[AndConditionStatus, _Mapping]] = ..., event_condition_status: _Optional[_Union[EventConditionStatus, _Mapping]] = ...) -> None: ...

class DurationConditionStatus(_message.Message):
    __slots__ = ["elapsed_time"]
    ELAPSED_TIME_FIELD_NUMBER: _ClassVar[int]
    elapsed_time: float
    def __init__(self, elapsed_time: _Optional[float] = ...) -> None: ...

class SimulationTimeConditionStatus(_message.Message):
    __slots__ = ["simulation_time"]
    SIMULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    simulation_time: float
    def __init__(self, simulation_time: _Optional[float] = ...) -> None: ...

class DistanceConditionStatus(_message.Message):
    __slots__ = ["distance", "actor_point", "reference_object_point"]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_POINT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_OBJECT_POINT_FIELD_NUMBER: _ClassVar[int]
    distance: float
    actor_point: _geometry_pb2.Vector3
    reference_object_point: _geometry_pb2.Vector3
    def __init__(self, distance: _Optional[float] = ..., actor_point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., reference_object_point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class ActorSpeedConditionStatus(_message.Message):
    __slots__ = ["actor_speed"]
    ACTOR_SPEED_FIELD_NUMBER: _ClassVar[int]
    actor_speed: float
    def __init__(self, actor_speed: _Optional[float] = ...) -> None: ...

class CollisionConditionStatus(_message.Message):
    __slots__ = ["collisions"]
    COLLISIONS_FIELD_NUMBER: _ClassVar[int]
    collisions: _containers.RepeatedCompositeFieldContainer[Collision]
    def __init__(self, collisions: _Optional[_Iterable[_Union[Collision, _Mapping]]] = ...) -> None: ...

class Collision(_message.Message):
    __slots__ = ["actor_id", "other_actor"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_ACTOR_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    other_actor: str
    def __init__(self, actor_id: _Optional[str] = ..., other_actor: _Optional[str] = ...) -> None: ...

class ActorLaneConditionStatus(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OrConditionStatus(_message.Message):
    __slots__ = ["operands_status"]
    OPERANDS_STATUS_FIELD_NUMBER: _ClassVar[int]
    operands_status: _containers.RepeatedCompositeFieldContainer[ConditionStatus]
    def __init__(self, operands_status: _Optional[_Iterable[_Union[ConditionStatus, _Mapping]]] = ...) -> None: ...

class LateralOffsetConditionStatus(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PhaseStateConditionStatus(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AndConditionStatus(_message.Message):
    __slots__ = ["operands_status"]
    OPERANDS_STATUS_FIELD_NUMBER: _ClassVar[int]
    operands_status: _containers.RepeatedCompositeFieldContainer[ConditionStatus]
    def __init__(self, operands_status: _Optional[_Iterable[_Union[ConditionStatus, _Mapping]]] = ...) -> None: ...

class EventConditionStatus(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
