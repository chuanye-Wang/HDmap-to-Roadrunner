from mathworks.roadrunner import import_settings_pb2 as _import_settings_pb2
from mathworks.roadrunner import export_settings_pb2 as _export_settings_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from mathworks.scenario.common import array_pb2 as _array_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewProjectRequest(_message.Message):
    __slots__ = ["folder_path", "asset_libraries"]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    ASSET_LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    asset_libraries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, folder_path: _Optional[str] = ..., asset_libraries: _Optional[_Iterable[str]] = ...) -> None: ...

class NewProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LoadProjectRequest(_message.Message):
    __slots__ = ["folder_path"]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    def __init__(self, folder_path: _Optional[str] = ...) -> None: ...

class LoadProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SaveProjectRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SaveProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NewSceneRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NewSceneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LoadSceneRequest(_message.Message):
    __slots__ = ["file_path"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class LoadSceneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SaveSceneRequest(_message.Message):
    __slots__ = ["file_path"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class SaveSceneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ChangeWorldSettingsRequest(_message.Message):
    __slots__ = ["clear_world_projection", "world_origin", "transform_scene", "scene_center", "scene_extents"]
    CLEAR_WORLD_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    WORLD_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_SCENE_FIELD_NUMBER: _ClassVar[int]
    SCENE_CENTER_FIELD_NUMBER: _ClassVar[int]
    SCENE_EXTENTS_FIELD_NUMBER: _ClassVar[int]
    clear_world_projection: bool
    world_origin: Coordinates
    transform_scene: bool
    scene_center: _geometry_pb2.Vector2
    scene_extents: _geometry_pb2.Vector2
    def __init__(self, clear_world_projection: bool = ..., world_origin: _Optional[_Union[Coordinates, _Mapping]] = ..., transform_scene: bool = ..., scene_center: _Optional[_Union[_geometry_pb2.Vector2, _Mapping]] = ..., scene_extents: _Optional[_Union[_geometry_pb2.Vector2, _Mapping]] = ...) -> None: ...

class ChangeWorldSettingsResponse(_message.Message):
    __slots__ = ["projection", "world_origin", "scene_center", "scene_extents"]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    WORLD_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    SCENE_CENTER_FIELD_NUMBER: _ClassVar[int]
    SCENE_EXTENTS_FIELD_NUMBER: _ClassVar[int]
    projection: _geometry_pb2.Projection
    world_origin: Coordinates
    scene_center: _geometry_pb2.Vector2
    scene_extents: _geometry_pb2.Vector2
    def __init__(self, projection: _Optional[_Union[_geometry_pb2.Projection, _Mapping]] = ..., world_origin: _Optional[_Union[Coordinates, _Mapping]] = ..., scene_center: _Optional[_Union[_geometry_pb2.Vector2, _Mapping]] = ..., scene_extents: _Optional[_Union[_geometry_pb2.Vector2, _Mapping]] = ...) -> None: ...

class Coordinates(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class SetVariableRequest(_message.Message):
    __slots__ = ["name", "value", "typed_value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPED_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    typed_value: _array_pb2.Value
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., typed_value: _Optional[_Union[_array_pb2.Value, _Mapping]] = ...) -> None: ...

class SetVariableResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetVariableRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetVariableResponse(_message.Message):
    __slots__ = ["value", "variable"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    value: str
    variable: Variable
    def __init__(self, value: _Optional[str] = ..., variable: _Optional[_Union[Variable, _Mapping]] = ...) -> None: ...

class GetAllVariablesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllVariablesResponse(_message.Message):
    __slots__ = ["variables"]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    variables: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, variables: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class Variable(_message.Message):
    __slots__ = ["name", "value", "typed_value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPED_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    typed_value: _array_pb2.Value
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., typed_value: _Optional[_Union[_array_pb2.Value, _Mapping]] = ...) -> None: ...

class NewScenarioRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NewScenarioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LoadScenarioRequest(_message.Message):
    __slots__ = ["file_path", "keep_current_scene"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    KEEP_CURRENT_SCENE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    keep_current_scene: bool
    def __init__(self, file_path: _Optional[str] = ..., keep_current_scene: bool = ...) -> None: ...

class LoadScenarioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SaveScenarioRequest(_message.Message):
    __slots__ = ["file_path"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    def __init__(self, file_path: _Optional[str] = ...) -> None: ...

class SaveScenarioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PrepareSimulationRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PrepareSimulationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulateScenarioRequest(_message.Message):
    __slots__ = ["pacing", "blocking", "stepping_start"]
    PACING_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_FIELD_NUMBER: _ClassVar[int]
    STEPPING_START_FIELD_NUMBER: _ClassVar[int]
    pacing: _wrappers_pb2.DoubleValue
    blocking: _wrappers_pb2.BoolValue
    stepping_start: _wrappers_pb2.BoolValue
    def __init__(self, pacing: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., blocking: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., stepping_start: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SimulateScenarioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportRequest(_message.Message):
    __slots__ = ["file_path", "format_name", "auto_cad_settings", "filmbox_settings", "gltf_settings", "open_flight_settings", "open_scene_graph_settings", "unreal_datasmith_settings", "usd_settings", "apollo_settings", "geo_json_settings", "open_drive_settings", "carla_settings", "carla_filmbox_settings", "metamoto_settings", "rfpro_settings", "unity_settings", "unreal_settings", "datasmith_road_settings", "vtd_settings", "open_scenario_settings", "open_scenario_2_settings"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FORMAT_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FILMBOX_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GLTF_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FLIGHT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPEN_SCENE_GRAPH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UNREAL_DATASMITH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GEO_JSON_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPEN_DRIVE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CARLA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CARLA_FILMBOX_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    METAMOTO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RFPRO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UNITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UNREAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DATASMITH_ROAD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VTD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPEN_SCENARIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OPEN_SCENARIO_2_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    format_name: str
    auto_cad_settings: _export_settings_pb2.AutoCadExportSettings
    filmbox_settings: _export_settings_pb2.FilmboxExportSettings
    gltf_settings: _export_settings_pb2.GltfExportSettings
    open_flight_settings: _export_settings_pb2.OpenFlightExportSettings
    open_scene_graph_settings: _export_settings_pb2.OpenSceneGraphExportSettings
    unreal_datasmith_settings: _export_settings_pb2.UnrealDatasmithExportSettings
    usd_settings: _export_settings_pb2.UsdExportSettings
    apollo_settings: _export_settings_pb2.ApolloExportSettings
    geo_json_settings: _export_settings_pb2.GeoJsonExportSettings
    open_drive_settings: _export_settings_pb2.OpenDriveExportSettings
    carla_settings: _export_settings_pb2.CarlaExportSettings
    carla_filmbox_settings: _export_settings_pb2.CarlaFilmboxExportSettings
    metamoto_settings: _export_settings_pb2.MetamotoExportSettings
    rfpro_settings: _export_settings_pb2.RFProExportSettings
    unity_settings: _export_settings_pb2.UnityExportSettings
    unreal_settings: _export_settings_pb2.UnrealExportSettings
    datasmith_road_settings: _export_settings_pb2.DatasmithRoadExportSettings
    vtd_settings: _export_settings_pb2.VtdExportSettings
    open_scenario_settings: _export_settings_pb2.OpenScenarioExportSettings
    open_scenario_2_settings: _export_settings_pb2.OpenScenario2ExportSettings
    def __init__(self, file_path: _Optional[str] = ..., format_name: _Optional[str] = ..., auto_cad_settings: _Optional[_Union[_export_settings_pb2.AutoCadExportSettings, _Mapping]] = ..., filmbox_settings: _Optional[_Union[_export_settings_pb2.FilmboxExportSettings, _Mapping]] = ..., gltf_settings: _Optional[_Union[_export_settings_pb2.GltfExportSettings, _Mapping]] = ..., open_flight_settings: _Optional[_Union[_export_settings_pb2.OpenFlightExportSettings, _Mapping]] = ..., open_scene_graph_settings: _Optional[_Union[_export_settings_pb2.OpenSceneGraphExportSettings, _Mapping]] = ..., unreal_datasmith_settings: _Optional[_Union[_export_settings_pb2.UnrealDatasmithExportSettings, _Mapping]] = ..., usd_settings: _Optional[_Union[_export_settings_pb2.UsdExportSettings, _Mapping]] = ..., apollo_settings: _Optional[_Union[_export_settings_pb2.ApolloExportSettings, _Mapping]] = ..., geo_json_settings: _Optional[_Union[_export_settings_pb2.GeoJsonExportSettings, _Mapping]] = ..., open_drive_settings: _Optional[_Union[_export_settings_pb2.OpenDriveExportSettings, _Mapping]] = ..., carla_settings: _Optional[_Union[_export_settings_pb2.CarlaExportSettings, _Mapping]] = ..., carla_filmbox_settings: _Optional[_Union[_export_settings_pb2.CarlaFilmboxExportSettings, _Mapping]] = ..., metamoto_settings: _Optional[_Union[_export_settings_pb2.MetamotoExportSettings, _Mapping]] = ..., rfpro_settings: _Optional[_Union[_export_settings_pb2.RFProExportSettings, _Mapping]] = ..., unity_settings: _Optional[_Union[_export_settings_pb2.UnityExportSettings, _Mapping]] = ..., unreal_settings: _Optional[_Union[_export_settings_pb2.UnrealExportSettings, _Mapping]] = ..., datasmith_road_settings: _Optional[_Union[_export_settings_pb2.DatasmithRoadExportSettings, _Mapping]] = ..., vtd_settings: _Optional[_Union[_export_settings_pb2.VtdExportSettings, _Mapping]] = ..., open_scenario_settings: _Optional[_Union[_export_settings_pb2.OpenScenarioExportSettings, _Mapping]] = ..., open_scenario_2_settings: _Optional[_Union[_export_settings_pb2.OpenScenario2ExportSettings, _Mapping]] = ...) -> None: ...

class ExportResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ["file_path", "format_name", "open_drive_settings", "roadrunner_hd_map_settings", "csv_trajectory_settings", "sd_map_settings"]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FORMAT_NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_DRIVE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROADRUNNER_HD_MAP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CSV_TRAJECTORY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SD_MAP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    format_name: str
    open_drive_settings: _import_settings_pb2.OpenDriveImportSettings
    roadrunner_hd_map_settings: _import_settings_pb2.RoadRunnerHdMapImportSettings
    csv_trajectory_settings: _import_settings_pb2.CsvTrajectoryImportSettings
    sd_map_settings: _import_settings_pb2.SdMapImportSettings
    def __init__(self, file_path: _Optional[str] = ..., format_name: _Optional[str] = ..., open_drive_settings: _Optional[_Union[_import_settings_pb2.OpenDriveImportSettings, _Mapping]] = ..., roadrunner_hd_map_settings: _Optional[_Union[_import_settings_pb2.RoadRunnerHdMapImportSettings, _Mapping]] = ..., csv_trajectory_settings: _Optional[_Union[_import_settings_pb2.CsvTrajectoryImportSettings, _Mapping]] = ..., sd_map_settings: _Optional[_Union[_import_settings_pb2.SdMapImportSettings, _Mapping]] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExitRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExitResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RoadRunnerStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RoadRunnerStatusResponse(_message.Message):
    __slots__ = ["project_info", "scene_info", "scenario_info", "version"]
    PROJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    project_info: DatasetInfo
    scene_info: DatasetInfo
    scenario_info: DatasetInfo
    version: str
    def __init__(self, project_info: _Optional[_Union[DatasetInfo, _Mapping]] = ..., scene_info: _Optional[_Union[DatasetInfo, _Mapping]] = ..., scenario_info: _Optional[_Union[DatasetInfo, _Mapping]] = ..., version: _Optional[str] = ...) -> None: ...

class DatasetInfo(_message.Message):
    __slots__ = ["unsaved_changes", "file_path"]
    UNSAVED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    unsaved_changes: bool
    file_path: str
    def __init__(self, unsaved_changes: bool = ..., file_path: _Optional[str] = ...) -> None: ...

class RemapAnchorRequest(_message.Message):
    __slots__ = ["source_anchor", "name_remap", "position_remap"]
    SOURCE_ANCHOR_FIELD_NUMBER: _ClassVar[int]
    NAME_REMAP_FIELD_NUMBER: _ClassVar[int]
    POSITION_REMAP_FIELD_NUMBER: _ClassVar[int]
    source_anchor: str
    name_remap: AnchorRemapToName
    position_remap: AnchorRemapToPosition
    def __init__(self, source_anchor: _Optional[str] = ..., name_remap: _Optional[_Union[AnchorRemapToName, _Mapping]] = ..., position_remap: _Optional[_Union[AnchorRemapToPosition, _Mapping]] = ...) -> None: ...

class RemapAnchorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AnchorRemapToName(_message.Message):
    __slots__ = ["target_anchor"]
    TARGET_ANCHOR_FIELD_NUMBER: _ClassVar[int]
    target_anchor: str
    def __init__(self, target_anchor: _Optional[str] = ...) -> None: ...

class AnchorRemapToPosition(_message.Message):
    __slots__ = ["position", "new_anchor_name"]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    NEW_ANCHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    position: _geometry_pb2.Vector3
    new_anchor_name: str
    def __init__(self, position: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ..., new_anchor_name: _Optional[str] = ...) -> None: ...
