from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DrivingSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DRIVING_SIDE_UNSPECIFIED: _ClassVar[DrivingSide]
    DRIVING_SIDE_LEFT: _ClassVar[DrivingSide]
    DRIVING_SIDE_RIGHT: _ClassVar[DrivingSide]
DRIVING_SIDE_UNSPECIFIED: DrivingSide
DRIVING_SIDE_LEFT: DrivingSide
DRIVING_SIDE_RIGHT: DrivingSide
