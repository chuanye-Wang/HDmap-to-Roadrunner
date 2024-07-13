from mathworks.scenario.simulation import action_pb2 as _action_pb2
from mathworks.scenario.simulation import condition_status_pb2 as _condition_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionStatus(_message.Message):
    __slots__ = ["id", "action_event_status", "condition_status"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_EVENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    action_event_status: _action_pb2.ActionEventStatus
    condition_status: _condition_status_pb2.ConditionStatus
    def __init__(self, id: _Optional[str] = ..., action_event_status: _Optional[_Union[_action_pb2.ActionEventStatus, str]] = ..., condition_status: _Optional[_Union[_condition_status_pb2.ConditionStatus, _Mapping]] = ...) -> None: ...
