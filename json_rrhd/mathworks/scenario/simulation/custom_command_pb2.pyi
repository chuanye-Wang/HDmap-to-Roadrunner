from mathworks.scenario.simulation import attributes_pb2 as _attributes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomCommand(_message.Message):
    __slots__ = ["name", "attributes"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    attributes: _containers.RepeatedCompositeFieldContainer[_attributes_pb2.Attribute]
    def __init__(self, name: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[_attributes_pb2.Attribute, _Mapping]]] = ...) -> None: ...
