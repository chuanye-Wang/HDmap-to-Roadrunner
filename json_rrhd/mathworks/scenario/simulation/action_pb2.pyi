from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.simulation import attributes_pb2 as _attributes_pb2
from mathworks.scenario.simulation import comparison_pb2 as _comparison_pb2
from mathworks.scenario.simulation import custom_command_pb2 as _custom_command_pb2
from mathworks.scenario.simulation import targets_pb2 as _targets_pb2
from mathworks.scenario.simulation import transition_dynamics_pb2 as _transition_dynamics_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhaseInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PHASE_INTERVAL_UNSPECIFIED: _ClassVar[PhaseInterval]
    PHASE_INTERVAL_AT_START: _ClassVar[PhaseInterval]
    PHASE_INTERVAL_AT_END: _ClassVar[PhaseInterval]
    PHASE_INTERVAL_INVARIANT: _ClassVar[PhaseInterval]

class ActionEventStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ACTION_EVENT_STATUS_UNSPECIFIED: _ClassVar[ActionEventStatus]
    ACTION_EVENT_STATUS_DISPATCHED: _ClassVar[ActionEventStatus]
    ACTION_EVENT_STATUS_INTERRUPTED: _ClassVar[ActionEventStatus]
    ACTION_EVENT_STATUS_SKIPPED: _ClassVar[ActionEventStatus]
    ACTION_EVENT_STATUS_DONE: _ClassVar[ActionEventStatus]
PHASE_INTERVAL_UNSPECIFIED: PhaseInterval
PHASE_INTERVAL_AT_START: PhaseInterval
PHASE_INTERVAL_AT_END: PhaseInterval
PHASE_INTERVAL_INVARIANT: PhaseInterval
ACTION_EVENT_STATUS_UNSPECIFIED: ActionEventStatus
ACTION_EVENT_STATUS_DISPATCHED: ActionEventStatus
ACTION_EVENT_STATUS_INTERRUPTED: ActionEventStatus
ACTION_EVENT_STATUS_SKIPPED: ActionEventStatus
ACTION_EVENT_STATUS_DONE: ActionEventStatus

