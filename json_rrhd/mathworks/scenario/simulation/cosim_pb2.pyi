from mathworks.scenario.common import coordinate_system_pb2 as _coordinate_system_pb2
from mathworks.scenario.scene.hd import hd_map_pb2 as _hd_map_pb2
from mathworks.scenario.scene.hd import hd_map_header_pb2 as _hd_map_header_pb2
from mathworks.scenario.simulation import actor_pb2 as _actor_pb2
from mathworks.scenario.simulation import event_pb2 as _event_pb2
from mathworks.scenario.simulation import logging_pb2 as _logging_pb2
from mathworks.scenario.simulation import phase_status_pb2 as _phase_status_pb2
from mathworks.scenario.simulation import simulation_settings_pb2 as _simulation_settings_pb2
from mathworks.scenario.simulation import simulation_status_pb2 as _simulation_status_pb2
from mathworks.scenario.common import geometry_pb2 as _geometry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationServiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIMULATION_SERVICE_STATUS_UNSPECIFIED: _ClassVar[SimulationServiceStatus]
    SIMULATION_SERVICE_STATUS_NOT_LAUNCHED: _ClassVar[SimulationServiceStatus]
    SIMULATION_SERVICE_STATUS_LAUNCHING: _ClassVar[SimulationServiceStatus]
    SIMULATION_SERVICE_STATUS_LAUNCHED: _ClassVar[SimulationServiceStatus]
    SIMULATION_SERVICE_STATUS_ENDED: _ClassVar[SimulationServiceStatus]
SIMULATION_SERVICE_STATUS_UNSPECIFIED: SimulationServiceStatus
SIMULATION_SERVICE_STATUS_NOT_LAUNCHED: SimulationServiceStatus
SIMULATION_SERVICE_STATUS_LAUNCHING: SimulationServiceStatus
SIMULATION_SERVICE_STATUS_LAUNCHED: SimulationServiceStatus
SIMULATION_SERVICE_STATUS_ENDED: SimulationServiceStatus

