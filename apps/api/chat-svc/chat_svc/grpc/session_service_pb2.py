# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15session_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x01\n\x16GetChatSessionsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\x04take\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04skip\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08order_by\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05order\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_takeB\x07\n\x05_skipB\x0b\n\t_order_byB\x08\n\x06_order\"<\n\x16GetChatSessionResponse\x12\"\n\x0c\x63hat_session\x18\x01 \x01(\x0b\x32\x0c.ChatSession\"9\n\x18\x43reateChatSessionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"L\n\x17GetChatSessionsResponse\x12\"\n\x0c\x63hat_session\x18\x01 \x03(\x0b\x32\x0c.ChatSession\x12\r\n\x05total\x18\x02 \x01(\x05\"4\n\x18UpdateChatSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"?\n\x19UpdateChatSessionResponse\x12\"\n\x0c\x63hat_session\x18\x01 \x01(\x0b\x32\x0c.ChatSession\"&\n\x18\x44\x65leteChatSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t\",\n\x19\x44\x65leteChatSessionResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"h\n\x0b\x43hatSession\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"#\n\x15GetChatSessionRequest\x12\n\n\x02id\x18\x01 \x01(\t2\x87\x03\n\x12\x43hatSessionService\x12\x43\n\x0eGetChatSession\x12\x16.GetChatSessionRequest\x1a\x17.GetChatSessionResponse\"\x00\x12\x45\n\x0fGetChatSessions\x12\x17.GetChatSessionsRequest\x1a\x17.GetChatSessionResponse\"\x00\x12I\n\x11\x43reateChatSession\x12\x19.CreateChatSessionRequest\x1a\x17.GetChatSessionResponse\"\x00\x12L\n\x11UpdateChatSession\x12\x19.UpdateChatSessionRequest\x1a\x1a.UpdateChatSessionResponse\"\x00\x12L\n\x11\x44\x65leteChatSession\x12\x19.DeleteChatSessionRequest\x1a\x1a.DeleteChatSessionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'session_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETCHATSESSIONSREQUEST']._serialized_start=59
  _globals['_GETCHATSESSIONSREQUEST']._serialized_end=222
  _globals['_GETCHATSESSIONRESPONSE']._serialized_start=224
  _globals['_GETCHATSESSIONRESPONSE']._serialized_end=284
  _globals['_CREATECHATSESSIONREQUEST']._serialized_start=286
  _globals['_CREATECHATSESSIONREQUEST']._serialized_end=343
  _globals['_GETCHATSESSIONSRESPONSE']._serialized_start=345
  _globals['_GETCHATSESSIONSRESPONSE']._serialized_end=421
  _globals['_UPDATECHATSESSIONREQUEST']._serialized_start=423
  _globals['_UPDATECHATSESSIONREQUEST']._serialized_end=475
  _globals['_UPDATECHATSESSIONRESPONSE']._serialized_start=477
  _globals['_UPDATECHATSESSIONRESPONSE']._serialized_end=540
  _globals['_DELETECHATSESSIONREQUEST']._serialized_start=542
  _globals['_DELETECHATSESSIONREQUEST']._serialized_end=580
  _globals['_DELETECHATSESSIONRESPONSE']._serialized_start=582
  _globals['_DELETECHATSESSIONRESPONSE']._serialized_end=626
  _globals['_CHATSESSION']._serialized_start=628
  _globals['_CHATSESSION']._serialized_end=732
  _globals['_GETCHATSESSIONREQUEST']._serialized_start=734
  _globals['_GETCHATSESSIONREQUEST']._serialized_end=769
  _globals['_CHATSESSIONSERVICE']._serialized_start=772
  _globals['_CHATSESSIONSERVICE']._serialized_end=1163
# @@protoc_insertion_point(module_scope)
