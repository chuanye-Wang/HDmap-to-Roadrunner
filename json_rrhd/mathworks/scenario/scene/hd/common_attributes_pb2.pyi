from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALIGNMENT_UNSPECIFIED: _ClassVar[Alignment]
    ALIGNMENT_FORWARD: _ClassVar[Alignment]
    ALIGNMENT_BACKWARD: _ClassVar[Alignment]
ALIGNMENT_UNSPECIFIED: Alignment
ALIGNMENT_FORWARD: Alignment
ALIGNMENT_BACKWARD: Alignment

class ParametricRange(_message.Message):
    __slots__ = ["span_start", "span_end"]
    SPAN_START_FIELD_NUMBER: _ClassVar[int]
    SPAN_END_FIELD_NUMBER: _ClassVar[int]
    span_start: float
    span_end: float
    def __init__(self, span_start: _Optional[float] = ..., span_end: _Optional[float] = ...) -> None: ...

class AlignedReference(_message.Message):
    __slots__ = ["reference", "alignment"]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    reference: Reference
    alignment: Alignment
    def __init__(self, reference: _Optional[_Union[Reference, _Mapping]] = ..., alignment: _Optional[_Union[Alignment, str]] = ...) -> None: ...

class Reference(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RelativeAssetPath(_message.Message):
    __slots__ = ["asset_path"]
    ASSET_PATH_FIELD_NUMBER: _ClassVar[int]
    asset_path: str
    def __init__(self, asset_path: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
