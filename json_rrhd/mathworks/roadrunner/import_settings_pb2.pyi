from google.protobuf import wrappers_pb2 as _wrappers_pb2
from mathworks.roadrunner import core_pb2 as _core_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PROJECTION_MODE_UNSPECIFIED: _ClassVar[ProjectionMode]
    PROJECTION_MODE_FULL_PROJECTION: _ClassVar[ProjectionMode]
    PROJECTION_MODE_TRANSLATE_ONLY: _ClassVar[ProjectionMode]
    PROJECTION_MODE_NO_PROJECTION: _ClassVar[ProjectionMode]

class MedianLaneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MEDIAN_LANE_TYPE_UNSPECIFIED: _ClassVar[MedianLaneType]
    MEDIAN_LANE_TYPE_MEDIAN: _ClassVar[MedianLaneType]
    MEDIAN_LANE_TYPE_RAISED_MEDIAN: _ClassVar[MedianLaneType]

class ImportStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    IMPORT_STEP_UNSPECIFIED: _ClassVar[ImportStep]
    IMPORT_STEP_LOAD: _ClassVar[ImportStep]
    IMPORT_STEP_BUILD: _ClassVar[ImportStep]
PROJECTION_MODE_UNSPECIFIED: ProjectionMode
PROJECTION_MODE_FULL_PROJECTION: ProjectionMode
PROJECTION_MODE_TRANSLATE_ONLY: ProjectionMode
PROJECTION_MODE_NO_PROJECTION: ProjectionMode
MEDIAN_LANE_TYPE_UNSPECIFIED: MedianLaneType
MEDIAN_LANE_TYPE_MEDIAN: MedianLaneType
MEDIAN_LANE_TYPE_RAISED_MEDIAN: MedianLaneType
IMPORT_STEP_UNSPECIFIED: ImportStep
IMPORT_STEP_LOAD: ImportStep
IMPORT_STEP_BUILD: ImportStep

class OpenDriveImportSettings(_message.Message):
    __slots__ = ["import_signals", "import_props", "import_hoffset_relative_to_orientation", "lane_options", "offset", "projection", "projection_mode"]
    IMPORT_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PROPS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_HOFFSET_RELATIVE_TO_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    LANE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    import_signals: _wrappers_pb2.BoolValue
    import_props: _wrappers_pb2.BoolValue
    import_hoffset_relative_to_orientation: _wrappers_pb2.BoolValue
    lane_options: LaneOptions
    offset: _geometry_pb2.Vector3
    projection: _geometry_pb2.Projection
    projection_mode: ProjectionMode
    def __init__(self, import_signals: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., import_props: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., import_hoffset_relative_to_orientation: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., lane_options: _Optional[_Union[LaneOptions, _Mapping]] = ..., offset: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., projection: _Optional[_Union[_geometry_pb2.Projection, _Mapping]] = ..., projection_mode: _Optional[_Union[ProjectionMode, str]] = ...) -> None: ...

class RoadRunnerHdMapImportSettings(_message.Message):
    __slots__ = ["import_step", "load_settings", "build_settings"]
    IMPORT_STEP_FIELD_NUMBER: _ClassVar[int]
    LOAD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BUILD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    import_step: ImportStep
    load_settings: RoadRunnerHdMapLoadSettings
    build_settings: RoadRunnerHdMapBuildSettings
    def __init__(self, import_step: _Optional[_Union[ImportStep, str]] = ..., load_settings: _Optional[_Union[RoadRunnerHdMapLoadSettings, _Mapping]] = ..., build_settings: _Optional[_Union[RoadRunnerHdMapBuildSettings, _Mapping]] = ...) -> None: ...

