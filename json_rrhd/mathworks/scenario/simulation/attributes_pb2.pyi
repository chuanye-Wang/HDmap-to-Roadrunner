from mathworks.scenario.common import array_pb2 as _array_pb2
from mathworks.scenario.common import core_pb2 as _core_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Attribute(_message.Message):
    __slots__ = ["color", "name", "point", "path", "data"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    color: _core_pb2.ColorRGBA
    name: str
    point: _geometry_pb2.Vector3
    path: _geometry_pb2.Path
    data: _array_pb2.Data
    def __init__(self, color: _Optional[_Union[_core_pb2.ColorRGBA, _Mapping]] = ..., name: _Optional[str] = ..., point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., path: _Optional[_Union[_geometry_pb2.Path, _Mapping]] = ..., data: _Optional[_Union[_array_pb2.Data, _Mapping]] = ...) -> None: ...
