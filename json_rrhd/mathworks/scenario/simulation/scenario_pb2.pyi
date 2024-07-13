from mathworks.scenario.simulation import action_pb2 as _action_pb2
from mathworks.scenario.simulation import condition_pb2 as _condition_pb2
from mathworks.scenario.simulation import custom_command_pb2 as _custom_command_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActorCreationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ACTOR_CREATION_MODE_UNSPECIFIED: _ClassVar[ActorCreationMode]
    ACTOR_CREATION_MODE_AUTOMATIC: _ClassVar[ActorCreationMode]
    ACTOR_CREATION_MODE_CREATE: _ClassVar[ActorCreationMode]
    ACTOR_CREATION_MODE_NO_CREATE: _ClassVar[ActorCreationMode]
ACTOR_CREATION_MODE_UNSPECIFIED: ActorCreationMode
ACTOR_CREATION_MODE_AUTOMATIC: ActorCreationMode
ACTOR_CREATION_MODE_CREATE: ActorCreationMode
ACTOR_CREATION_MODE_NO_CREATE: ActorCreationMode

class Scenario(_message.Message):
    __slots__ = ["root_phase", "custom_events", "custom_actions"]
    ROOT_PHASE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    root_phase: Phase
    custom_events: _containers.RepeatedCompositeFieldContainer[_custom_command_pb2.CustomCommand]
    custom_actions: _containers.RepeatedCompositeFieldContainer[_custom_command_pb2.CustomCommand]
    def __init__(self, root_phase: _Optional[_Union[Phase, _Mapping]] = ..., custom_events: _Optional[_Iterable[_Union[_custom_command_pb2.CustomCommand, _Mapping]]] = ..., custom_actions: _Optional[_Iterable[_Union[_custom_command_pb2.CustomCommand, _Mapping]]] = ...) -> None: ...

class Phase(_message.Message):
    __slots__ = ["id", "name", "start_condition", "end_condition", "system_actions", "composite_phase", "action_phase"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_CONDITION_FIELD_NUMBER: _ClassVar[int]
    END_CONDITION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_PHASE_FIELD_NUMBER: _ClassVar[int]
    ACTION_PHASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    start_condition: _condition_pb2.Condition
    end_condition: _condition_pb2.Condition
    system_actions: _containers.RepeatedCompositeFieldContainer[Phase]
    composite_phase: CompositePhase
    action_phase: ActionPhase
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., start_condition: _Optional[_Union[_condition_pb2.Condition, _Mapping]] = ..., end_condition: _Optional[_Union[_condition_pb2.Condition, _Mapping]] = ..., system_actions: _Optional[_Iterable[_Union[Phase, _Mapping]]] = ..., composite_phase: _Optional[_Union[CompositePhase, _Mapping]] = ..., action_phase: _Optional[_Union[ActionPhase, _Mapping]] = ...) -> None: ...

class CompositePhase(_message.Message):
    __slots__ = ["children", "serial_phase", "mix_phase"]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    SERIAL_PHASE_FIELD_NUMBER: _ClassVar[int]
    MIX_PHASE_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[Phase]
    serial_phase: SerialPhase
    mix_phase: MixPhase
    def __init__(self, children: _Optional[_Iterable[_Union[Phase, _Mapping]]] = ..., serial_phase: _Optional[_Union[SerialPhase, _Mapping]] = ..., mix_phase: _Optional[_Union[MixPhase, _Mapping]] = ...) -> None: ...

class SerialPhase(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MixPhase(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionPhase(_message.Message):
    __slots__ = ["actions", "actor_action_phase", "system_action_phase"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ACTION_PHASE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ACTION_PHASE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    actor_action_phase: ActorActionPhase
    system_action_phase: SystemActionPhase
    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., actor_action_phase: _Optional[_Union[ActorActionPhase, _Mapping]] = ..., system_action_phase: _Optional[_Union[SystemActionPhase, _Mapping]] = ...) -> None: ...

class ActorActionPhase(_message.Message):
    __slots__ = ["actor_id", "creation_mode"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_MODE_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    creation_mode: ActorCreationMode
    def __init__(self, actor_id: _Optional[str] = ..., creation_mode: _Optional[_Union[ActorCreationMode, str]] = ...) -> None: ...

class SystemActionPhase(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
