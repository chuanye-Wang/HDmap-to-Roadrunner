from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Junction(_message.Message):
    __slots__ = ["id", "geometry", "lanes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    LANES_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.MultiPolygon
    lanes: _containers.RepeatedCompositeFieldContainer[_common_attributes_pb2.Reference]
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.MultiPolygon, _Mapping]] = ..., lanes: _Optional[_Iterable[_Union[_common_attributes_pb2.Reference, _Mapping]]] = ...) -> None: ...
