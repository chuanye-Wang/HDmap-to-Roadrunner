# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mathworks/scenario/simulation/scenario.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mathworks.scenario.simulation import action_pb2 as mathworks_dot_scenario_dot_simulation_dot_action__pb2
from mathworks.scenario.simulation import condition_pb2 as mathworks_dot_scenario_dot_simulation_dot_condition__pb2
from mathworks.scenario.simulation import custom_command_pb2 as mathworks_dot_scenario_dot_simulation_dot_custom__command__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,mathworks/scenario/simulation/scenario.proto\x12\x1dmathworks.scenario.simulation\x1a*mathworks/scenario/simulation/action.proto\x1a-mathworks/scenario/simulation/condition.proto\x1a\x32mathworks/scenario/simulation/custom_command.proto\"\xcf\x01\n\x08Scenario\x12\x38\n\nroot_phase\x18\x01 \x01(\x0b\x32$.mathworks.scenario.simulation.Phase\x12\x43\n\rcustom_events\x18\x02 \x03(\x0b\x32,.mathworks.scenario.simulation.CustomCommand\x12\x44\n\x0e\x63ustom_actions\x18\x03 \x03(\x0b\x32,.mathworks.scenario.simulation.CustomCommand\"\xf9\x02\n\x05Phase\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x41\n\x0fstart_condition\x18\x03 \x01(\x0b\x32(.mathworks.scenario.simulation.Condition\x12?\n\rend_condition\x18\x04 \x01(\x0b\x32(.mathworks.scenario.simulation.Condition\x12<\n\x0esystem_actions\x18\x06 \x03(\x0b\x32$.mathworks.scenario.simulation.Phase\x12H\n\x0f\x63omposite_phase\x18\x65 \x01(\x0b\x32-.mathworks.scenario.simulation.CompositePhaseH\x00\x12\x42\n\x0c\x61\x63tion_phase\x18\x66 \x01(\x0b\x32*.mathworks.scenario.simulation.ActionPhaseH\x00\x42\x06\n\x04type\"\xd2\x01\n\x0e\x43ompositePhase\x12\x36\n\x08\x63hildren\x18\x01 \x03(\x0b\x32$.mathworks.scenario.simulation.Phase\x12\x42\n\x0cserial_phase\x18\x65 \x01(\x0b\x32*.mathworks.scenario.simulation.SerialPhaseH\x00\x12<\n\tmix_phase\x18\x66 \x01(\x0b\x32\'.mathworks.scenario.simulation.MixPhaseH\x00\x42\x06\n\x04type\"\r\n\x0bSerialPhase\"\n\n\x08MixPhase\"\xed\x01\n\x0b\x41\x63tionPhase\x12\x36\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32%.mathworks.scenario.simulation.Action\x12M\n\x12\x61\x63tor_action_phase\x18\x65 \x01(\x0b\x32/.mathworks.scenario.simulation.ActorActionPhaseH\x00\x12O\n\x13system_action_phase\x18\x66 \x01(\x0b\x32\x30.mathworks.scenario.simulation.SystemActionPhaseH\x00\x42\x06\n\x04type\"m\n\x10\x41\x63torActionPhase\x12\x10\n\x08\x61\x63tor_id\x18\x01 \x01(\t\x12G\n\rcreation_mode\x18\x02 \x01(\x0e\x32\x30.mathworks.scenario.simulation.ActorCreationMode\"\x13\n\x11SystemActionPhase*\x9e\x01\n\x11\x41\x63torCreationMode\x12#\n\x1f\x41\x43TOR_CREATION_MODE_UNSPECIFIED\x10\x00\x12!\n\x1d\x41\x43TOR_CREATION_MODE_AUTOMATIC\x10\x01\x12\x1e\n\x1a\x41\x43TOR_CREATION_MODE_CREATE\x10\x02\x12!\n\x1d\x41\x43TOR_CREATION_MODE_NO_CREATE\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mathworks.scenario.simulation.scenario_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ACTORCREATIONMODE']._serialized_start=1425
  _globals['_ACTORCREATIONMODE']._serialized_end=1583
  _globals['_SCENARIO']._serialized_start=223
  _globals['_SCENARIO']._serialized_end=430
  _globals['_PHASE']._serialized_start=433
  _globals['_PHASE']._serialized_end=810
  _globals['_COMPOSITEPHASE']._serialized_start=813
  _globals['_COMPOSITEPHASE']._serialized_end=1023
  _globals['_SERIALPHASE']._serialized_start=1025
  _globals['_SERIALPHASE']._serialized_end=1038
  _globals['_MIXPHASE']._serialized_start=1040
  _globals['_MIXPHASE']._serialized_end=1050
  _globals['_ACTIONPHASE']._serialized_start=1053
  _globals['_ACTIONPHASE']._serialized_end=1290
  _globals['_ACTORACTIONPHASE']._serialized_start=1292
  _globals['_ACTORACTIONPHASE']._serialized_end=1401
  _globals['_SYSTEMACTIONPHASE']._serialized_start=1403
  _globals['_SYSTEMACTIONPHASE']._serialized_end=1422
# @@protoc_insertion_point(module_scope)
