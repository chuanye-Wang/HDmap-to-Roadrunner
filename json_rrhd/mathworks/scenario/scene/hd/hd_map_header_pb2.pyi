from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Header(_message.Message):
    __slots__ = ["author", "projection", "geographic_boundary"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    GEOGRAPHIC_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    author: str
    projection: _geometry_pb2.Projection
    geographic_boundary: DataBounds
    def __init__(self, author: _Optional[str] = ..., projection: _Optional[_Union[_geometry_pb2.Projection, _Mapping]] = ..., geographic_boundary: _Optional[_Union[DataBounds, _Mapping]] = ...) -> None: ...

class DataBounds(_message.Message):
    __slots__ = ["bounds"]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    bounds: _geometry_pb2.Box3
    def __init__(self, bounds: _Optional[_Union[_geometry_pb2.Box3, _Mapping]] = ...) -> None: ...
