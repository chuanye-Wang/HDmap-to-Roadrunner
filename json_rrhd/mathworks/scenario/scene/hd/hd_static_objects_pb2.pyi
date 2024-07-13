from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StaticObjectTypeDefinition(_message.Message):
    __slots__ = ["id", "asset_path"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_path: _common_attributes_pb2.RelativeAssetPath
    def __init__(self, id: _Optional[str] = ..., asset_path: _Optional[_Union[_common_attributes_pb2.RelativeAssetPath, _Mapping]] = ...) -> None: ...

class StaticObject(_message.Message):
    __slots__ = ["id", "geometry", "object_type_ref"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_REF_FIELD_NUMBER: _ClassVar[int]
    id: str
    geometry: _geometry_pb2.GeoOrientedBoundingBox
    object_type_ref: _common_attributes_pb2.Reference
    def __init__(self, id: _Optional[str] = ..., geometry: _Optional[_Union[_geometry_pb2.GeoOrientedBoundingBox, _Mapping]] = ..., object_type_ref: _Optional[_Union[_common_attributes_pb2.Reference, _Mapping]] = ...) -> None: ...