class Action(_message.Message):
    __slots__ = ["id", "actor_action", "system_action"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ACTION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ACTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    actor_action: ActorAction
    system_action: SystemAction
    def __init__(self, id: _Optional[str] = ..., actor_action: _Optional[_Union[ActorAction, _Mapping]] = ..., system_action: _Optional[_Union[SystemAction, _Mapping]] = ...) -> None: ...

class ActorAction(_message.Message):
    __slots__ = ["actor_id", "phase_interval", "lane_change_action", "path_action", "position_action", "speed_action", "change_parameter_action", "lateral_offset_action", "longitudinal_distance_action", "user_defined_action", "remove_actor_action"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    LANE_CHANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    PATH_ACTION_FIELD_NUMBER: _ClassVar[int]
    POSITION_ACTION_FIELD_NUMBER: _ClassVar[int]
    SPEED_ACTION_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PARAMETER_ACTION_FIELD_NUMBER: _ClassVar[int]
    LATERAL_OFFSET_ACTION_FIELD_NUMBER: _ClassVar[int]
    LONGITUDINAL_DISTANCE_ACTION_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_ACTION_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ACTOR_ACTION_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    phase_interval: PhaseInterval
    lane_change_action: LaneChangeAction
    path_action: PathAction
    position_action: PositionAction
    speed_action: SpeedAction
    change_parameter_action: ChangeParameterAction
    lateral_offset_action: LateralOffsetAction
    longitudinal_distance_action: LongitudinalDistanceAction
    user_defined_action: UserDefinedAction
    remove_actor_action: RemoveActorAction
    def __init__(self, actor_id: _Optional[str] = ..., phase_interval: _Optional[_Union[PhaseInterval, str]] = ..., lane_change_action: _Optional[_Union[LaneChangeAction, _Mapping]] = ..., path_action: _Optional[_Union[PathAction, _Mapping]] = ..., position_action: _Optional[_Union[PositionAction, _Mapping]] = ..., speed_action: _Optional[_Union[SpeedAction, _Mapping]] = ..., change_parameter_action: _Optional[_Union[ChangeParameterAction, _Mapping]] = ..., lateral_offset_action: _Optional[_Union[LateralOffsetAction, _Mapping]] = ..., longitudinal_distance_action: _Optional[_Union[LongitudinalDistanceAction, _Mapping]] = ..., user_defined_action: _Optional[_Union[UserDefinedAction, _Mapping]] = ..., remove_actor_action: _Optional[_Union[RemoveActorAction, _Mapping]] = ...) -> None: ...

class SpeedAction(_message.Message):
    __slots__ = ["speed_target", "transition_dynamics", "allow_negative_speed"]
    SPEED_TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_DYNAMICS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NEGATIVE_SPEED_FIELD_NUMBER: _ClassVar[int]
    speed_target: _targets_pb2.SpeedTarget
    transition_dynamics: _transition_dynamics_pb2.TransitionDynamics
    allow_negative_speed: bool
    def __init__(self, speed_target: _Optional[_Union[_targets_pb2.SpeedTarget, _Mapping]] = ..., transition_dynamics: _Optional[_Union[_transition_dynamics_pb2.TransitionDynamics, _Mapping]] = ..., allow_negative_speed: bool = ...) -> None: ...

class LaneChangeAction(_message.Message):
    __slots__ = ["lane_change_target", "transition_dynamics"]
    LANE_CHANGE_TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_DYNAMICS_FIELD_NUMBER: _ClassVar[int]
    lane_change_target: _targets_pb2.LaneChangeTarget
    transition_dynamics: _transition_dynamics_pb2.TransitionDynamics
    def __init__(self, lane_change_target: _Optional[_Union[_targets_pb2.LaneChangeTarget, _Mapping]] = ..., transition_dynamics: _Optional[_Union[_transition_dynamics_pb2.TransitionDynamics, _Mapping]] = ...) -> None: ...

class PositionAction(_message.Message):
    __slots__ = ["value", "range", "position_reference"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    value: float
    range: _comparison_pb2.DoubleRange
    position_reference: PositionReference
    def __init__(self, value: _Optional[float] = ..., range: _Optional[_Union[_comparison_pb2.DoubleRange, _Mapping]] = ..., position_reference: _Optional[_Union[PositionReference, _Mapping]] = ...) -> None: ...

class PositionReference(_message.Message):
    __slots__ = ["reference_actor_id", "position_comparison"]
    REFERENCE_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    reference_actor_id: str
    position_comparison: _comparison_pb2.PositionComparison
    def __init__(self, reference_actor_id: _Optional[str] = ..., position_comparison: _Optional[_Union[_comparison_pb2.PositionComparison, str]] = ...) -> None: ...

class PathPointTiming(_message.Message):
    __slots__ = ["time", "speed", "wait_time"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    time: float
    speed: float
    wait_time: float
    def __init__(self, time: _Optional[float] = ..., speed: _Optional[float] = ..., wait_time: _Optional[float] = ...) -> None: ...

class PathAction(_message.Message):
    __slots__ = ["path", "actor_id", "timings", "actor_orientations"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TIMINGS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ORIENTATIONS_FIELD_NUMBER: _ClassVar[int]
    path: _geometry_pb2.Path
    actor_id: str
    timings: _containers.RepeatedCompositeFieldContainer[PathPointTiming]
    actor_orientations: _containers.RepeatedCompositeFieldContainer[_geometry_pb2.Orientation]
    def __init__(self, path: _Optional[_Union[_geometry_pb2.Path, _Mapping]] = ..., actor_id: _Optional[str] = ..., timings: _Optional[_Iterable[_Union[PathPointTiming, _Mapping]]] = ..., actor_orientations: _Optional[_Iterable[_Union[_geometry_pb2.Orientation, _Mapping]]] = ...) -> None: ...

class ChangeParameterAction(_message.Message):
    __slots__ = ["parameter", "parameter_type"]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    parameter: _attributes_pb2.Attribute
    parameter_type: _targets_pb2.ParameterType
    def __init__(self, parameter: _Optional[_Union[_attributes_pb2.Attribute, _Mapping]] = ..., parameter_type: _Optional[_Union[_targets_pb2.ParameterType, str]] = ...) -> None: ...

class LateralOffsetAction(_message.Message):
    __slots__ = ["lateral_offset_target", "transition_dynamics"]
    LATERAL_OFFSET_TARGET_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_DYNAMICS_FIELD_NUMBER: _ClassVar[int]
    lateral_offset_target: _targets_pb2.LateralOffsetTarget
    transition_dynamics: _transition_dynamics_pb2.TimeTransitionDynamics
    def __init__(self, lateral_offset_target: _Optional[_Union[_targets_pb2.LateralOffsetTarget, _Mapping]] = ..., transition_dynamics: _Optional[_Union[_transition_dynamics_pb2.TimeTransitionDynamics, _Mapping]] = ...) -> None: ...

class LongitudinalDistanceAction(_message.Message):
    __slots__ = ["distance_target", "reference_sampling_mode", "dynamic_constraints"]
    DISTANCE_TARGET_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SAMPLING_MODE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    distance_target: _targets_pb2.DistanceTarget
    reference_sampling_mode: _comparison_pb2.ReferenceSamplingMode
    dynamic_constraints: _transition_dynamics_pb2.DynamicConstraints
    def __init__(self, distance_target: _Optional[_Union[_targets_pb2.DistanceTarget, _Mapping]] = ..., reference_sampling_mode: _Optional[_Union[_comparison_pb2.ReferenceSamplingMode, str]] = ..., dynamic_constraints: _Optional[_Union[_transition_dynamics_pb2.DynamicConstraints, _Mapping]] = ...) -> None: ...

class UserDefinedAction(_message.Message):
    __slots__ = ["custom_command", "instantaneous"]
    CUSTOM_COMMAND_FIELD_NUMBER: _ClassVar[int]
    INSTANTANEOUS_FIELD_NUMBER: _ClassVar[int]
    custom_command: _custom_command_pb2.CustomCommand
    instantaneous: bool
    def __init__(self, custom_command: _Optional[_Union[_custom_command_pb2.CustomCommand, _Mapping]] = ..., instantaneous: bool = ...) -> None: ...

class RemoveActorAction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SystemAction(_message.Message):
    __slots__ = ["scenario_success", "scenario_failure", "wait_action", "send_event_action"]
    SCENARIO_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FAILURE_FIELD_NUMBER: _ClassVar[int]
    WAIT_ACTION_FIELD_NUMBER: _ClassVar[int]
    SEND_EVENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    scenario_success: ScenarioSuccess
    scenario_failure: ScenarioFailure
    wait_action: WaitAction
    send_event_action: SendEventAction
    def __init__(self, scenario_success: _Optional[_Union[ScenarioSuccess, _Mapping]] = ..., scenario_failure: _Optional[_Union[ScenarioFailure, _Mapping]] = ..., wait_action: _Optional[_Union[WaitAction, _Mapping]] = ..., send_event_action: _Optional[_Union[SendEventAction, _Mapping]] = ...) -> None: ...

class ScenarioSuccess(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ScenarioFailure(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WaitAction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendEventAction(_message.Message):
    __slots__ = ["custom_command"]
    CUSTOM_COMMAND_FIELD_NUMBER: _ClassVar[int]
    custom_command: _custom_command_pb2.CustomCommand
    def __init__(self, custom_command: _Optional[_Union[_custom_command_pb2.CustomCommand, _Mapping]] = ...) -> None: ...
