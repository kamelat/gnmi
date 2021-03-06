# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/gnmi_ext/gnmi_ext.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/gnmi_ext/gnmi_ext.proto',
  package='gnmi_ext',
  syntax='proto3',
  serialized_pb=_b('\n\x1dproto/gnmi_ext/gnmi_ext.proto\x12\x08gnmi_ext\"K\n\tExtension\x12\x37\n\x0eregistered_ext\x18\x01 \x01(\x0b\x32\x1d.gnmi_ext.RegisteredExtensionH\x00\x42\x05\n\x03\x65xt\"E\n\x13RegisteredExtension\x12!\n\x02id\x18\x01 \x01(\x0e\x32\x15.gnmi_ext.ExtensionID\x12\x0b\n\x03msg\x18\x02 \x01(\x0c*3\n\x0b\x45xtensionID\x12\r\n\tEID_UNSET\x10\x00\x12\x15\n\x10\x45ID_EXPERIMENTAL\x10\xe7\x07\x62\x06proto3')
)

_EXTENSIONID = _descriptor.EnumDescriptor(
  name='ExtensionID',
  full_name='gnmi_ext.ExtensionID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EID_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EID_EXPERIMENTAL', index=1, number=999,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=191,
  serialized_end=242,
)
_sym_db.RegisterEnumDescriptor(_EXTENSIONID)

ExtensionID = enum_type_wrapper.EnumTypeWrapper(_EXTENSIONID)
EID_UNSET = 0
EID_EXPERIMENTAL = 999



_EXTENSION = _descriptor.Descriptor(
  name='Extension',
  full_name='gnmi_ext.Extension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registered_ext', full_name='gnmi_ext.Extension.registered_ext', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ext', full_name='gnmi_ext.Extension.ext',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=118,
)


_REGISTEREDEXTENSION = _descriptor.Descriptor(
  name='RegisteredExtension',
  full_name='gnmi_ext.RegisteredExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gnmi_ext.RegisteredExtension.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='gnmi_ext.RegisteredExtension.msg', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=189,
)

_EXTENSION.fields_by_name['registered_ext'].message_type = _REGISTEREDEXTENSION
_EXTENSION.oneofs_by_name['ext'].fields.append(
  _EXTENSION.fields_by_name['registered_ext'])
_EXTENSION.fields_by_name['registered_ext'].containing_oneof = _EXTENSION.oneofs_by_name['ext']
_REGISTEREDEXTENSION.fields_by_name['id'].enum_type = _EXTENSIONID
DESCRIPTOR.message_types_by_name['Extension'] = _EXTENSION
DESCRIPTOR.message_types_by_name['RegisteredExtension'] = _REGISTEREDEXTENSION
DESCRIPTOR.enum_types_by_name['ExtensionID'] = _EXTENSIONID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Extension = _reflection.GeneratedProtocolMessageType('Extension', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSION,
  __module__ = 'proto.gnmi_ext.gnmi_ext_pb2'
  # @@protoc_insertion_point(class_scope:gnmi_ext.Extension)
  ))
_sym_db.RegisterMessage(Extension)

RegisteredExtension = _reflection.GeneratedProtocolMessageType('RegisteredExtension', (_message.Message,), dict(
  DESCRIPTOR = _REGISTEREDEXTENSION,
  __module__ = 'proto.gnmi_ext.gnmi_ext_pb2'
  # @@protoc_insertion_point(class_scope:gnmi_ext.RegisteredExtension)
  ))
_sym_db.RegisterMessage(RegisteredExtension)


# @@protoc_insertion_point(module_scope)
