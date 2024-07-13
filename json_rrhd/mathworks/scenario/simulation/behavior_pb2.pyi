from mathworks.scenario.simulation import attributes_pb2 as _attributes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BehaviorFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BEHAVIOR_FORMAT_UNSPECIFIED: _ClassVar[BehaviorFormat]
    BEHAVIOR_FORMAT_SIMULINK_MODEL: _ClassVar[BehaviorFormat]
    BEHAVIOR_FORMAT_MATLAB_SYSTEM_OBJECT: _ClassVar[BehaviorFormat]

class SimulationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIMULATION_MODE_UNSPECIFIED: _ClassVar[SimulationMode]
    SIMULATION_MODE_INTERPRETED: _ClassVar[SimulationMode]
    SIMULATION_MODE_ACCELERATED: _ClassVar[SimulationMode]
BEHAVIOR_FORMAT_UNSPECIFIED: BehaviorFormat
BEHAVIOR_FORMAT_SIMULINK_MODEL: BehaviorFormat
BEHAVIOR_FORMAT_MATLAB_SYSTEM_OBJECT: BehaviorFormat
SIMULATION_MODE_UNSPECIFIED: SimulationMode
SIMULATION_MODE_INTERPRETED: SimulationMode
SIMULATION_MODE_ACCELERATED: SimulationMode

class Behavior(_message.Message):
    __slots__ = ["id", "asset_reference", "parameters", "roadrunner_behavior", "simulink_behavior", "external_behavior", "no_behavior"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ROADRUNNER_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    SIMULINK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    NO_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_reference: str
    parameters: _containers.RepeatedCompositeFieldContainer[_attributes_pb2.Attribute]
    roadrunner_behavior: RoadRunnerBehavior
    simulink_behavior: SimulinkBehavior
    external_behavior: ExternalBehavior
    no_behavior: NoBehavior
    def __init__(self, id: _Optional[str] = ..., asset_reference: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_attributes_pb2.Attribute, _Mapping]]] = ..., roadrunner_behavior: _Optional[_Union[RoadRunnerBehavior, _Mapping]] = ..., simulink_behavior: _Optional[_Union[SimulinkBehavior, _Mapping]] = ..., external_behavior: _Optional[_Union[ExternalBehavior, _Mapping]] = ..., no_behavior: _Optional[_Union[NoBehavior, _Mapping]] = ...) -> None: ...

class RoadRunnerBehavior(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimulinkBehavior(_message.Message):
    __slots__ = ["artifact_location", "behavior_format", "simulation_mode"]
    ARTIFACT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_MODE_FIELD_NUMBER: _ClassVar[int]
    artifact_location: str
    behavior_format: BehaviorFormat
    simulation_mode: SimulationMode
    def __init__(self, artifact_location: _Optional[str] = ..., behavior_format: _Optional[_Union[BehaviorFormat, str]] = ..., simulation_mode: _Optional[_Union[SimulationMode, str]] = ...) -> None: ...

class ExternalBehavior(_message.Message):
    __slots__ = ["platform_name", "model_location"]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    platform_name: str
    model_location: str
    def __init__(self, platform_name: _Optional[str] = ..., model_location: _Optional[str] = ...) -> None: ...

class NoBehavior(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
