from mathworks.scenario.common import coordinate_system_pb2 as _coordinate_system_pb2
from mathworks.scenario.common import core_pb2 as _core_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.simulation import attributes_pb2 as _attributes_pb2
from mathworks.scenario.simulation import behavior_pb2 as _behavior_pb2
from mathworks.scenario.simulation import scenario_pb2 as _scenario_pb2
from mathworks.scenario.simulation import sensor_pb2 as _sensor_pb2
from mathworks.scenario.scene.hd import common_attributes_pb2 as _common_attributes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CONNECTION_TYPE_UNSPECIFIED: _ClassVar[ConnectionType]
    CONNECTION_TYPE_TRAILER: _ClassVar[ConnectionType]
    CONNECTION_TYPE_CARGO: _ClassVar[ConnectionType]

class ReferenceFrame(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFERENCE_FRAME_UNSPECIFIED: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_WORLD: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_PARENT: _ClassVar[ReferenceFrame]
    REFERENCE_FRAME_SPECIFIED: _ClassVar[ReferenceFrame]
CONNECTION_TYPE_UNSPECIFIED: ConnectionType
CONNECTION_TYPE_TRAILER: ConnectionType
CONNECTION_TYPE_CARGO: ConnectionType
REFERENCE_FRAME_UNSPECIFIED: ReferenceFrame
REFERENCE_FRAME_WORLD: ReferenceFrame
REFERENCE_FRAME_PARENT: ReferenceFrame
REFERENCE_FRAME_SPECIFIED: ReferenceFrame

class Actor(_message.Message):
    __slots__ = ["actor_spec", "actor_runtime"]
    ACTOR_SPEC_FIELD_NUMBER: _ClassVar[int]
    ACTOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    actor_spec: ActorSpec
    actor_runtime: ActorRuntime
    def __init__(self, actor_spec: _Optional[_Union[ActorSpec, _Mapping]] = ..., actor_runtime: _Optional[_Union[ActorRuntime, _Mapping]] = ...) -> None: ...

class ActorSpec(_message.Message):
    __slots__ = ["id", "name", "asset_reference", "bounding_box", "behavior_id", "simulator_id", "attributes", "world_spec", "vehicle_spec", "character_spec", "sensor_spec", "miscellaneous_spec", "prop_reference_spec"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_ID_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORLD_SPEC_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SPEC_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SPEC_FIELD_NUMBER: _ClassVar[int]
    MISCELLANEOUS_SPEC_FIELD_NUMBER: _ClassVar[int]
    PROP_REFERENCE_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    asset_reference: str
    bounding_box: _geometry_pb2.Box3
    behavior_id: str
    simulator_id: str
    attributes: _containers.RepeatedCompositeFieldContainer[_attributes_pb2.Attribute]
    world_spec: WorldSpec
    vehicle_spec: VehicleSpec
    character_spec: CharacterSpec
    sensor_spec: SensorSpec
    miscellaneous_spec: MiscellaneousSpec
    prop_reference_spec: PropReferenceSpec
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., asset_reference: _Optional[str] = ..., bounding_box: _Optional[_Union[_geometry_pb2.Box3, _Mapping]] = ..., behavior_id: _Optional[str] = ..., simulator_id: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[_attributes_pb2.Attribute, _Mapping]]] = ..., world_spec: _Optional[_Union[WorldSpec, _Mapping]] = ..., vehicle_spec: _Optional[_Union[VehicleSpec, _Mapping]] = ..., character_spec: _Optional[_Union[CharacterSpec, _Mapping]] = ..., sensor_spec: _Optional[_Union[SensorSpec, _Mapping]] = ..., miscellaneous_spec: _Optional[_Union[MiscellaneousSpec, _Mapping]] = ..., prop_reference_spec: _Optional[_Union[PropReferenceSpec, _Mapping]] = ...) -> None: ...