class RoadRunnerHdMapLoadSettings(_message.Message):
    __slots__ = ["offset", "projection"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    offset: _geometry_pb2.Vector3
    projection: _geometry_pb2.Projection
    def __init__(self, offset: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., projection: _Optional[_Union[_geometry_pb2.Projection, _Mapping]] = ...) -> None: ...

class RoadRunnerHdMapBuildSettings(_message.Message):
    __slots__ = ["fit_cross_sections", "detect_asphalt_surfaces", "clear_scene_of_existing_data", "curvature_blend", "auto_detect_bridges", "enable_overlap_groups"]
    FIT_CROSS_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    DETECT_ASPHALT_SURFACES_FIELD_NUMBER: _ClassVar[int]
    CLEAR_SCENE_OF_EXISTING_DATA_FIELD_NUMBER: _ClassVar[int]
    CURVATURE_BLEND_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_BRIDGES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OVERLAP_GROUPS_FIELD_NUMBER: _ClassVar[int]
    fit_cross_sections: _wrappers_pb2.BoolValue
    detect_asphalt_surfaces: _wrappers_pb2.BoolValue
    clear_scene_of_existing_data: _wrappers_pb2.BoolValue
    curvature_blend: _wrappers_pb2.DoubleValue
    auto_detect_bridges: AutoDetectBridges
    enable_overlap_groups: EnableOverlapGroups
    def __init__(self, fit_cross_sections: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., detect_asphalt_surfaces: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., clear_scene_of_existing_data: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., curvature_blend: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., auto_detect_bridges: _Optional[_Union[AutoDetectBridges, _Mapping]] = ..., enable_overlap_groups: _Optional[_Union[EnableOverlapGroups, _Mapping]] = ...) -> None: ...

class AutoDetectBridges(_message.Message):
    __slots__ = ["bridge_span_inflation"]
    BRIDGE_SPAN_INFLATION_FIELD_NUMBER: _ClassVar[int]
    bridge_span_inflation: _wrappers_pb2.DoubleValue
    def __init__(self, bridge_span_inflation: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class EnableOverlapGroups(_message.Message):
    __slots__ = ["enable", "group_name"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    enable: _wrappers_pb2.BoolValue
    group_name: _wrappers_pb2.StringValue
    def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., group_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class LaneOptions(_message.Message):
    __slots__ = ["curb_lane_markings_to_curb_lanes", "convert_lane_heights", "median_lane_type"]
    CURB_LANE_MARKINGS_TO_CURB_LANES_FIELD_NUMBER: _ClassVar[int]
    CONVERT_LANE_HEIGHTS_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_LANE_TYPE_FIELD_NUMBER: _ClassVar[int]
    curb_lane_markings_to_curb_lanes: _wrappers_pb2.BoolValue
    convert_lane_heights: _wrappers_pb2.BoolValue
    median_lane_type: MedianLaneType
    def __init__(self, curb_lane_markings_to_curb_lanes: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., convert_lane_heights: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., median_lane_type: _Optional[_Union[MedianLaneType, str]] = ...) -> None: ...

class ActorAttributes(_message.Message):
    __slots__ = ["name", "id", "color", "asset_path", "behavior_asset_path"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ASSET_PATH_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_ASSET_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    color: str
    asset_path: str
    behavior_asset_path: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., color: _Optional[str] = ..., asset_path: _Optional[str] = ..., behavior_asset_path: _Optional[str] = ...) -> None: ...

class CsvTrajectoryImportSettings(_message.Message):
    __slots__ = ["actor_attributes", "spawn_time", "remove_time"]
    ACTOR_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SPAWN_TIME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TIME_FIELD_NUMBER: _ClassVar[int]
    actor_attributes: ActorAttributes
    spawn_time: _wrappers_pb2.DoubleValue
    remove_time: _wrappers_pb2.DoubleValue
    def __init__(self, actor_attributes: _Optional[_Union[ActorAttributes, _Mapping]] = ..., spawn_time: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., remove_time: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class SdMapImportSettings(_message.Message):
    __slots__ = ["build_settings"]
    BUILD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    build_settings: SdMapBuildSettings
    def __init__(self, build_settings: _Optional[_Union[SdMapBuildSettings, _Mapping]] = ...) -> None: ...

class SdMapBuildSettings(_message.Message):
    __slots__ = ["destructive_options", "non_destructive_options", "scene_builder_options", "auto_detect_bridges", "enable_overlap_groups"]
    DESTRUCTIVE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    NON_DESTRUCTIVE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SCENE_BUILDER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DETECT_BRIDGES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OVERLAP_GROUPS_FIELD_NUMBER: _ClassVar[int]
    destructive_options: SdMapDestructiveBuildOptions
    non_destructive_options: SdMapNonDestructiveBuildOptions
    scene_builder_options: SdMapSceneBuilderOptions
    auto_detect_bridges: AutoDetectBridges
    enable_overlap_groups: EnableOverlapGroups
    def __init__(self, destructive_options: _Optional[_Union[SdMapDestructiveBuildOptions, _Mapping]] = ..., non_destructive_options: _Optional[_Union[SdMapNonDestructiveBuildOptions, _Mapping]] = ..., scene_builder_options: _Optional[_Union[SdMapSceneBuilderOptions, _Mapping]] = ..., auto_detect_bridges: _Optional[_Union[AutoDetectBridges, _Mapping]] = ..., enable_overlap_groups: _Optional[_Union[EnableOverlapGroups, _Mapping]] = ...) -> None: ...

class SdMapDestructiveBuildOptions(_message.Message):
    __slots__ = ["preserve_heights", "clear_scene_of_existing_data"]
    PRESERVE_HEIGHTS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_SCENE_OF_EXISTING_DATA_FIELD_NUMBER: _ClassVar[int]
    preserve_heights: _wrappers_pb2.BoolValue
    clear_scene_of_existing_data: _wrappers_pb2.BoolValue
    def __init__(self, preserve_heights: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., clear_scene_of_existing_data: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SdMapNonDestructiveBuildOptions(_message.Message):
    __slots__ = ["driving_side", "enable_overlap_groups"]
    DRIVING_SIDE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OVERLAP_GROUPS_FIELD_NUMBER: _ClassVar[int]
    driving_side: _core_pb2.DrivingSide
    enable_overlap_groups: _wrappers_pb2.BoolValue
    def __init__(self, driving_side: _Optional[_Union[_core_pb2.DrivingSide, str]] = ..., enable_overlap_groups: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SdMapSceneBuilderOptions(_message.Message):
    __slots__ = ["elevate_roads_by_layer", "create_turn_lanes"]
    ELEVATE_ROADS_BY_LAYER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TURN_LANES_FIELD_NUMBER: _ClassVar[int]
    elevate_roads_by_layer: _wrappers_pb2.BoolValue
    create_turn_lanes: _wrappers_pb2.BoolValue
    def __init__(self, elevate_roads_by_layer: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., create_turn_lanes: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
