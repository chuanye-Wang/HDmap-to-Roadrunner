from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoordinateReferenceSystem(_message.Message):
    __slots__ = ["projected_coordinate_system", "geographic_coordinate_system", "geocentric_coordinate_system", "engineering_coordinate_system"]
    PROJECTED_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    GEOGRAPHIC_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    GEOCENTRIC_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    ENGINEERING_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    projected_coordinate_system: _geometry_pb2.Projection
    geographic_coordinate_system: GeographicCoordinateSystem
    geocentric_coordinate_system: GeocentricCoordinateSystem
    engineering_coordinate_system: EngineeringCoordinateSystem
    def __init__(self, projected_coordinate_system: _Optional[_Union[_geometry_pb2.Projection, _Mapping]] = ..., geographic_coordinate_system: _Optional[_Union[GeographicCoordinateSystem, _Mapping]] = ..., geocentric_coordinate_system: _Optional[_Union[GeocentricCoordinateSystem, _Mapping]] = ..., engineering_coordinate_system: _Optional[_Union[EngineeringCoordinateSystem, _Mapping]] = ...) -> None: ...

class GeographicCoordinateSystem(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GeocentricCoordinateSystem(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EngineeringCoordinateSystem(_message.Message):
    __slots__ = ["geodetic_origin"]
    GEODETIC_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    geodetic_origin: GeodeticCoordinates
    def __init__(self, geodetic_origin: _Optional[_Union[GeodeticCoordinates, _Mapping]] = ...) -> None: ...

class GeodeticCoordinates(_message.Message):
    __slots__ = ["latitude", "longitude", "altitude"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class CoordinateSystemRef(_message.Message):
    __slots__ = ["coordinate_system"]
    COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    coordinate_system: CoordinateReferenceSystem
    def __init__(self, coordinate_system: _Optional[_Union[CoordinateReferenceSystem, _Mapping]] = ...) -> None: ...
