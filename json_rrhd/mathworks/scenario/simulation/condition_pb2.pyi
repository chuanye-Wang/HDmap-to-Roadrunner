from mathworks.scenario.simulation import comparison_pb2 as _comparison_pb2
from mathworks.scenario.simulation import phase_status_pb2 as _phase_status_pb2
from mathworks.scenario.simulation import targets_pb2 as _targets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ["id", "composite_condition", "singular_condition"]
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SINGULAR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    composite_condition: CompositeCondition
    singular_condition: SingularCondition
    def __init__(self, id: _Optional[str] = ..., composite_condition: _Optional[_Union[CompositeCondition, _Mapping]] = ..., singular_condition: _Optional[_Union[SingularCondition, _Mapping]] = ...) -> None: ...

class CompositeCondition(_message.Message):
    __slots__ = ["or_condition", "and_condition", "operands"]
    OR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    AND_CONDITION_FIELD_NUMBER: _ClassVar[int]
    OPERANDS_FIELD_NUMBER: _ClassVar[int]
    or_condition: OrCondition
    and_condition: AndCondition
    operands: _containers.RepeatedCompositeFieldContainer[Condition]
    def __init__(self, or_condition: _Optional[_Union[OrCondition, _Mapping]] = ..., and_condition: _Optional[_Union[AndCondition, _Mapping]] = ..., operands: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...

class OrCondition(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AndCondition(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SingularCondition(_message.Message):
    __slots__ = ["actor_speed_condition", "distance_condition", "collision_condition", "duration_condition", "phase_state_condition", "simulation_time_condition", "event_condition", "parameter_condition", "actions_complete_condition", "time_to_actor_condition"]
    ACTOR_SPEED_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    COLLISION_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DURATION_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PHASE_STATE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_TIME_CONDITION_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_COMPLETE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_ACTOR_CONDITION_FIELD_NUMBER: _ClassVar[int]
    actor_speed_condition: ActorSpeedCondition
    distance_condition: DistanceCondition
    collision_condition: CollisionCondition
    duration_condition: DurationCondition
    phase_state_condition: PhaseStateCondition
    simulation_time_condition: SimulationTimeCondition
    event_condition: EventCondition
    parameter_condition: ParameterCondition
    actions_complete_condition: ActionsCompleteCondition
    time_to_actor_condition: TimeToActorCondition
    def __init__(self, actor_speed_condition: _Optional[_Union[ActorSpeedCondition, _Mapping]] = ..., distance_condition: _Optional[_Union[DistanceCondition, _Mapping]] = ..., collision_condition: _Optional[_Union[CollisionCondition, _Mapping]] = ..., duration_condition: _Optional[_Union[DurationCondition, _Mapping]] = ..., phase_state_condition: _Optional[_Union[PhaseStateCondition, _Mapping]] = ..., simulation_time_condition: _Optional[_Union[SimulationTimeCondition, _Mapping]] = ..., event_condition: _Optional[_Union[EventCondition, _Mapping]] = ..., parameter_condition: _Optional[_Union[ParameterCondition, _Mapping]] = ..., actions_complete_condition: _Optional[_Union[ActionsCompleteCondition, _Mapping]] = ..., time_to_actor_condition: _Optional[_Union[TimeToActorCondition, _Mapping]] = ...) -> None: ...

class ActorSpeedCondition(_message.Message):
    __slots__ = ["actor_id", "speed_target"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SPEED_TARGET_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    speed_target: _targets_pb2.SpeedTarget
    def __init__(self, actor_id: _Optional[str] = ..., speed_target: _Optional[_Union[_targets_pb2.SpeedTarget, _Mapping]] = ...) -> None: ...

class DistanceCondition(_message.Message):
    __slots__ = ["actor_id", "distance_target"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TARGET_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    distance_target: _targets_pb2.DistanceTarget
    def __init__(self, actor_id: _Optional[str] = ..., distance_target: _Optional[_Union[_targets_pb2.DistanceTarget, _Mapping]] = ...) -> None: ...

class CollisionCondition(_message.Message):
    __slots__ = ["actor_ids", "reference_actor_ids"]
    ACTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ACTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    actor_ids: _containers.RepeatedScalarFieldContainer[str]
    reference_actor_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, actor_ids: _Optional[_Iterable[str]] = ..., reference_actor_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DurationCondition(_message.Message):
    __slots__ = ["duration_time"]
    DURATION_TIME_FIELD_NUMBER: _ClassVar[int]
    duration_time: float
    def __init__(self, duration_time: _Optional[float] = ...) -> None: ...

class PhaseStateCondition(_message.Message):
    __slots__ = ["phase_id", "phase_state"]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_STATE_FIELD_NUMBER: _ClassVar[int]
    phase_id: str
    phase_state: _phase_status_pb2.PhaseState
    def __init__(self, phase_id: _Optional[str] = ..., phase_state: _Optional[_Union[_phase_status_pb2.PhaseState, str]] = ...) -> None: ...

class SimulationTimeCondition(_message.Message):
    __slots__ = ["time"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: float
    def __init__(self, time: _Optional[float] = ...) -> None: ...

class EventCondition(_message.Message):
    __slots__ = ["event_name", "parameter_conditions"]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    parameter_conditions: _containers.RepeatedCompositeFieldContainer[ParameterCondition]
    def __init__(self, event_name: _Optional[str] = ..., parameter_conditions: _Optional[_Iterable[_Union[ParameterCondition, _Mapping]]] = ...) -> None: ...

class ParameterCondition(_message.Message):
    __slots__ = ["parameter_reference", "rule", "compared_parameter_value"]
    PARAMETER_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    COMPARED_PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    parameter_reference: _targets_pb2.ParameterReference
    rule: _comparison_pb2.ComparisonRule
    compared_parameter_value: str
    def __init__(self, parameter_reference: _Optional[_Union[_targets_pb2.ParameterReference, _Mapping]] = ..., rule: _Optional[_Union[_comparison_pb2.ComparisonRule, str]] = ..., compared_parameter_value: _Optional[str] = ...) -> None: ...

class ActionsCompleteCondition(_message.Message):
    __slots__ = ["phase_id"]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    phase_id: str
    def __init__(self, phase_id: _Optional[str] = ...) -> None: ...

class TimeToActorCondition(_message.Message):
    __slots__ = ["actor_id", "distance_target"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_TARGET_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    distance_target: _targets_pb2.DistanceTarget
    def __init__(self, actor_id: _Optional[str] = ..., distance_target: _Optional[_Union[_targets_pb2.DistanceTarget, _Mapping]] = ...) -> None: ...
