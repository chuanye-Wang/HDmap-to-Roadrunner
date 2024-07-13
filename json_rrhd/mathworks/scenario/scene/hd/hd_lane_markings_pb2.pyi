from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaneMarking(_message.Message):
    __slots__ = ["id", "asset_path"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_path: _common_attributes_pb2.RelativeAssetPath
    def __init__(self, id: _Optional[str] = ..., asset_path: _Optional[_Union[_common_attributes_pb2.RelativeAssetPath, _Mapping]] = ...) -> None: ...

class MarkingReference(_message.Message):
    __slots__ = ["marking_id", "flip_laterally"]
    MARKING_ID_FIELD_NUMBER: _ClassVar[int]
    FLIP_LATERALLY_FIELD_NUMBER: _ClassVar[int]
    marking_id: _common_attributes_pb2.Reference
    flip_laterally: bool
    def __init__(self, marking_id: _Optional[_Union[_common_attributes_pb2.Reference, _Mapping]] = ..., flip_laterally: bool = ...) -> None: ...
