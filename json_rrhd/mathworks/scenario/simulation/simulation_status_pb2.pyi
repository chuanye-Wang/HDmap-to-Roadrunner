from mathworks.scenario.simulation import condition_status_pb2 as _condition_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIMULATION_STATUS_UNSPECIFIED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_STOPPED: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_RUNNING: _ClassVar[SimulationStatus]
    SIMULATION_STATUS_PAUSED: _ClassVar[SimulationStatus]
SIMULATION_STATUS_UNSPECIFIED: SimulationStatus
SIMULATION_STATUS_STOPPED: SimulationStatus
SIMULATION_STATUS_RUNNING: SimulationStatus
SIMULATION_STATUS_PAUSED: SimulationStatus

class SimulationStopCause(_message.Message):
    __slots__ = ["summary", "simulation_complete", "simulation_failed"]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    summary: str
    simulation_complete: SimulationComplete
    simulation_failed: SimulationFailed
    def __init__(self, summary: _Optional[str] = ..., simulation_complete: _Optional[_Union[SimulationComplete, _Mapping]] = ..., simulation_failed: _Optional[_Union[SimulationFailed, _Mapping]] = ...) -> None: ...

class SimulationFailed(_message.Message):
    __slots__ = ["failure_status", "engine_error", "client_error"]
    FAILURE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ERROR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    failure_status: FailureStatus
    engine_error: EngineError
    client_error: ClientError
    def __init__(self, failure_status: _Optional[_Union[FailureStatus, _Mapping]] = ..., engine_error: _Optional[_Union[EngineError, _Mapping]] = ..., client_error: _Optional[_Union[ClientError, _Mapping]] = ...) -> None: ...

class SuccessStatus(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[_condition_status_pb2.ConditionStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[_condition_status_pb2.ConditionStatus, _Mapping]]] = ...) -> None: ...

class FailureStatus(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[_condition_status_pb2.ConditionStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[_condition_status_pb2.ConditionStatus, _Mapping]]] = ...) -> None: ...

class EngineError(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClientError(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulationComplete(_message.Message):
    __slots__ = ["success_status", "stop_requested", "stop_time_reached"]
    SUCCESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    STOP_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_REACHED_FIELD_NUMBER: _ClassVar[int]
    success_status: SuccessStatus
    stop_requested: StopRequested
    stop_time_reached: StopTimeReached
    def __init__(self, success_status: _Optional[_Union[SuccessStatus, _Mapping]] = ..., stop_requested: _Optional[_Union[StopRequested, _Mapping]] = ..., stop_time_reached: _Optional[_Union[StopTimeReached, _Mapping]] = ...) -> None: ...

class StopRequested(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class StopTimeReached(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
