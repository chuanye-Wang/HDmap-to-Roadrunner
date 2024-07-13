from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BarrierTypeDefinition(_message.Message):
    __slots__ = ["id", "extrusion_path"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTRUSION_PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    extrusion_path: _common_attributes_pb2.RelativeAssetPath
    def __init__(self, id: _Optional[str] = ..., extrusion_path: _Optional[_Union[_common_attributes_pb2.RelativeAssetPath, _Mapping]] = ...) -> None: ...

class Barrier(_message.Message):
    __slots__ = ["id", "geometry", "barrier_type_ref", "flip_laterally"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    BARRIER_TYPE_REF_FIELD_NUMBER: _ClassVar[int]
    FLIP_LATERALLY_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.Vector3List
    barrier_type_ref: _common_attributes_pb2.Reference
    flip_laterally: bool
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.Vector3List, _Mapping]] = ..., barrier_type_ref: _Optional[_Union[_common_attributes_pb2.Reference, _Mapping]] = ..., flip_laterally: bool = ...) -> None: ...
