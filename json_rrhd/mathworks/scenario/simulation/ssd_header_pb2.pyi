from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Header(_message.Message):
    __slots__ = ["author"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    author: str
    def __init__(self, author: _Optional[str] = ...) -> None: ...
