from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Data(_message.Message):
    __slots__ = ["array_element", "cell_element", "struct_element"]
    ARRAY_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    CELL_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    array_element: Array
    cell_element: Cell
    struct_element: Struct
    def __init__(self, array_element: _Optional[_Union[Array, _Mapping]] = ..., cell_element: _Optional[_Union[Cell, _Mapping]] = ..., struct_element: _Optional[_Union[Struct, _Mapping]] = ...) -> None: ...

class Array(_message.Message):
    __slots__ = ["dimensions", "elements"]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedScalarFieldContainer[int]
    elements: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, dimensions: _Optional[_Iterable[int]] = ..., elements: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class Cell(_message.Message):
    __slots__ = ["dimensions", "elements"]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedScalarFieldContainer[int]
    elements: _containers.RepeatedCompositeFieldContainer[Data]
    def __init__(self, dimensions: _Optional[_Iterable[int]] = ..., elements: _Optional[_Iterable[_Union[Data, _Mapping]]] = ...) -> None: ...

class Struct(_message.Message):
    __slots__ = ["names", "elements"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    elements: _containers.RepeatedCompositeFieldContainer[Data]
    def __init__(self, names: _Optional[_Iterable[str]] = ..., elements: _Optional[_Iterable[_Union[Data, _Mapping]]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ["number_element", "complex_element", "logical_element", "char_element", "string_element_deprecated", "struct_element", "string_element"]
    NUMBER_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    COMPLEX_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    CHAR_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    STRING_ELEMENT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    STRUCT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    STRING_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    number_element: Number
    complex_element: Complex
    logical_element: bool
    char_element: int
    string_element_deprecated: String
    struct_element: Struct
    string_element: str
    def __init__(self, number_element: _Optional[_Union[Number, _Mapping]] = ..., complex_element: _Optional[_Union[Complex, _Mapping]] = ..., logical_element: bool = ..., char_element: _Optional[int] = ..., string_element_deprecated: _Optional[_Union[String, _Mapping]] = ..., struct_element: _Optional[_Union[Struct, _Mapping]] = ..., string_element: _Optional[str] = ...) -> None: ...

class Number(_message.Message):
    __slots__ = ["uint8_element", "int8_element", "uint16_element", "int16_element", "uint32_element", "int32_element", "uint64_element", "int64_element", "single_element", "double_element"]
    UINT8_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    INT8_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    UINT16_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    INT16_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    UINT32_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    INT32_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    UINT64_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    INT64_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    SINGLE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    uint8_element: int
    int8_element: int
    uint16_element: int
    int16_element: int
    uint32_element: int
    int32_element: int
    uint64_element: int
    int64_element: int
    single_element: float
    double_element: float
    def __init__(self, uint8_element: _Optional[int] = ..., int8_element: _Optional[int] = ..., uint16_element: _Optional[int] = ..., int16_element: _Optional[int] = ..., uint32_element: _Optional[int] = ..., int32_element: _Optional[int] = ..., uint64_element: _Optional[int] = ..., int64_element: _Optional[int] = ..., single_element: _Optional[float] = ..., double_element: _Optional[float] = ...) -> None: ...

class Complex(_message.Message):
    __slots__ = ["real_element", "imag_element"]
    REAL_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    IMAG_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    real_element: Number
    imag_element: Number
    def __init__(self, real_element: _Optional[_Union[Number, _Mapping]] = ..., imag_element: _Optional[_Union[Number, _Mapping]] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, elements: _Optional[_Iterable[int]] = ...) -> None: ...
