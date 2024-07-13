from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vector2(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Vector2Array(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Vector2]
    def __init__(self, values: _Optional[_Iterable[_Union[Vector2, _Mapping]]] = ...) -> None: ...

class Vector3(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Vector3Array(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Vector3]
    def __init__(self, values: _Optional[_Iterable[_Union[Vector3, _Mapping]]] = ...) -> None: ...

class Matrix3x3(_message.Message):
    __slots__ = ["col0", "col1", "col2"]
    COL0_FIELD_NUMBER: _ClassVar[int]
    COL1_FIELD_NUMBER: _ClassVar[int]
    COL2_FIELD_NUMBER: _ClassVar[int]
    col0: Vector3
    col1: Vector3
    col2: Vector3
    def __init__(self, col0: _Optional[_Union[Vector3, _Mapping]] = ..., col1: _Optional[_Union[Vector3, _Mapping]] = ..., col2: _Optional[_Union[Vector3, _Mapping]] = ...) -> None: ...

class Matrix3x3Array(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Matrix3x3]
    def __init__(self, values: _Optional[_Iterable[_Union[Matrix3x3, _Mapping]]] = ...) -> None: ...

class Vector4(_message.Message):
    __slots__ = ["x", "y", "z", "w"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    w: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class Vector4Array(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Vector4]
    def __init__(self, values: _Optional[_Iterable[_Union[Vector4, _Mapping]]] = ...) -> None: ...

class Matrix4x4(_message.Message):
    __slots__ = ["col0", "col1", "col2", "col3"]
    COL0_FIELD_NUMBER: _ClassVar[int]
    COL1_FIELD_NUMBER: _ClassVar[int]
    COL2_FIELD_NUMBER: _ClassVar[int]
    COL3_FIELD_NUMBER: _ClassVar[int]
    col0: Vector4
    col1: Vector4
    col2: Vector4
    col3: Vector4
    def __init__(self, col0: _Optional[_Union[Vector4, _Mapping]] = ..., col1: _Optional[_Union[Vector4, _Mapping]] = ..., col2: _Optional[_Union[Vector4, _Mapping]] = ..., col3: _Optional[_Union[Vector4, _Mapping]] = ...) -> None: ...

class Matrix4x4Array(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Matrix4x4]
    def __init__(self, values: _Optional[_Iterable[_Union[Matrix4x4, _Mapping]]] = ...) -> None: ...

class Box3(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: Vector3
    max: Vector3
    def __init__(self, min: _Optional[_Union[Vector3, _Mapping]] = ..., max: _Optional[_Union[Vector3, _Mapping]] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ["points"]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Vector3]
    def __init__(self, points: _Optional[_Iterable[_Union[Vector3, _Mapping]]] = ...) -> None: ...

class Vector3List(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Vector3]
    def __init__(self, values: _Optional[_Iterable[_Union[Vector3, _Mapping]]] = ...) -> None: ...

class Polygon(_message.Message):
    __slots__ = ["exterior_ring", "interior_rings"]
    EXTERIOR_RING_FIELD_NUMBER: _ClassVar[int]
    INTERIOR_RINGS_FIELD_NUMBER: _ClassVar[int]
    exterior_ring: Vector3List
    interior_rings: _containers.RepeatedCompositeFieldContainer[Vector3List]
    def __init__(self, exterior_ring: _Optional[_Union[Vector3List, _Mapping]] = ..., interior_rings: _Optional[_Iterable[_Union[Vector3List, _Mapping]]] = ...) -> None: ...

class MultiPolygon(_message.Message):
    __slots__ = ["polygons"]
    POLYGONS_FIELD_NUMBER: _ClassVar[int]
    polygons: _containers.RepeatedCompositeFieldContainer[Polygon]
    def __init__(self, polygons: _Optional[_Iterable[_Union[Polygon, _Mapping]]] = ...) -> None: ...

class Projection(_message.Message):
    __slots__ = ["projection"]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    projection: str
    def __init__(self, projection: _Optional[str] = ...) -> None: ...

class Dimension3(_message.Message):
    __slots__ = ["length", "width", "height"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    length: float
    width: float
    height: float
    def __init__(self, length: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class GeoAngle3(_message.Message):
    __slots__ = ["roll", "pitch", "heading"]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    roll: float
    pitch: float
    heading: float
    def __init__(self, roll: _Optional[float] = ..., pitch: _Optional[float] = ..., heading: _Optional[float] = ...) -> None: ...

class GeoOrientation3(_message.Message):
    __slots__ = ["geo_angle"]
    GEO_ANGLE_FIELD_NUMBER: _ClassVar[int]
    geo_angle: GeoAngle3
    def __init__(self, geo_angle: _Optional[_Union[GeoAngle3, _Mapping]] = ...) -> None: ...

class GeoOrientedBoundingBox(_message.Message):
    __slots__ = ["center", "dimension", "geo_orientation"]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    GEO_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    center: Vector3
    dimension: Dimension3
    geo_orientation: GeoOrientation3
    def __init__(self, center: _Optional[_Union[Vector3, _Mapping]] = ..., dimension: _Optional[_Union[Dimension3, _Mapping]] = ..., geo_orientation: _Optional[_Union[GeoOrientation3, _Mapping]] = ...) -> None: ...

class Orientation(_message.Message):
    __slots__ = ["euler_angles", "rotation_matrix"]
    EULER_ANGLES_FIELD_NUMBER: _ClassVar[int]
    ROTATION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    euler_angles: GeoAngle3
    rotation_matrix: Matrix3x3
    def __init__(self, euler_angles: _Optional[_Union[GeoAngle3, _Mapping]] = ..., rotation_matrix: _Optional[_Union[Matrix3x3, _Mapping]] = ...) -> None: ...
