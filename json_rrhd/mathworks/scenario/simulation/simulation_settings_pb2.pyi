from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationSettings(_message.Message):
    __slots__ = ["step_size", "max_simulation_time", "is_pacer_on", "simulation_pace"]
    STEP_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIMULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_PACER_ON_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_PACE_FIELD_NUMBER: _ClassVar[int]
    step_size: float
    max_simulation_time: float
    is_pacer_on: bool
    simulation_pace: float
    def __init__(self, step_size: _Optional[float] = ..., max_simulation_time: _Optional[float] = ..., is_pacer_on: bool = ..., simulation_pace: _Optional[float] = ...) -> None: ...
