# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mathworks/scenario/simulation/cosim.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mathworks.scenario.common import coordinate_system_pb2 as mathworks_dot_scenario_dot_common_dot_coordinate__system__pb2
from mathworks.scenario.scene.hd import hd_map_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__map__pb2
from mathworks.scenario.scene.hd import hd_map_header_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__map__header__pb2
from mathworks.scenario.simulation import actor_pb2 as mathworks_dot_scenario_dot_simulation_dot_actor__pb2
from mathworks.scenario.simulation import event_pb2 as mathworks_dot_scenario_dot_simulation_dot_event__pb2
from mathworks.scenario.simulation import logging_pb2 as mathworks_dot_scenario_dot_simulation_dot_logging__pb2
from mathworks.scenario.simulation import phase_status_pb2 as mathworks_dot_scenario_dot_simulation_dot_phase__status__pb2
from mathworks.scenario.simulation import simulation_settings_pb2 as mathworks_dot_scenario_dot_simulation_dot_simulation__settings__pb2
from mathworks.scenario.simulation import simulation_status_pb2 as mathworks_dot_scenario_dot_simulation_dot_simulation__status__pb2
from mathworks.scenario.common import geometry_pb2 as mathworks_dot_scenario_dot_common_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)mathworks/scenario/simulation/cosim.proto\x12\x1dmathworks.scenario.simulation\x1a\x31mathworks/scenario/common/coordinate_system.proto\x1a(mathworks/scenario/scene/hd/hd_map.proto\x1a/mathworks/scenario/scene/hd/hd_map_header.proto\x1a)mathworks/scenario/simulation/actor.proto\x1a)mathworks/scenario/simulation/event.proto\x1a+mathworks/scenario/simulation/logging.proto\x1a\x30mathworks/scenario/simulation/phase_status.proto\x1a\x37mathworks/scenario/simulation/simulation_settings.proto\x1a\x35mathworks/scenario/simulation/simulation_status.proto\x1a(mathworks/scenario/common/geometry.proto\"A\n\x15RegisterClientRequest\x12\x1a\n\x12proposed_client_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"+\n\x16RegisterClientResponse\x12\x11\n\tclient_id\x18\x01 \x01(\t\"$\n\x0fSetReadyRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x12\n\x10SetReadyResponse\"3\n\x0eSetBusyRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x11\n\x0fSetBusyResponse\"q\n\x16SubscribeEventsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x44\n\x0e\x63lient_profile\x18\x02 \x01(\x0b\x32,.mathworks.scenario.simulation.ClientProfile\"\xda\x02\n\rClientProfile\x12P\n\x13roadrunner_platform\x18\x01 \x01(\x0b\x32\x31.mathworks.scenario.simulation.RoadRunnerPlatformH\x00\x12L\n\x11simulink_platform\x18\x02 \x01(\x0b\x32/.mathworks.scenario.simulation.SimulinkPlatformH\x00\x12L\n\x11\x65xternal_platform\x18\x03 \x01(\x0b\x32/.mathworks.scenario.simulation.ExternalPlatformH\x00\x12\x13\n\x0bsynchronous\x18\x04 \x01(\x08\x12\x1c\n\x14timeout_milliseconds\x18\x05 \x01(\r\x12\x17\n\x0fsimulate_actors\x18\x06 \x01(\x08\x42\x0f\n\rplatform_type\"\x14\n\x12RoadRunnerPlatform\"\x12\n\x10SimulinkPlatform\")\n\x10\x45xternalPlatform\x12\x15\n\rplatform_name\x18\x01 \x01(\t\"`\n\x15\x41\x64\x64SimulationsRequest\x12G\n\x10simulation_specs\x18\x01 \x03(\x0b\x32-.mathworks.scenario.simulation.SimulationSpec\"\x18\n\x16\x41\x64\x64SimulationsResponse\"E\n\x18RemoveSimulationsRequest\x12\x11\n\tis_forced\x18\x01 \x01(\x08\x12\x16\n\x0esimulation_ids\x18\x02 \x03(\t\"\x1b\n\x19RemoveSimulationsResponse\"\xec\x01\n\x0eSimulationSpec\x12\n\n\x02id\x18\x01 \x01(\t\x12\x43\n\x0emap_and_header\x18\x02 \x01(\x0b\x32+.mathworks.scenario.simulation.MapAndHeader\x12\x39\n\x0bworld_actor\x18\x03 \x01(\x0b\x32$.mathworks.scenario.simulation.Actor\x12N\n\x13simulation_settings\x18\x04 \x01(\x0b\x32\x31.mathworks.scenario.simulation.SimulationSettings\"%\n#GetSimulationServiceProfilesRequest\"\x84\x01\n$GetSimulationServiceProfilesResponse\x12\\\n\x1bsimulation_service_profiles\x18\x01 \x03(\x0b\x32\x37.mathworks.scenario.simulation.SimulationServiceProfile\"\xd1\x01\n\x18SimulationServiceProfile\x12\x15\n\rsimulation_id\x18\x01 \x01(\t\x12Y\n\x19simulation_service_status\x18\x02 \x01(\x0e\x32\x36.mathworks.scenario.simulation.SimulationServiceStatus\x12\"\n\x1asimulation_service_address\x18\x03 \x01(\t\x12\x1f\n\x17simulation_service_port\x18\x04 \x01(\r\"\x1a\n\x18LaunchSimulationsRequest\"\x1b\n\x19LaunchSimulationsResponse\"o\n\x0cResourceSpec\x12\x15\n\rmax_num_cosim\x18\x01 \x01(\r\x12#\n\x1bmin_simulation_service_port\x18\x02 \x01(\r\x12#\n\x1bmax_simulation_service_port\x18\x03 \x01(\r\"W\n\x10UploadMapRequest\x12\x43\n\x0emap_and_header\x18\x01 \x01(\x0b\x32+.mathworks.scenario.simulation.MapAndHeader\"\x13\n\x11UploadMapResponse\"\x14\n\x12\x44ownloadMapRequest\"Z\n\x13\x44ownloadMapResponse\x12\x43\n\x0emap_and_header\x18\x01 \x01(\x0b\x32+.mathworks.scenario.simulation.MapAndHeader\"R\n\x15UploadScenarioRequest\x12\x39\n\x0bworld_actor\x18\x01 \x01(\x0b\x32$.mathworks.scenario.simulation.Actor\"\x18\n\x16UploadScenarioResponse\"\x19\n\x17\x44ownloadScenarioRequest\"U\n\x18\x44ownloadScenarioResponse\x12\x39\n\x0bworld_actor\x18\x01 \x01(\x0b\x32$.mathworks.scenario.simulation.Actor\"n\n\x1cSetSimulationSettingsRequest\x12N\n\x13simulation_settings\x18\x01 \x01(\x0b\x32\x31.mathworks.scenario.simulation.SimulationSettings\"\x1f\n\x1dSetSimulationSettingsResponse\"H\n\x18SetSimulationPaceRequest\x12\x13\n\x0bis_pacer_on\x18\x01 \x01(\x08\x12\x17\n\x0fsimulation_pace\x18\x02 \x01(\x01\"\x1b\n\x19SetSimulationPaceResponse\"\x1e\n\x1cGetSimulationSettingsRequest\"o\n\x1dGetSimulationSettingsResponse\x12N\n\x13simulation_settings\x18\x01 \x01(\x0b\x32\x31.mathworks.scenario.simulation.SimulationSettings\"\xf2\x01\n\x16StartSimulationRequest\x12\x17\n\x0fsingle_stepping\x18\x01 \x01(\x08\x12U\n\x16normal_mode_simulation\x18\x65 \x01(\x0b\x32\x33.mathworks.scenario.simulation.NormalModeSimulationH\x00\x12U\n\x16replay_mode_simulation\x18\x66 \x01(\x0b\x32\x33.mathworks.scenario.simulation.ReplayModeSimulationH\x00\x42\x11\n\x0fsimulation_mode\"\x16\n\x14NormalModeSimulation\"F\n\x14ReplayModeSimulation\x12\x18\n\x10replay_file_path\x18\x01 \x01(\t\x12\x14\n\x0c\x65xcluded_ids\x18\x02 \x03(\t\"\x19\n\x17StartSimulationResponse\"\x1a\n\x18RestartSimulationRequest\"\x1b\n\x19RestartSimulationResponse\"Z\n\x15StopSimulationRequest\x12\x41\n\x05\x63\x61use\x18\x01 \x01(\x0b\x32\x32.mathworks.scenario.simulation.SimulationStopCause\"\x18\n\x16StopSimulationResponse\"\x17\n\x15StepSimulationRequest\"\x18\n\x16StepSimulationResponse\"9\n\x1dToggleSimulationPausedRequest\x12\x18\n\x10pause_simulation\x18\x01 \x01(\x08\" \n\x1eToggleSimulationPausedResponse\"\x1c\n\x1aGetSimulationStatusRequest\"i\n\x1bGetSimulationStatusResponse\x12J\n\x11simulation_status\x18\x01 \x01(\x0e\x32/.mathworks.scenario.simulation.SimulationStatus\"\x1a\n\x18GetSimulationTimeRequest\"C\n\x19GetSimulationTimeResponse\x12\x17\n\x0fsimulation_time\x18\x01 \x01(\x01\x12\r\n\x05steps\x18\x02 \x01(\x03\"]\n\x17SetRuntimeActorsRequest\x12\x42\n\ractor_runtime\x18\x01 \x03(\x0b\x32+.mathworks.scenario.simulation.ActorRuntime\"\x1a\n\x18SetRuntimeActorsResponse\"U\n\x14SetActorPosesRequest\x12=\n\x0b\x61\x63tor_poses\x18\x01 \x03(\x0b\x32(.mathworks.scenario.simulation.ActorPose\"\x17\n\x15SetActorPosesResponse\"[\n\x16SetVehiclePosesRequest\x12\x41\n\rvehicle_poses\x18\x01 \x03(\x0b\x32*.mathworks.scenario.simulation.VehiclePose\"\x19\n\x17SetVehiclePosesResponse\"\x12\n\x10GetActorsRequest\"I\n\x11GetActorsResponse\x12\x34\n\x06\x61\x63tors\x18\x01 \x03(\x0b\x32$.mathworks.scenario.simulation.Actor\"\x19\n\x17GetRuntimeActorsRequest\"^\n\x18GetRuntimeActorsResponse\x12\x42\n\ractor_runtime\x18\x01 \x03(\x0b\x32+.mathworks.scenario.simulation.ActorRuntime\"\xad\x01\n\x14GetActorPosesRequest\x12\x46\n\x0freference_frame\x18\x01 \x01(\x0e\x32-.mathworks.scenario.simulation.ReferenceFrame\x12M\n\x15\x63oordinate_system_ref\x18\x02 \x01(\x0b\x32..mathworks.scenario.common.CoordinateSystemRef\"V\n\x15GetActorPosesResponse\x12=\n\x0b\x61\x63tor_poses\x18\x01 \x03(\x0b\x32(.mathworks.scenario.simulation.ActorPose\"\xb0\x01\n\x1cGetGeodeticCoordinateRequest\x12P\n\x18source_coordinate_system\x18\x01 \x01(\x0b\x32..mathworks.scenario.common.CoordinateSystemRef\x12>\n\x12source_coordinates\x18\x02 \x01(\x0b\x32\".mathworks.scenario.common.Vector3\"m\n\x1dGetGeodeticCoordinateResponse\x12L\n\x14geodetic_coordinates\x18\x01 \x01(\x0b\x32..mathworks.scenario.common.GeodeticCoordinates\"0\n\x1bNotifyActionCompleteRequest\x12\x11\n\taction_id\x18\x01 \x01(\t\"\x1e\n\x1cNotifyActionCompleteResponse\"I\n\x11SendEventsRequest\x12\x34\n\x06\x65vents\x18\x01 \x03(\x0b\x32$.mathworks.scenario.simulation.Event\"\x14\n\x12SendEventsResponse\"+\n\x14ReceiveEventsRequest\x12\x13\n\x0b\x65vent_names\x18\x01 \x03(\t\"M\n\x15ReceiveEventsResponse\x12\x34\n\x06\x65vents\x18\x01 \x03(\x0b\x32$.mathworks.scenario.simulation.Event\"\x17\n\x15GetPhaseStatusRequest\"Z\n\x16GetPhaseStatusResponse\x12@\n\x0cphase_status\x18\x01 \x03(\x0b\x32*.mathworks.scenario.simulation.PhaseStatus\"z\n\x0cMapAndHeader\x12\x36\n\x06header\x18\x01 \x01(\x0b\x32&.mathworks.scenario.scene.hdmap.Header\x12\x32\n\x03map\x18\x02 \x01(\x0b\x32%.mathworks.scenario.scene.hdmap.HDMap\"\xd3\x01\n\x1cQueryCommunicationLogRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x14\n\x0cpublish_type\x18\x02 \x01(\t\x12\x10\n\x08rpc_type\x18\x03 \x01(\t\x12<\n\nstart_time\x18\x04 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\x12:\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\"k\n\x1dQueryCommunicationLogResponse\x12J\n\x11\x63ommunication_log\x18\x01 \x01(\x0b\x32/.mathworks.scenario.simulation.CommunicationLog\"Y\n!EnableCommunicationLoggingRequest\x12\x19\n\x11log_communication\x18\x01 \x01(\x08\x12\x19\n\x11log_buffer_length\x18\x02 \x01(\r\"$\n\"EnableCommunicationLoggingResponse\"\xa9\x01\n\x1bQueryWorldRuntimeLogRequest\x12\x10\n\x08\x61\x63tor_id\x18\x01 \x01(\t\x12<\n\nstart_time\x18\x02 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\x12:\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\"t\n\x1cQueryWorldRuntimeLogResponse\x12T\n\x17world_runtime_state_log\x18\x01 \x01(\x0b\x32\x33.mathworks.scenario.simulation.WorldRuntimeStateLog\"T\n EnableWorldRuntimeLoggingRequest\x12\x19\n\x11log_world_runtime\x18\x01 \x01(\x08\x12\x15\n\rbuffer_length\x18\x02 \x01(\r\"#\n!EnableWorldRuntimeLoggingResponse\"l\n\x1b\x41\x64\x64\x44iagnosticMessageRequest\x12M\n\x13\x64iagnostic_messages\x18\x01 \x03(\x0b\x32\x30.mathworks.scenario.simulation.DiagnosticMessage\"\x1e\n\x1c\x41\x64\x64\x44iagnosticMessageResponse\"\xf7\x01\n QueryDiagnosticMessageLogRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x46\n\x0f\x64iagnostic_type\x18\x02 \x01(\x0e\x32-.mathworks.scenario.simulation.DiagnosticType\x12<\n\nstart_time\x18\x03 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\x12:\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32(.mathworks.scenario.simulation.TimeStamp\"x\n!QueryDiagnosticMessageLogResponse\x12S\n\x16\x64iagnostic_message_log\x18\x01 \x01(\x0b\x32\x33.mathworks.scenario.simulation.DiagnosticMessageLog*\xe6\x01\n\x17SimulationServiceStatus\x12)\n%SIMULATION_SERVICE_STATUS_UNSPECIFIED\x10\x00\x12*\n&SIMULATION_SERVICE_STATUS_NOT_LAUNCHED\x10\x01\x12\'\n#SIMULATION_SERVICE_STATUS_LAUNCHING\x10\x02\x12&\n\"SIMULATION_SERVICE_STATUS_LAUNCHED\x10\x03\x12#\n\x1fSIMULATION_SERVICE_STATUS_ENDED\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mathworks.scenario.simulation.cosim_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SIMULATIONSERVICESTATUS']._serialized_start=7176
  _globals['_SIMULATIONSERVICESTATUS']._serialized_end=7406
  _globals['_REGISTERCLIENTREQUEST']._serialized_start=553
  _globals['_REGISTERCLIENTREQUEST']._serialized_end=618
  _globals['_REGISTERCLIENTRESPONSE']._serialized_start=620
  _globals['_REGISTERCLIENTRESPONSE']._serialized_end=663
  _globals['_SETREADYREQUEST']._serialized_start=665
  _globals['_SETREADYREQUEST']._serialized_end=701
  _globals['_SETREADYRESPONSE']._serialized_start=703
  _globals['_SETREADYRESPONSE']._serialized_end=721
  _globals['_SETBUSYREQUEST']._serialized_start=723
  _globals['_SETBUSYREQUEST']._serialized_end=774
  _globals['_SETBUSYRESPONSE']._serialized_start=776
  _globals['_SETBUSYRESPONSE']._serialized_end=793
  _globals['_SUBSCRIBEEVENTSREQUEST']._serialized_start=795
  _globals['_SUBSCRIBEEVENTSREQUEST']._serialized_end=908
  _globals['_CLIENTPROFILE']._serialized_start=911
  _globals['_CLIENTPROFILE']._serialized_end=1257
  _globals['_ROADRUNNERPLATFORM']._serialized_start=1259
  _globals['_ROADRUNNERPLATFORM']._serialized_end=1279
  _globals['_SIMULINKPLATFORM']._serialized_start=1281
  _globals['_SIMULINKPLATFORM']._serialized_end=1299
  _globals['_EXTERNALPLATFORM']._serialized_start=1301
  _globals['_EXTERNALPLATFORM']._serialized_end=1342
  _globals['_ADDSIMULATIONSREQUEST']._serialized_start=1344
  _globals['_ADDSIMULATIONSREQUEST']._serialized_end=1440
  _globals['_ADDSIMULATIONSRESPONSE']._serialized_start=1442
  _globals['_ADDSIMULATIONSRESPONSE']._serialized_end=1466
  _globals['_REMOVESIMULATIONSREQUEST']._serialized_start=1468
  _globals['_REMOVESIMULATIONSREQUEST']._serialized_end=1537
  _globals['_REMOVESIMULATIONSRESPONSE']._serialized_start=1539
  _globals['_REMOVESIMULATIONSRESPONSE']._serialized_end=1566
  _globals['_SIMULATIONSPEC']._serialized_start=1569
  _globals['_SIMULATIONSPEC']._serialized_end=1805
  _globals['_GETSIMULATIONSERVICEPROFILESREQUEST']._serialized_start=1807
  _globals['_GETSIMULATIONSERVICEPROFILESREQUEST']._serialized_end=1844
  _globals['_GETSIMULATIONSERVICEPROFILESRESPONSE']._serialized_start=1847
  _globals['_GETSIMULATIONSERVICEPROFILESRESPONSE']._serialized_end=1979
  _globals['_SIMULATIONSERVICEPROFILE']._serialized_start=1982
  _globals['_SIMULATIONSERVICEPROFILE']._serialized_end=2191
  _globals['_LAUNCHSIMULATIONSREQUEST']._serialized_start=2193
  _globals['_LAUNCHSIMULATIONSREQUEST']._serialized_end=2219
  _globals['_LAUNCHSIMULATIONSRESPONSE']._serialized_start=2221
  _globals['_LAUNCHSIMULATIONSRESPONSE']._serialized_end=2248
  _globals['_RESOURCESPEC']._serialized_start=2250
  _globals['_RESOURCESPEC']._serialized_end=2361
  _globals['_UPLOADMAPREQUEST']._serialized_start=2363
  _globals['_UPLOADMAPREQUEST']._serialized_end=2450
  _globals['_UPLOADMAPRESPONSE']._serialized_start=2452
  _globals['_UPLOADMAPRESPONSE']._serialized_end=2471
  _globals['_DOWNLOADMAPREQUEST']._serialized_start=2473
  _globals['_DOWNLOADMAPREQUEST']._serialized_end=2493
  _globals['_DOWNLOADMAPRESPONSE']._serialized_start=2495
  _globals['_DOWNLOADMAPRESPONSE']._serialized_end=2585
  _globals['_UPLOADSCENARIOREQUEST']._serialized_start=2587
  _globals['_UPLOADSCENARIOREQUEST']._serialized_end=2669
  _globals['_UPLOADSCENARIORESPONSE']._serialized_start=2671
  _globals['_UPLOADSCENARIORESPONSE']._serialized_end=2695
  _globals['_DOWNLOADSCENARIOREQUEST']._serialized_start=2697
  _globals['_DOWNLOADSCENARIOREQUEST']._serialized_end=2722
  _globals['_DOWNLOADSCENARIORESPONSE']._serialized_start=2724
  _globals['_DOWNLOADSCENARIORESPONSE']._serialized_end=2809
  _globals['_SETSIMULATIONSETTINGSREQUEST']._serialized_start=2811
  _globals['_SETSIMULATIONSETTINGSREQUEST']._serialized_end=2921
  _globals['_SETSIMULATIONSETTINGSRESPONSE']._serialized_start=2923
  _globals['_SETSIMULATIONSETTINGSRESPONSE']._serialized_end=2954
  _globals['_SETSIMULATIONPACEREQUEST']._serialized_start=2956
  _globals['_SETSIMULATIONPACEREQUEST']._serialized_end=3028
  _globals['_SETSIMULATIONPACERESPONSE']._serialized_start=3030
  _globals['_SETSIMULATIONPACERESPONSE']._serialized_end=3057
  _globals['_GETSIMULATIONSETTINGSREQUEST']._serialized_start=3059
  _globals['_GETSIMULATIONSETTINGSREQUEST']._serialized_end=3089
  _globals['_GETSIMULATIONSETTINGSRESPONSE']._serialized_start=3091
  _globals['_GETSIMULATIONSETTINGSRESPONSE']._serialized_end=3202
  _globals['_STARTSIMULATIONREQUEST']._serialized_start=3205
  _globals['_STARTSIMULATIONREQUEST']._serialized_end=3447
  _globals['_NORMALMODESIMULATION']._serialized_start=3449
  _globals['_NORMALMODESIMULATION']._serialized_end=3471
  _globals['_REPLAYMODESIMULATION']._serialized_start=3473
  _globals['_REPLAYMODESIMULATION']._serialized_end=3543
  _globals['_STARTSIMULATIONRESPONSE']._serialized_start=3545
  _globals['_STARTSIMULATIONRESPONSE']._serialized_end=3570
  _globals['_RESTARTSIMULATIONREQUEST']._serialized_start=3572
  _globals['_RESTARTSIMULATIONREQUEST']._serialized_end=3598
  _globals['_RESTARTSIMULATIONRESPONSE']._serialized_start=3600
  _globals['_RESTARTSIMULATIONRESPONSE']._serialized_end=3627
  _globals['_STOPSIMULATIONREQUEST']._serialized_start=3629
  _globals['_STOPSIMULATIONREQUEST']._serialized_end=3719
  _globals['_STOPSIMULATIONRESPONSE']._serialized_start=3721
  _globals['_STOPSIMULATIONRESPONSE']._serialized_end=3745
  _globals['_STEPSIMULATIONREQUEST']._serialized_start=3747
  _globals['_STEPSIMULATIONREQUEST']._serialized_end=3770
  _globals['_STEPSIMULATIONRESPONSE']._serialized_start=3772
  _globals['_STEPSIMULATIONRESPONSE']._serialized_end=3796
  _globals['_TOGGLESIMULATIONPAUSEDREQUEST']._serialized_start=3798
  _globals['_TOGGLESIMULATIONPAUSEDREQUEST']._serialized_end=3855
  _globals['_TOGGLESIMULATIONPAUSEDRESPONSE']._serialized_start=3857
  _globals['_TOGGLESIMULATIONPAUSEDRESPONSE']._serialized_end=3889
  _globals['_GETSIMULATIONSTATUSREQUEST']._serialized_start=3891
  _globals['_GETSIMULATIONSTATUSREQUEST']._serialized_end=3919
  _globals['_GETSIMULATIONSTATUSRESPONSE']._serialized_start=3921
  _globals['_GETSIMULATIONSTATUSRESPONSE']._serialized_end=4026
  _globals['_GETSIMULATIONTIMEREQUEST']._serialized_start=4028
  _globals['_GETSIMULATIONTIMEREQUEST']._serialized_end=4054
  _globals['_GETSIMULATIONTIMERESPONSE']._serialized_start=4056
  _globals['_GETSIMULATIONTIMERESPONSE']._serialized_end=4123
  _globals['_SETRUNTIMEACTORSREQUEST']._serialized_start=4125
  _globals['_SETRUNTIMEACTORSREQUEST']._serialized_end=4218
  _globals['_SETRUNTIMEACTORSRESPONSE']._serialized_start=4220
  _globals['_SETRUNTIMEACTORSRESPONSE']._serialized_end=4246
  _globals['_SETACTORPOSESREQUEST']._serialized_start=4248
  _globals['_SETACTORPOSESREQUEST']._serialized_end=4333
  _globals['_SETACTORPOSESRESPONSE']._serialized_start=4335
  _globals['_SETACTORPOSESRESPONSE']._serialized_end=4358
  _globals['_SETVEHICLEPOSESREQUEST']._serialized_start=4360
  _globals['_SETVEHICLEPOSESREQUEST']._serialized_end=4451
  _globals['_SETVEHICLEPOSESRESPONSE']._serialized_start=4453
  _globals['_SETVEHICLEPOSESRESPONSE']._serialized_end=4478
  _globals['_GETACTORSREQUEST']._serialized_start=4480
  _globals['_GETACTORSREQUEST']._serialized_end=4498
  _globals['_GETACTORSRESPONSE']._serialized_start=4500
  _globals['_GETACTORSRESPONSE']._serialized_end=4573
  _globals['_GETRUNTIMEACTORSREQUEST']._serialized_start=4575
  _globals['_GETRUNTIMEACTORSREQUEST']._serialized_end=4600
  _globals['_GETRUNTIMEACTORSRESPONSE']._serialized_start=4602
  _globals['_GETRUNTIMEACTORSRESPONSE']._serialized_end=4696
  _globals['_GETACTORPOSESREQUEST']._serialized_start=4699
  _globals['_GETACTORPOSESREQUEST']._serialized_end=4872
  _globals['_GETACTORPOSESRESPONSE']._serialized_start=4874
  _globals['_GETACTORPOSESRESPONSE']._serialized_end=4960
  _globals['_GETGEODETICCOORDINATEREQUEST']._serialized_start=4963
  _globals['_GETGEODETICCOORDINATEREQUEST']._serialized_end=5139
  _globals['_GETGEODETICCOORDINATERESPONSE']._serialized_start=5141
  _globals['_GETGEODETICCOORDINATERESPONSE']._serialized_end=5250
  _globals['_NOTIFYACTIONCOMPLETEREQUEST']._serialized_start=5252
  _globals['_NOTIFYACTIONCOMPLETEREQUEST']._serialized_end=5300
  _globals['_NOTIFYACTIONCOMPLETERESPONSE']._serialized_start=5302
  _globals['_NOTIFYACTIONCOMPLETERESPONSE']._serialized_end=5332
  _globals['_SENDEVENTSREQUEST']._serialized_start=5334
  _globals['_SENDEVENTSREQUEST']._serialized_end=5407
  _globals['_SENDEVENTSRESPONSE']._serialized_start=5409
  _globals['_SENDEVENTSRESPONSE']._serialized_end=5429
  _globals['_RECEIVEEVENTSREQUEST']._serialized_start=5431
  _globals['_RECEIVEEVENTSREQUEST']._serialized_end=5474
  _globals['_RECEIVEEVENTSRESPONSE']._serialized_start=5476
  _globals['_RECEIVEEVENTSRESPONSE']._serialized_end=5553
  _globals['_GETPHASESTATUSREQUEST']._serialized_start=5555
  _globals['_GETPHASESTATUSREQUEST']._serialized_end=5578
  _globals['_GETPHASESTATUSRESPONSE']._serialized_start=5580
  _globals['_GETPHASESTATUSRESPONSE']._serialized_end=5670
  _globals['_MAPANDHEADER']._serialized_start=5672
  _globals['_MAPANDHEADER']._serialized_end=5794
  _globals['_QUERYCOMMUNICATIONLOGREQUEST']._serialized_start=5797
  _globals['_QUERYCOMMUNICATIONLOGREQUEST']._serialized_end=6008
  _globals['_QUERYCOMMUNICATIONLOGRESPONSE']._serialized_start=6010
  _globals['_QUERYCOMMUNICATIONLOGRESPONSE']._serialized_end=6117
  _globals['_ENABLECOMMUNICATIONLOGGINGREQUEST']._serialized_start=6119
  _globals['_ENABLECOMMUNICATIONLOGGINGREQUEST']._serialized_end=6208
  _globals['_ENABLECOMMUNICATIONLOGGINGRESPONSE']._serialized_start=6210
  _globals['_ENABLECOMMUNICATIONLOGGINGRESPONSE']._serialized_end=6246
  _globals['_QUERYWORLDRUNTIMELOGREQUEST']._serialized_start=6249
  _globals['_QUERYWORLDRUNTIMELOGREQUEST']._serialized_end=6418
  _globals['_QUERYWORLDRUNTIMELOGRESPONSE']._serialized_start=6420
  _globals['_QUERYWORLDRUNTIMELOGRESPONSE']._serialized_end=6536
  _globals['_ENABLEWORLDRUNTIMELOGGINGREQUEST']._serialized_start=6538
  _globals['_ENABLEWORLDRUNTIMELOGGINGREQUEST']._serialized_end=6622
  _globals['_ENABLEWORLDRUNTIMELOGGINGRESPONSE']._serialized_start=6624
  _globals['_ENABLEWORLDRUNTIMELOGGINGRESPONSE']._serialized_end=6659
  _globals['_ADDDIAGNOSTICMESSAGEREQUEST']._serialized_start=6661
  _globals['_ADDDIAGNOSTICMESSAGEREQUEST']._serialized_end=6769
  _globals['_ADDDIAGNOSTICMESSAGERESPONSE']._serialized_start=6771
  _globals['_ADDDIAGNOSTICMESSAGERESPONSE']._serialized_end=6801
  _globals['_QUERYDIAGNOSTICMESSAGELOGREQUEST']._serialized_start=6804
  _globals['_QUERYDIAGNOSTICMESSAGELOGREQUEST']._serialized_end=7051
  _globals['_QUERYDIAGNOSTICMESSAGELOGRESPONSE']._serialized_start=7053
  _globals['_QUERYDIAGNOSTICMESSAGELOGRESPONSE']._serialized_end=7173
# @@protoc_insertion_point(module_scope)
