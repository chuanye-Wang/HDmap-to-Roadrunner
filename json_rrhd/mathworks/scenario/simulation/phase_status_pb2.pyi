from mathworks.scenario.simulation import action_status_pb2 as _action_status_pb2
from mathworks.scenario.simulation import condition_status_pb2 as _condition_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhaseState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PHASE_STATE_UNSPECIFIED: _ClassVar[PhaseState]
    PHASE_STATE_IDLE: _ClassVar[PhaseState]
    PHASE_STATE_START: _ClassVar[PhaseState]
    PHASE_STATE_RUN: _ClassVar[PhaseState]
    PHASE_STATE_END: _ClassVar[PhaseState]
PHASE_STATE_UNSPECIFIED: PhaseState
PHASE_STATE_IDLE: PhaseState
PHASE_STATE_START: PhaseState
PHASE_STATE_RUN: PhaseState
PHASE_STATE_END: PhaseState

class PhaseStatus(_message.Message):
    __slots__ = ["id", "phase_state", "start_condition_status", "end_condition_status", "action_status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_STATE_FIELD_NUMBER: _ClassVar[int]
    START_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    END_CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    phase_state: PhaseState
    start_condition_status: _condition_status_pb2.ConditionStatus
    end_condition_status: _condition_status_pb2.ConditionStatus
    action_status: _containers.RepeatedCompositeFieldContainer[_action_status_pb2.ActionStatus]
    def __init__(self, id: _Optional[str] = ..., phase_state: _Optional[_Union[PhaseState, str]] = ..., start_condition_status: _Optional[_Union[_condition_status_pb2.ConditionStatus, _Mapping]] = ..., end_condition_status: _Optional[_Union[_condition_status_pb2.ConditionStatus, _Mapping]] = ..., action_status: _Optional[_Iterable[_Union[_action_status_pb2.ActionStatus, _Mapping]]] = ...) -> None: ...
