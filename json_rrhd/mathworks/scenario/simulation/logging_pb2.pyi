from mathworks.scenario.simulation import actor_pb2 as _actor_pb2
from mathworks.scenario.simulation import event_pb2 as _event_pb2
from mathworks.scenario.simulation import simulation_settings_pb2 as _simulation_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiagnosticType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_TYPE: _ClassVar[DiagnosticType]
    INFORMATION_TYPE: _ClassVar[DiagnosticType]
    WARNING_TYPE: _ClassVar[DiagnosticType]
    ERROR_TYPE: _ClassVar[DiagnosticType]
UNKNOWN_TYPE: DiagnosticType
INFORMATION_TYPE: DiagnosticType
WARNING_TYPE: DiagnosticType
ERROR_TYPE: DiagnosticType

class Timestamp(_message.Message):
    __slots__ = ["seconds", "nanos"]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class TimeStamp(_message.Message):
    __slots__ = ["simulation_time", "wall_clock_time"]
    SIMULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    WALL_CLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    simulation_time: float
    wall_clock_time: Timestamp
    def __init__(self, simulation_time: _Optional[float] = ..., wall_clock_time: _Optional[_Union[Timestamp, _Mapping]] = ...) -> None: ...

class CommunicationLog(_message.Message):
    __slots__ = ["communication_log"]
    COMMUNICATION_LOG_FIELD_NUMBER: _ClassVar[int]
    communication_log: _containers.RepeatedCompositeFieldContainer[Communication]
    def __init__(self, communication_log: _Optional[_Iterable[_Union[Communication, _Mapping]]] = ...) -> None: ...

class Communication(_message.Message):
    __slots__ = ["time_stamp", "rpc_call", "published_message"]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    RPC_CALL_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    time_stamp: TimeStamp
    rpc_call: RemoteProcedureCall
    published_message: PublishMessage
    def __init__(self, time_stamp: _Optional[_Union[TimeStamp, _Mapping]] = ..., rpc_call: _Optional[_Union[RemoteProcedureCall, _Mapping]] = ..., published_message: _Optional[_Union[PublishMessage, _Mapping]] = ...) -> None: ...

class RemoteProcedureCall(_message.Message):
    __slots__ = ["client_id", "service_name", "success"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    service_name: str
    success: bool
    def __init__(self, client_id: _Optional[str] = ..., service_name: _Optional[str] = ..., success: bool = ...) -> None: ...

class PublishMessage(_message.Message):
    __slots__ = ["message_type"]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    message_type: str
    def __init__(self, message_type: _Optional[str] = ...) -> None: ...

class WorldRuntimeStateLog(_message.Message):
    __slots__ = ["world_states", "simulation_settings"]
    WORLD_STATES_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    world_states: _containers.RepeatedCompositeFieldContainer[WorldRuntimeState]
    simulation_settings: _simulation_settings_pb2.SimulationSettings
    def __init__(self, world_states: _Optional[_Iterable[_Union[WorldRuntimeState, _Mapping]]] = ..., simulation_settings: _Optional[_Union[_simulation_settings_pb2.SimulationSettings, _Mapping]] = ...) -> None: ...

class WorldRuntimeState(_message.Message):
    __slots__ = ["time_stamp", "actor_runtimes", "simulation_events"]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    ACTOR_RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    time_stamp: TimeStamp
    actor_runtimes: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRuntime]
    simulation_events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    def __init__(self, time_stamp: _Optional[_Union[TimeStamp, _Mapping]] = ..., actor_runtimes: _Optional[_Iterable[_Union[_actor_pb2.ActorRuntime, _Mapping]]] = ..., simulation_events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ...) -> None: ...

class DiagnosticMessageLog(_message.Message):
    __slots__ = ["diagnostic_messages"]
    DIAGNOSTIC_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    diagnostic_messages: _containers.RepeatedCompositeFieldContainer[DiagnosticMessage]
    def __init__(self, diagnostic_messages: _Optional[_Iterable[_Union[DiagnosticMessage, _Mapping]]] = ...) -> None: ...

class DiagnosticMessage(_message.Message):
    __slots__ = ["client_id", "client_name", "time_stamp", "diagnostic_type", "diagnostic_message"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_name: str
    time_stamp: TimeStamp
    diagnostic_type: DiagnosticType
    diagnostic_message: str
    def __init__(self, client_id: _Optional[str] = ..., client_name: _Optional[str] = ..., time_stamp: _Optional[_Union[TimeStamp, _Mapping]] = ..., diagnostic_type: _Optional[_Union[DiagnosticType, str]] = ..., diagnostic_message: _Optional[str] = ...) -> None: ...

class RuntimeLogMetadata(_message.Message):
    __slots__ = ["project_folder", "scenario_file_path", "scenario_checksum"]
    PROJECT_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    project_folder: str
    scenario_file_path: str
    scenario_checksum: str
    def __init__(self, project_folder: _Optional[str] = ..., scenario_file_path: _Optional[str] = ..., scenario_checksum: _Optional[str] = ...) -> None: ...
