from mathworks.scenario.simulation import action_pb2 as _action_pb2
from mathworks.scenario.simulation import actor_pb2 as _actor_pb2
from mathworks.scenario.simulation import custom_command_pb2 as _custom_command_pb2
from mathworks.scenario.simulation import scenario_pb2 as _scenario_pb2
from mathworks.scenario.simulation import simulation_settings_pb2 as _simulation_settings_pb2
from mathworks.scenario.simulation import simulation_status_pb2 as _simulation_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationStartMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIMULATION_START_MODE_UNSPECIFIED: _ClassVar[SimulationStartMode]
    SIMULATION_START_MODE_NORMAL: _ClassVar[SimulationStartMode]
    SIMULATION_START_MODE_REPLAY: _ClassVar[SimulationStartMode]
SIMULATION_START_MODE_UNSPECIFIED: SimulationStartMode
SIMULATION_START_MODE_NORMAL: SimulationStartMode
SIMULATION_START_MODE_REPLAY: SimulationStartMode

class Event(_message.Message):
    __slots__ = ["priority", "need_set_ready", "sender_id", "receiver_ids", "server_shutdown_event", "client_subscribed_event", "client_unsubscribed_event", "scene_changed_event", "scenario_changed_event", "simulation_settings_changed_event", "simulation_status_changed_event", "simulation_start_event", "simulation_stop_event", "simulation_step_event", "simulation_post_step_event", "scenario_update_event", "create_actor_event", "remove_actor_event", "action_event", "action_complete_event", "user_defined_event"]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    NEED_SET_READY_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_IDS_FIELD_NUMBER: _ClassVar[int]
    SERVER_SHUTDOWN_EVENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBSCRIBED_EVENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_UNSUBSCRIBED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCENE_CHANGED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_CHANGED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SETTINGS_CHANGED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_STATUS_CHANGED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_START_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_STOP_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_STEP_EVENT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_POST_STEP_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_UPDATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACTOR_EVENT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ACTOR_EVENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_COMPLETE_EVENT_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_EVENT_FIELD_NUMBER: _ClassVar[int]
    priority: int
    need_set_ready: bool
    sender_id: str
    receiver_ids: _containers.RepeatedScalarFieldContainer[str]
    server_shutdown_event: ServerShutdownEvent
    client_subscribed_event: ClientSubscribedEvent
    client_unsubscribed_event: ClientUnsubscribedEvent
    scene_changed_event: SceneChangedEvent
    scenario_changed_event: ScenarioChangedEvent
    simulation_settings_changed_event: SimulationSettingsChangedEvent
    simulation_status_changed_event: SimulationStatusChangedEvent
    simulation_start_event: SimulationStartEvent
    simulation_stop_event: SimulationStopEvent
    simulation_step_event: SimulationStepEvent
    simulation_post_step_event: SimulationPostStepEvent
    scenario_update_event: ScenarioUpdateEvent
    create_actor_event: CreateActorEvent
    remove_actor_event: WillRemoveActorEvent
    action_event: ActionEvent
    action_complete_event: ActionCompleteEvent
    user_defined_event: _custom_command_pb2.CustomCommand
    def __init__(self, priority: _Optional[int] = ..., need_set_ready: bool = ..., sender_id: _Optional[str] = ..., receiver_ids: _Optional[_Iterable[str]] = ..., server_shutdown_event: _Optional[_Union[ServerShutdownEvent, _Mapping]] = ..., client_subscribed_event: _Optional[_Union[ClientSubscribedEvent, _Mapping]] = ..., client_unsubscribed_event: _Optional[_Union[ClientUnsubscribedEvent, _Mapping]] = ..., scene_changed_event: _Optional[_Union[SceneChangedEvent, _Mapping]] = ..., scenario_changed_event: _Optional[_Union[ScenarioChangedEvent, _Mapping]] = ..., simulation_settings_changed_event: _Optional[_Union[SimulationSettingsChangedEvent, _Mapping]] = ..., simulation_status_changed_event: _Optional[_Union[SimulationStatusChangedEvent, _Mapping]] = ..., simulation_start_event: _Optional[_Union[SimulationStartEvent, _Mapping]] = ..., simulation_stop_event: _Optional[_Union[SimulationStopEvent, _Mapping]] = ..., simulation_step_event: _Optional[_Union[SimulationStepEvent, _Mapping]] = ..., simulation_post_step_event: _Optional[_Union[SimulationPostStepEvent, _Mapping]] = ..., scenario_update_event: _Optional[_Union[ScenarioUpdateEvent, _Mapping]] = ..., create_actor_event: _Optional[_Union[CreateActorEvent, _Mapping]] = ..., remove_actor_event: _Optional[_Union[WillRemoveActorEvent, _Mapping]] = ..., action_event: _Optional[_Union[ActionEvent, _Mapping]] = ..., action_complete_event: _Optional[_Union[ActionCompleteEvent, _Mapping]] = ..., user_defined_event: _Optional[_Union[_custom_command_pb2.CustomCommand, _Mapping]] = ...) -> None: ...

class ServerShutdownEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClientSubscribedEvent(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class ClientUnsubscribedEvent(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class SceneChangedEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ScenarioChangedEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulationSettingsChangedEvent(_message.Message):
    __slots__ = ["simulation_settings"]
    SIMULATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    simulation_settings: _simulation_settings_pb2.SimulationSettings
    def __init__(self, simulation_settings: _Optional[_Union[_simulation_settings_pb2.SimulationSettings, _Mapping]] = ...) -> None: ...

class SimulationStatusChangedEvent(_message.Message):
    __slots__ = ["simulation_status"]
    SIMULATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    simulation_status: _simulation_status_pb2.SimulationStatus
    def __init__(self, simulation_status: _Optional[_Union[_simulation_status_pb2.SimulationStatus, str]] = ...) -> None: ...

class SimulationStartEvent(_message.Message):
    __slots__ = ["simulation_mode"]
    SIMULATION_MODE_FIELD_NUMBER: _ClassVar[int]
    simulation_mode: SimulationStartMode
    def __init__(self, simulation_mode: _Optional[_Union[SimulationStartMode, str]] = ...) -> None: ...

class SimulationStopEvent(_message.Message):
    __slots__ = ["stop_time_seconds", "steps", "cause"]
    STOP_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    stop_time_seconds: float
    steps: int
    cause: _simulation_status_pb2.SimulationStopCause
    def __init__(self, stop_time_seconds: _Optional[float] = ..., steps: _Optional[int] = ..., cause: _Optional[_Union[_simulation_status_pb2.SimulationStopCause, _Mapping]] = ...) -> None: ...

class SimulationStepEvent(_message.Message):
    __slots__ = ["elapsed_time_seconds", "steps"]
    ELAPSED_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    elapsed_time_seconds: float
    steps: int
    def __init__(self, elapsed_time_seconds: _Optional[float] = ..., steps: _Optional[int] = ...) -> None: ...

class SimulationPostStepEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ScenarioUpdateEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateActorEvent(_message.Message):
    __slots__ = ["actor", "descendants", "initial_phase"]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    DESCENDANTS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_PHASE_FIELD_NUMBER: _ClassVar[int]
    actor: _actor_pb2.Actor
    descendants: _containers.RepeatedCompositeFieldContainer[_actor_pb2.Actor]
    initial_phase: _scenario_pb2.Phase
    def __init__(self, actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]] = ..., descendants: _Optional[_Iterable[_Union[_actor_pb2.Actor, _Mapping]]] = ..., initial_phase: _Optional[_Union[_scenario_pb2.Phase, _Mapping]] = ...) -> None: ...

class WillRemoveActorEvent(_message.Message):
    __slots__ = ["actor_id", "descendant_ids"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DESCENDANT_IDS_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    descendant_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, actor_id: _Optional[str] = ..., descendant_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ActionEvent(_message.Message):
    __slots__ = ["phase"]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    phase: _scenario_pb2.Phase
    def __init__(self, phase: _Optional[_Union[_scenario_pb2.Phase, _Mapping]] = ...) -> None: ...

class ActionCompleteEvent(_message.Message):
    __slots__ = ["action_id", "actor_id", "final_status"]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    actor_id: str
    final_status: _action_pb2.ActionEventStatus
    def __init__(self, action_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., final_status: _Optional[_Union[_action_pb2.ActionEventStatus, str]] = ...) -> None: ...