class RegisterClientRequest(_message.Message):
    __slots__ = ["proposed_client_id", "name"]
    PROPOSED_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    proposed_client_id: str
    name: str
    def __init__(self, proposed_client_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RegisterClientResponse(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class SetReadyRequest(_message.Message):
    __slots__ = ["client_id"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class SetReadyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetBusyRequest(_message.Message):
    __slots__ = ["client_id", "status"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    status: str
    def __init__(self, client_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class SetBusyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SubscribeEventsRequest(_message.Message):
    __slots__ = ["client_id", "client_profile"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_profile: ClientProfile
    def __init__(self, client_id: _Optional[str] = ..., client_profile: _Optional[_Union[ClientProfile, _Mapping]] = ...) -> None: ...

class ClientProfile(_message.Message):
    __slots__ = ["roadrunner_platform", "simulink_platform", "external_platform", "synchronous", "timeout_milliseconds", "simulate_actors"]
    ROADRUNNER_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SIMULINK_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONOUS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    SIMULATE_ACTORS_FIELD_NUMBER: _ClassVar[int]
    roadrunner_platform: RoadRunnerPlatform
    simulink_platform: SimulinkPlatform
    external_platform: ExternalPlatform
    synchronous: bool
    timeout_milliseconds: int
    simulate_actors: bool
    def __init__(self, roadrunner_platform: _Optional[_Union[RoadRunnerPlatform, _Mapping]] = ..., simulink_platform: _Optional[_Union[SimulinkPlatform, _Mapping]] = ..., external_platform: _Optional[_Union[ExternalPlatform, _Mapping]] = ..., synchronous: bool = ..., timeout_milliseconds: _Optional[int] = ..., simulate_actors: bool = ...) -> None: ...

class RoadRunnerPlatform(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulinkPlatform(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExternalPlatform(_message.Message):
    __slots__ = ["platform_name"]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    platform_name: str
    def __init__(self, platform_name: _Optional[str] = ...) -> None: ...

class AddSimulationsRequest(_message.Message):
    __slots__ = ["simulation_specs"]
    SIMULATION_SPECS_FIELD_NUMBER: _ClassVar[int]
    simulation_specs: _containers.RepeatedCompositeFieldContainer[SimulationSpec]
    def __init__(self, simulation_specs: _Optional[_Iterable[_Union[SimulationSpec, _Mapping]]] = ...) -> None: ...

class AddSimulationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveSimulationsRequest(_message.Message):
    __slots__ = ["is_forced", "simulation_ids"]
    IS_FORCED_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_IDS_FIELD_NUMBER: _ClassVar[int]
    is_forced: bool
    simulation_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_forced: bool = ..., simulation_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoveSimulationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulationSpec(_message.Message):
    __slots__ = ["id", "map_and_header", "world_actor", "simulation_settings"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAP_AND_HEADER_FIELD_NUMBER: _ClassVar[int]
    WORLD_ACTOR_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    map_and_header: MapAndHeader
    world_actor: _actor_pb2.Actor
    simulation_settings: _simulation_settings_pb2.SimulationSettings
    def __init__(self, id: _Optional[str] = ..., map_and_header: _Optional[_Union[MapAndHeader, _Mapping]] = ..., world_actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]] = ..., simulation_settings: _Optional[_Union[_simulation_settings_pb2.SimulationSettings, _Mapping]] = ...) -> None: ...

class GetSimulationServiceProfilesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationServiceProfilesResponse(_message.Message):
    __slots__ = ["simulation_service_profiles"]
    SIMULATION_SERVICE_PROFILES_FIELD_NUMBER: _ClassVar[int]
    simulation_service_profiles: _containers.RepeatedCompositeFieldContainer[SimulationServiceProfile]
    def __init__(self, simulation_service_profiles: _Optional[_Iterable[_Union[SimulationServiceProfile, _Mapping]]] = ...) -> None: ...

class SimulationServiceProfile(_message.Message):
    __slots__ = ["simulation_id", "simulation_service_status", "simulation_service_address", "simulation_service_port"]
    SIMULATION_ID_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SERVICE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
    simulation_id: str
    simulation_service_status: SimulationServiceStatus
    simulation_service_address: str
    simulation_service_port: int
    def __init__(self, simulation_id: _Optional[str] = ..., simulation_service_status: _Optional[_Union[SimulationServiceStatus, str]] = ..., simulation_service_address: _Optional[str] = ..., simulation_service_port: _Optional[int] = ...) -> None: ...

class LaunchSimulationsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LaunchSimulationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResourceSpec(_message.Message):
    __slots__ = ["max_num_cosim", "min_simulation_service_port", "max_simulation_service_port"]
    MAX_NUM_COSIM_FIELD_NUMBER: _ClassVar[int]
    MIN_SIMULATION_SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
    MAX_SIMULATION_SERVICE_PORT_FIELD_NUMBER: _ClassVar[int]
    max_num_cosim: int
    min_simulation_service_port: int
    max_simulation_service_port: int
    def __init__(self, max_num_cosim: _Optional[int] = ..., min_simulation_service_port: _Optional[int] = ..., max_simulation_service_port: _Optional[int] = ...) -> None: ...

class UploadMapRequest(_message.Message):
    __slots__ = ["map_and_header"]
    MAP_AND_HEADER_FIELD_NUMBER: _ClassVar[int]
    map_and_header: MapAndHeader
    def __init__(self, map_and_header: _Optional[_Union[MapAndHeader, _Mapping]] = ...) -> None: ...

class UploadMapResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadMapRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadMapResponse(_message.Message):
    __slots__ = ["map_and_header"]
    MAP_AND_HEADER_FIELD_NUMBER: _ClassVar[int]
    map_and_header: MapAndHeader
    def __init__(self, map_and_header: _Optional[_Union[MapAndHeader, _Mapping]] = ...) -> None: ...

class UploadScenarioRequest(_message.Message):
    __slots__ = ["world_actor"]
    WORLD_ACTOR_FIELD_NUMBER: _ClassVar[int]
    world_actor: _actor_pb2.Actor
    def __init__(self, world_actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]] = ...) -> None: ...

class UploadScenarioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadScenarioRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadScenarioResponse(_message.Message):
    __slots__ = ["world_actor"]
    WORLD_ACTOR_FIELD_NUMBER: _ClassVar[int]
    world_actor: _actor_pb2.Actor
    def __init__(self, world_actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]] = ...) -> None: ...

class SetSimulationSettingsRequest(_message.Message):
    __slots__ = ["simulation_settings"]
    SIMULATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    simulation_settings: _simulation_settings_pb2.SimulationSettings
    def __init__(self, simulation_settings: _Optional[_Union[_simulation_settings_pb2.SimulationSettings, _Mapping]] = ...) -> None: ...

class SetSimulationSettingsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetSimulationPaceRequest(_message.Message):
    __slots__ = ["is_pacer_on", "simulation_pace"]
    IS_PACER_ON_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_PACE_FIELD_NUMBER: _ClassVar[int]
    is_pacer_on: bool
    simulation_pace: float
    def __init__(self, is_pacer_on: bool = ..., simulation_pace: _Optional[float] = ...) -> None: ...

class SetSimulationPaceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationSettingsResponse(_message.Message):
    __slots__ = ["simulation_settings"]
    SIMULATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    simulation_settings: _simulation_settings_pb2.SimulationSettings
    def __init__(self, simulation_settings: _Optional[_Union[_simulation_settings_pb2.SimulationSettings, _Mapping]] = ...) -> None: ...

class StartSimulationRequest(_message.Message):
    __slots__ = ["single_stepping", "normal_mode_simulation", "replay_mode_simulation"]
    SINGLE_STEPPING_FIELD_NUMBER: _ClassVar[int]
    NORMAL_MODE_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    REPLAY_MODE_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    single_stepping: bool
    normal_mode_simulation: NormalModeSimulation
    replay_mode_simulation: ReplayModeSimulation
    def __init__(self, single_stepping: bool = ..., normal_mode_simulation: _Optional[_Union[NormalModeSimulation, _Mapping]] = ..., replay_mode_simulation: _Optional[_Union[ReplayModeSimulation, _Mapping]] = ...) -> None: ...

class NormalModeSimulation(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReplayModeSimulation(_message.Message):
    __slots__ = ["replay_file_path", "excluded_ids"]
    REPLAY_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_IDS_FIELD_NUMBER: _ClassVar[int]
    replay_file_path: str
    excluded_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, replay_file_path: _Optional[str] = ..., excluded_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class StartSimulationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RestartSimulationRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RestartSimulationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StopSimulationRequest(_message.Message):
    __slots__ = ["cause"]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    cause: _simulation_status_pb2.SimulationStopCause
    def __init__(self, cause: _Optional[_Union[_simulation_status_pb2.SimulationStopCause, _Mapping]] = ...) -> None: ...

class StopSimulationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StepSimulationRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StepSimulationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ToggleSimulationPausedRequest(_message.Message):
    __slots__ = ["pause_simulation"]
    PAUSE_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    pause_simulation: bool
    def __init__(self, pause_simulation: bool = ...) -> None: ...

class ToggleSimulationPausedResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationStatusResponse(_message.Message):
    __slots__ = ["simulation_status"]
    SIMULATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    simulation_status: _simulation_status_pb2.SimulationStatus
    def __init__(self, simulation_status: _Optional[_Union[_simulation_status_pb2.SimulationStatus, str]] = ...) -> None: ...

class GetSimulationTimeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSimulationTimeResponse(_message.Message):
    __slots__ = ["simulation_time", "steps"]
    SIMULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    simulation_time: float
    steps: int
    def __init__(self, simulation_time: _Optional[float] = ..., steps: _Optional[int] = ...) -> None: ...

class SetRuntimeActorsRequest(_message.Message):
    __slots__ = ["actor_runtime"]
    ACTOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    actor_runtime: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRuntime]
    def __init__(self, actor_runtime: _Optional[_Iterable[_Union[_actor_pb2.ActorRuntime, _Mapping]]] = ...) -> None: ...

class SetRuntimeActorsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetActorPosesRequest(_message.Message):
    __slots__ = ["actor_poses"]
    ACTOR_POSES_FIELD_NUMBER: _ClassVar[int]
    actor_poses: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorPose]
    def __init__(self, actor_poses: _Optional[_Iterable[_Union[_actor_pb2.ActorPose, _Mapping]]] = ...) -> None: ...

class SetActorPosesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetVehiclePosesRequest(_message.Message):
    __slots__ = ["vehicle_poses"]
    VEHICLE_POSES_FIELD_NUMBER: _ClassVar[int]
    vehicle_poses: _containers.RepeatedCompositeFieldContainer[_actor_pb2.VehiclePose]
    def __init__(self, vehicle_poses: _Optional[_Iterable[_Union[_actor_pb2.VehiclePose, _Mapping]]] = ...) -> None: ...

class SetVehiclePosesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetActorsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetActorsResponse(_message.Message):
    __slots__ = ["actors"]
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[_actor_pb2.Actor]
    def __init__(self, actors: _Optional[_Iterable[_Union[_actor_pb2.Actor, _Mapping]]] = ...) -> None: ...

class GetRuntimeActorsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRuntimeActorsResponse(_message.Message):
    __slots__ = ["actor_runtime"]
    ACTOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    actor_runtime: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorRuntime]
    def __init__(self, actor_runtime: _Optional[_Iterable[_Union[_actor_pb2.ActorRuntime, _Mapping]]] = ...) -> None: ...

class GetActorPosesRequest(_message.Message):
    __slots__ = ["reference_frame", "coordinate_system_ref"]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_SYSTEM_REF_FIELD_NUMBER: _ClassVar[int]
    reference_frame: _actor_pb2.ReferenceFrame
    coordinate_system_ref: _coordinate_system_pb2.CoordinateSystemRef
    def __init__(self, reference_frame: _Optional[_Union[_actor_pb2.ReferenceFrame, str]] = ..., coordinate_system_ref: _Optional[_Union[_coordinate_system_pb2.CoordinateSystemRef, _Mapping]] = ...) -> None: ...

class GetActorPosesResponse(_message.Message):
    __slots__ = ["actor_poses"]
    ACTOR_POSES_FIELD_NUMBER: _ClassVar[int]
    actor_poses: _containers.RepeatedCompositeFieldContainer[_actor_pb2.ActorPose]
    def __init__(self, actor_poses: _Optional[_Iterable[_Union[_actor_pb2.ActorPose, _Mapping]]] = ...) -> None: ...

class GetGeodeticCoordinateRequest(_message.Message):
    __slots__ = ["source_coordinate_system", "source_coordinates"]
    SOURCE_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    source_coordinate_system: _coordinate_system_pb2.CoordinateSystemRef
    source_coordinates: _geometry_pb2.Vector3
    def __init__(self, source_coordinate_system: _Optional[_Union[_coordinate_system_pb2.CoordinateSystemRef, _Mapping]] = ..., source_coordinates: _Optional[_Union[_geometry_pb2.Vector3, _Mapping]] = ...) -> None: ...

class GetGeodeticCoordinateResponse(_message.Message):
    __slots__ = ["geodetic_coordinates"]
    GEODETIC_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    geodetic_coordinates: _coordinate_system_pb2.GeodeticCoordinates
    def __init__(self, geodetic_coordinates: _Optional[_Union[_coordinate_system_pb2.GeodeticCoordinates, _Mapping]] = ...) -> None: ...

class NotifyActionCompleteRequest(_message.Message):
    __slots__ = ["action_id"]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    def __init__(self, action_id: _Optional[str] = ...) -> None: ...

class NotifyActionCompleteResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendEventsRequest(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    def __init__(self, events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ...) -> None: ...

class SendEventsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReceiveEventsRequest(_message.Message):
    __slots__ = ["event_names"]
    EVENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    event_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ReceiveEventsResponse(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    def __init__(self, events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ...) -> None: ...

class GetPhaseStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPhaseStatusResponse(_message.Message):
    __slots__ = ["phase_status"]
    PHASE_STATUS_FIELD_NUMBER: _ClassVar[int]
    phase_status: _containers.RepeatedCompositeFieldContainer[_phase_status_pb2.PhaseStatus]
    def __init__(self, phase_status: _Optional[_Iterable[_Union[_phase_status_pb2.PhaseStatus, _Mapping]]] = ...) -> None: ...

class MapAndHeader(_message.Message):
    __slots__ = ["header", "map"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    header: _hd_map_header_pb2.Header
    map: _hd_map_pb2.HDMap
    def __init__(self, header: _Optional[_Union[_hd_map_header_pb2.Header, _Mapping]] = ..., map: _Optional[_Union[_hd_map_pb2.HDMap, _Mapping]] = ...) -> None: ...

class QueryCommunicationLogRequest(_message.Message):
    __slots__ = ["client_id", "publish_type", "rpc_type", "start_time", "end_time"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TYPE_FIELD_NUMBER: _ClassVar[int]
    RPC_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    publish_type: str
    rpc_type: str
    start_time: _logging_pb2.TimeStamp
    end_time: _logging_pb2.TimeStamp
    def __init__(self, client_id: _Optional[str] = ..., publish_type: _Optional[str] = ..., rpc_type: _Optional[str] = ..., start_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ..., end_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ...) -> None: ...

class QueryCommunicationLogResponse(_message.Message):
    __slots__ = ["communication_log"]
    COMMUNICATION_LOG_FIELD_NUMBER: _ClassVar[int]
    communication_log: _logging_pb2.CommunicationLog
    def __init__(self, communication_log: _Optional[_Union[_logging_pb2.CommunicationLog, _Mapping]] = ...) -> None: ...

class EnableCommunicationLoggingRequest(_message.Message):
    __slots__ = ["log_communication", "log_buffer_length"]
    LOG_COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    LOG_BUFFER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    log_communication: bool
    log_buffer_length: int
    def __init__(self, log_communication: bool = ..., log_buffer_length: _Optional[int] = ...) -> None: ...

class EnableCommunicationLoggingResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryWorldRuntimeLogRequest(_message.Message):
    __slots__ = ["actor_id", "start_time", "end_time"]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    start_time: _logging_pb2.TimeStamp
    end_time: _logging_pb2.TimeStamp
    def __init__(self, actor_id: _Optional[str] = ..., start_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ..., end_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ...) -> None: ...

class QueryWorldRuntimeLogResponse(_message.Message):
    __slots__ = ["world_runtime_state_log"]
    WORLD_RUNTIME_STATE_LOG_FIELD_NUMBER: _ClassVar[int]
    world_runtime_state_log: _logging_pb2.WorldRuntimeStateLog
    def __init__(self, world_runtime_state_log: _Optional[_Union[_logging_pb2.WorldRuntimeStateLog, _Mapping]] = ...) -> None: ...

class EnableWorldRuntimeLoggingRequest(_message.Message):
    __slots__ = ["log_world_runtime", "buffer_length"]
    LOG_WORLD_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    BUFFER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    log_world_runtime: bool
    buffer_length: int
    def __init__(self, log_world_runtime: bool = ..., buffer_length: _Optional[int] = ...) -> None: ...

class EnableWorldRuntimeLoggingResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AddDiagnosticMessageRequest(_message.Message):
    __slots__ = ["diagnostic_messages"]
    DIAGNOSTIC_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    diagnostic_messages: _containers.RepeatedCompositeFieldContainer[_logging_pb2.DiagnosticMessage]
    def __init__(self, diagnostic_messages: _Optional[_Iterable[_Union[_logging_pb2.DiagnosticMessage, _Mapping]]] = ...) -> None: ...

class AddDiagnosticMessageResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryDiagnosticMessageLogRequest(_message.Message):
    __slots__ = ["client_id", "diagnostic_type", "start_time", "end_time"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    diagnostic_type: _logging_pb2.DiagnosticType
    start_time: _logging_pb2.TimeStamp
    end_time: _logging_pb2.TimeStamp
    def __init__(self, client_id: _Optional[str] = ..., diagnostic_type: _Optional[_Union[_logging_pb2.DiagnosticType, str]] = ..., start_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ..., end_time: _Optional[_Union[_logging_pb2.TimeStamp, _Mapping]] = ...) -> None: ...

class QueryDiagnosticMessageLogResponse(_message.Message):
    __slots__ = ["diagnostic_message_log"]
    DIAGNOSTIC_MESSAGE_LOG_FIELD_NUMBER: _ClassVar[int]
    diagnostic_message_log: _logging_pb2.DiagnosticMessageLog
    def __init__(self, diagnostic_message_log: _Optional[_Union[_logging_pb2.DiagnosticMessageLog, _Mapping]] = ...) -> None: ...