class WorldSpec(_message.Message):
    __slots__ = ["actors", "behaviors", "scenario", "coordinate_system"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    BEHAVIORS_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[Actor]
    behaviors: _containers.RepeatedCompositeFieldContainer[_behavior_pb2.Behavior]
    scenario: _scenario_pb2.Scenario
    coordinate_system: _coordinate_system_pb2.CoordinateReferenceSystem
    def __init__(self, actors: _Optional[_Iterable[_Union[Actor, _Mapping]]] = ..., behaviors: _Optional[_Iterable[_Union[_behavior_pb2.Behavior, _Mapping]]] = ..., scenario: _Optional[_Union[_scenario_pb2.Scenario, _Mapping]] = ..., coordinate_system: _Optional[_Union[_coordinate_system_pb2.CoordinateReferenceSystem, _Mapping]] = ...) -> None: ...

class VehicleSpec(_message.Message):
    __slots__ = ["paint_color", "wheels"]
    PAINT_COLOR_FIELD_NUMBER: _ClassVar[int]
    WHEELS_FIELD_NUMBER: _ClassVar[int]
    paint_color: _core_pb2.ColorRGBA
    wheels: _containers.RepeatedCompositeFieldContainer[WheelSpec]
    def __init__(self, paint_color: _Optional[_Union[_core_pb2.ColorRGBA, _Mapping]] = ..., wheels: _Optional[_Iterable[_Union[WheelSpec, _Mapping]]] = ...) -> None: ...

class WheelSpec(_message.Message):
    __slots__ = ["axle_index", "wheel_offset", "wheel_radius"]
    AXLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    WHEEL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WHEEL_RADIUS_FIELD_NUMBER: _ClassVar[int]
    axle_index: int
    wheel_offset: _geometry_pb2.Vector3
    wheel_radius: float
    def __init__(self, axle_index: _Optional[int] = ..., wheel_offset: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., wheel_radius: _Optional[float] = ...) -> None: ...

class CharacterSpec(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SensorSpec(_message.Message):
    __slots__ = ["field_of_view", "range_limits", "detection_coordinates"]
    FIELD_OF_VIEW_FIELD_NUMBER: _ClassVar[int]
    RANGE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    field_of_view: _sensor_pb2.FieldOfView
    range_limits: _sensor_pb2.RangeLimits
    detection_coordinates: _sensor_pb2.SensorDetectionCoordinates
    def __init__(self, field_of_view: _Optional[_Union[_sensor_pb2.FieldOfView, _Mapping]] = ..., range_limits: _Optional[_Union[_sensor_pb2.RangeLimits, _Mapping]] = ..., detection_coordinates: _Optional[_Union[_sensor_pb2.SensorDetectionCoordinates, str]] = ...) -> None: ...

class MiscellaneousSpec(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PropReferenceSpec(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActorRuntime(_message.Message):
    __slots__ = ["id", "parent", "children", "connections", "pose", "velocity", "angular_velocity", "actor_lane_locations", "local_pose", "local_velocity", "local_angular_velocity", "behavior_parameters", "parameters", "world_runtime", "vehicle_runtime", "character_runtime", "sensor_runtime", "miscellaneous_runtime", "prop_reference_runtime"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ACTOR_LANE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_POSE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    WORLD_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SENSOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    MISCELLANEOUS_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    PROP_REFERENCE_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    parent: str
    children: _containers.RepeatedScalarFieldContainer[str]
    connections: _containers.RepeatedCompositeFieldContainer[Connection]
    pose: Transform
    velocity: _geometry_pb2.Vector3
    angular_velocity: _geometry_pb2.Vector3
    actor_lane_locations: ActorLaneLocations
    local_pose: Transform
    local_velocity: _geometry_pb2.Vector3
    local_angular_velocity: _geometry_pb2.Vector3
    behavior_parameters: _containers.RepeatedCompositeFieldContainer[_attributes_pb2.Attribute]
    parameters: _containers.RepeatedCompositeFieldContainer[_attributes_pb2.Attribute]
    world_runtime: WorldRuntime
    vehicle_runtime: VehicleRuntime
    character_runtime: CharacterRuntime
    sensor_runtime: SensorRuntime
    miscellaneous_runtime: MiscellaneousRuntime
    prop_reference_runtime: PropReferenceRuntime
    def __init__(self, id: _Optional[str] = ..., parent: _Optional[str] = ..., children: _Optional[_Iterable[str]] = ..., connections: _Optional[_Iterable[_Union[Connection, _Mapping]]] = ..., pose: _Optional[_Union[Transform, _Mapping]] = ..., velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., angular_velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., actor_lane_locations: _Optional[_Union[ActorLaneLocations, _Mapping]] = ..., local_pose: _Optional[_Union[Transform, _Mapping]] = ..., local_velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., local_angular_velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., behavior_parameters: _Optional[_Iterable[_Union[_attributes_pb2.Attribute, _Mapping]]] = ..., parameters: _Optional[_Iterable[_Union[_attributes_pb2.Attribute, _Mapping]]] = ..., world_runtime: _Optional[_Union[WorldRuntime, _Mapping]] = ..., vehicle_runtime: _Optional[_Union[VehicleRuntime, _Mapping]] = ..., character_runtime: _Optional[_Union[CharacterRuntime, _Mapping]] = ..., sensor_runtime: _Optional[_Union[SensorRuntime, _Mapping]] = ..., miscellaneous_runtime: _Optional[_Union[MiscellaneousRuntime, _Mapping]] = ..., prop_reference_runtime: _Optional[_Union[PropReferenceRuntime, _Mapping]] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ["connection_type", "first_actor_id", "first_connection_point", "second_actor_id", "second_connection_point"]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_CONNECTION_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SECOND_CONNECTION_POINT_FIELD_NUMBER: _ClassVar[int]
    connection_type: ConnectionType
    first_actor_id: str
    first_connection_point: _geometry_pb2.Vector3
    second_actor_id: str
    second_connection_point: _geometry_pb2.Vector3
    def __init__(self, connection_type: _Optional[_Union[ConnectionType, str]] = ..., first_actor_id: _Optional[str] = ..., first_connection_point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., second_actor_id: _Optional[str] = ..., second_connection_point: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class ActorPose(_message.Message):
    __slots__ = ["actor_id", "reference_frame", "coordinate_system_ref", "pose", "velocity", "angular_velocity"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_SYSTEM_REF_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    reference_frame: ReferenceFrame
    coordinate_system_ref: _coordinate_system_pb2.CoordinateSystemRef
    pose: Transform
    velocity: _geometry_pb2.Vector3
    angular_velocity: _geometry_pb2.Vector3
    def __init__(self, actor_id: _Optional[str] = ..., reference_frame: _Optional[_Union[ReferenceFrame, str]] = ..., coordinate_system_ref: _Optional[_Union[_coordinate_system_pb2.CoordinateSystemRef, _Mapping]] = ..., pose: _Optional[_Union[Transform, _Mapping]] = ..., velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., angular_velocity: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class WorldRuntime(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VehicleRuntime(_message.Message):
    __slots__ = ["wheels", "vehicle_map_locations"]
    WHEELS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_MAP_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    wheels: _containers.RepeatedCompositeFieldContainer[Transform]
    vehicle_map_locations: VehicleMapLocations
    def __init__(self, wheels: _Optional[_Iterable[_Union[Transform, _Mapping]]] = ..., vehicle_map_locations: _Optional[_Union[VehicleMapLocations, _Mapping]] = ...) -> None: ...

class VehiclePose(_message.Message):
    __slots__ = ["actor_pose", "wheels"]
    ACTOR_POSE_FIELD_NUMBER: _ClassVar[int]
    WHEELS_FIELD_NUMBER: _ClassVar[int]
    actor_pose: ActorPose
    wheels: _containers.RepeatedCompositeFieldContainer[Transform]
    def __init__(self, actor_pose: _Optional[_Union[ActorPose, _Mapping]] = ..., wheels: _Optional[_Iterable[_Union[Transform, _Mapping]]] = ...) -> None: ...

class VehicleMapLocations(_message.Message):
    __slots__ = ["on_lanes"]
    ON_LANES_FIELD_NUMBER: _ClassVar[int]
    on_lanes: VehicleMapLocationOnLanes
    def __init__(self, on_lanes: _Optional[_Union[VehicleMapLocationOnLanes, _Mapping]] = ...) -> None: ...

class VehicleMapLocationOnLanes(_message.Message):
    __slots__ = ["on_lane_positions", "best_aligned_lane_index", "angle"]
    ON_LANE_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    BEST_ALIGNED_LANE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    on_lane_positions: _containers.RepeatedCompositeFieldContainer[LanePosition]
    best_aligned_lane_index: int
    angle: float
    def __init__(self, on_lane_positions: _Optional[_Iterable[_Union[LanePosition, _Mapping]]] = ..., best_aligned_lane_index: _Optional[int] = ..., angle: _Optional[float] = ...) -> None: ...

class ActorLaneLocations(_message.Message):
    __slots__ = ["on_lane_positions", "best_aligned_lane_index", "angle"]
    ON_LANE_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    BEST_ALIGNED_LANE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    on_lane_positions: _containers.RepeatedCompositeFieldContainer[LanePosition]
    best_aligned_lane_index: int
    angle: float
    def __init__(self, on_lane_positions: _Optional[_Iterable[_Union[LanePosition, _Mapping]]] = ..., best_aligned_lane_index: _Optional[int] = ..., angle: _Optional[float] = ...) -> None: ...

class LanePosition(_message.Message):
    __slots__ = ["id", "s_value", "lane_offset"]
    ID_FIELD_NUMBER: _ClassVar[int]
    S_VALUE_FIELD_NUMBER: _ClassVar[int]
    LANE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    id: str
    s_value: float
    lane_offset: float
    def __init__(self, id: _Optional[str] = ..., s_value: _Optional[float] = ..., lane_offset: _Optional[float] = ...) -> None: ...

class AlignedLaneSegment(_message.Message):
    __slots__ = ["id", "span", "angle"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    span: _common_attributes_pb2.ParametricRange
    angle: float
    def __init__(self, id: _Optional[str] = ..., span: _Optional[_Union[_common_attributes_pb2.ParametricRange, _Mapping]] = ..., angle: _Optional[float] = ...) -> None: ...

class CharacterRuntime(_message.Message):
    __slots__ = ["bones"]
    BONES_FIELD_NUMBER: _ClassVar[int]
    bones: _containers.RepeatedCompositeFieldContainer[Bone]
    def __init__(self, bones: _Optional[_Iterable[_Union[Bone, _Mapping]]] = ...) -> None: ...

class MiscellaneousRuntime(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PropReferenceRuntime(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Transform(_message.Message):
    __slots__ = ["matrix"]
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    matrix: _geometry_pb2.Matrix4x4
    def __init__(self, matrix: _Optional[_Union[_geometry_pb2.Matrix4x4, _Mapping]] = ...) -> None: ...

class Bone(_message.Message):
    __slots__ = ["name", "transform"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    name: str
    transform: Transform
    def __init__(self, name: _Optional[str] = ..., transform: _Optional[_Union[Transform, _Mapping]] = ...) -> None: ...

class SensorRuntime(_message.Message):
    __slots__ = ["detections"]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    detections: _containers.RepeatedCompositeFieldContainer[_sensor_pb2.RayPath]
    def __init__(self, detections: _Optional[_Iterable[_Union[_sensor_pb2.RayPath, _Mapping]]] = ...) -> None: ...
