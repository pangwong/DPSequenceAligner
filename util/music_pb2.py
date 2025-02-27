import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='music.proto',
  package='tensorflow.magenta',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bmusic.proto\x12\x12tensorflow.magenta\"\xdc\x1f\n\x0cNoteSequence\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x18\n\x10reference_number\x18\x12 \x01(\x03\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x19\n\x11ticks_per_quarter\x18\x04 \x01(\x05\x12G\n\x0ftime_signatures\x18\x05 \x03(\x0b\x32..tensorflow.magenta.NoteSequence.TimeSignature\x12\x45\n\x0ekey_signatures\x18\x06 \x03(\x0b\x32-.tensorflow.magenta.NoteSequence.KeySignature\x12\x36\n\x06tempos\x18\x07 \x03(\x0b\x32&.tensorflow.magenta.NoteSequence.Tempo\x12\x34\n\x05notes\x18\x08 \x03(\x0b\x32%.tensorflow.magenta.NoteSequence.Note\x12\x12\n\ntotal_time\x18\t \x01(\x01\x12\x1d\n\x15total_quantized_steps\x18\x10 \x01(\x03\x12?\n\x0bpitch_bends\x18\n \x03(\x0b\x32*.tensorflow.magenta.NoteSequence.PitchBend\x12G\n\x0f\x63ontrol_changes\x18\x0b \x03(\x0b\x32..tensorflow.magenta.NoteSequence.ControlChange\x12=\n\npart_infos\x18\x0c \x03(\x0b\x32).tensorflow.magenta.NoteSequence.PartInfo\x12@\n\x0bsource_info\x18\r \x01(\x0b\x32+.tensorflow.magenta.NoteSequence.SourceInfo\x12I\n\x10text_annotations\x18\x0e \x03(\x0b\x32/.tensorflow.magenta.NoteSequence.TextAnnotation\x12O\n\x13section_annotations\x18\x14 \x03(\x0b\x32\x32.tensorflow.magenta.NoteSequence.SectionAnnotation\x12\x45\n\x0esection_groups\x18\x15 \x03(\x0b\x32-.tensorflow.magenta.NoteSequence.SectionGroup\x12L\n\x11quantization_info\x18\x0f \x01(\x0b\x32\x31.tensorflow.magenta.NoteSequence.QuantizationInfo\x12J\n\x10subsequence_info\x18\x11 \x01(\x0b\x32\x30.tensorflow.magenta.NoteSequence.SubsequenceInfo\x12?\n\x11sequence_metadata\x18\x13 \x01(\x0b\x32$.tensorflow.magenta.SequenceMetadata\x1a\xc2\x02\n\x04Note\x12\r\n\x05pitch\x18\x01 \x01(\x05\x12>\n\npitch_name\x18\x0b \x01(\x0e\x32*.tensorflow.magenta.NoteSequence.PitchName\x12\x10\n\x08velocity\x18\x02 \x01(\x05\x12\x12\n\nstart_time\x18\x03 \x01(\x01\x12\x1c\n\x14quantized_start_step\x18\r \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x01\x12\x1a\n\x12quantized_end_step\x18\x0e \x01(\x03\x12\x11\n\tnumerator\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x06 \x01(\x05\x12\x12\n\ninstrument\x18\x07 \x01(\x05\x12\x0f\n\x07program\x18\x08 \x01(\x05\x12\x0f\n\x07is_drum\x18\t \x01(\x08\x12\x0c\n\x04part\x18\n \x01(\x05\x12\r\n\x05voice\x18\x0c \x01(\x05\x1a\x45\n\rTimeSignature\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x11\n\tnumerator\x18\x02 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x03 \x01(\x05\x1a\xcc\x03\n\x0cKeySignature\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12>\n\x03key\x18\x02 \x01(\x0e\x32\x31.tensorflow.magenta.NoteSequence.KeySignature.Key\x12@\n\x04mode\x18\x03 \x01(\x0e\x32\x32.tensorflow.magenta.NoteSequence.KeySignature.Mode\"\xb7\x01\n\x03Key\x12\x05\n\x01\x43\x10\x00\x12\x0b\n\x07\x43_SHARP\x10\x01\x12\n\n\x06\x44_FLAT\x10\x01\x12\x05\n\x01\x44\x10\x02\x12\x0b\n\x07\x44_SHARP\x10\x03\x12\n\n\x06\x45_FLAT\x10\x03\x12\x05\n\x01\x45\x10\x04\x12\x05\n\x01\x46\x10\x05\x12\x0b\n\x07\x46_SHARP\x10\x06\x12\n\n\x06G_FLAT\x10\x06\x12\x05\n\x01G\x10\x07\x12\x0b\n\x07G_SHARP\x10\x08\x12\n\n\x06\x41_FLAT\x10\x08\x12\x05\n\x01\x41\x10\t\x12\x0b\n\x07\x41_SHARP\x10\n\x12\n\n\x06\x42_FLAT\x10\n\x12\x05\n\x01\x42\x10\x0b\x1a\x02\x10\x01\"r\n\x04Mode\x12\t\n\x05MAJOR\x10\x00\x12\t\n\x05MINOR\x10\x01\x12\x11\n\rNOT_SPECIFIED\x10\x02\x12\x0e\n\nMIXOLYDIAN\x10\x03\x12\n\n\x06\x44ORIAN\x10\x04\x12\x0c\n\x08PHRYGIAN\x10\x05\x12\n\n\x06LYDIAN\x10\x06\x12\x0b\n\x07LOCRIAN\x10\x07\x1a\"\n\x05Tempo\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0b\n\x03qpm\x18\x02 \x01(\x01\x1a]\n\tPitchBend\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x0c\n\x04\x62\x65nd\x18\x02 \x01(\x05\x12\x12\n\ninstrument\x18\x03 \x01(\x05\x12\x0f\n\x07program\x18\x04 \x01(\x05\x12\x0f\n\x07is_drum\x18\x05 \x01(\x08\x1a\x9a\x01\n\rControlChange\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x16\n\x0equantized_step\x18\x07 \x01(\x03\x12\x16\n\x0e\x63ontrol_number\x18\x02 \x01(\x05\x12\x15\n\rcontrol_value\x18\x03 \x01(\x05\x12\x12\n\ninstrument\x18\x04 \x01(\x05\x12\x0f\n\x07program\x18\x05 \x01(\x05\x12\x0f\n\x07is_drum\x18\x06 \x01(\x08\x1a&\n\x08PartInfo\x12\x0c\n\x04part\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xac\x04\n\nSourceInfo\x12K\n\x0bsource_type\x18\x01 \x01(\x0e\x32\x36.tensorflow.magenta.NoteSequence.SourceInfo.SourceType\x12O\n\rencoding_type\x18\x02 \x01(\x0e\x32\x38.tensorflow.magenta.NoteSequence.SourceInfo.EncodingType\x12\x42\n\x06parser\x18\x03 \x01(\x0e\x32\x32.tensorflow.magenta.NoteSequence.SourceInfo.Parser\"M\n\nSourceType\x12\x17\n\x13UNKNOWN_SOURCE_TYPE\x10\x00\x12\x0f\n\x0bSCORE_BASED\x10\x01\x12\x15\n\x11PERFORMANCE_BASED\x10\x02\"Y\n\x0c\x45ncodingType\x12\x19\n\x15UNKNOWN_ENCODING_TYPE\x10\x00\x12\r\n\tMUSIC_XML\x10\x01\x12\x07\n\x03\x41\x42\x43\x10\x02\x12\x08\n\x04MIDI\x10\x03\x12\x0c\n\x08MUSICNET\x10\x04\"\x91\x01\n\x06Parser\x12\x12\n\x0eUNKNOWN_PARSER\x10\x00\x12\x0b\n\x07MUSIC21\x10\x01\x12\x0f\n\x0bPRETTY_MIDI\x10\x02\x12\x15\n\x11MAGENTA_MUSIC_XML\x10\x03\x12\x14\n\x10MAGENTA_MUSICNET\x10\x04\x12\x0f\n\x0bMAGENTA_ABC\x10\x05\x12\x17\n\x13TONEJS_MIDI_CONVERT\x10\x06\x1a\xe0\x01\n\x0eTextAnnotation\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x16\n\x0equantized_step\x18\x04 \x01(\x03\x12\x0c\n\x04text\x18\x02 \x01(\t\x12[\n\x0f\x61nnotation_type\x18\x03 \x01(\x0e\x32\x42.tensorflow.magenta.NoteSequence.TextAnnotation.TextAnnotationType\"=\n\x12TextAnnotationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x43HORD_SYMBOL\x10\x01\x12\x08\n\x04\x42\x45\x41T\x10\x02\x1aY\n\x10QuantizationInfo\x12\x1b\n\x11steps_per_quarter\x18\x01 \x01(\x05H\x00\x12\x1a\n\x10steps_per_second\x18\x02 \x01(\x05H\x00\x42\x0c\n\nresolution\x1a\x45\n\x0fSubsequenceInfo\x12\x19\n\x11start_time_offset\x18\x01 \x01(\x01\x12\x17\n\x0f\x65nd_time_offset\x18\x02 \x01(\x01\x1a\x35\n\x11SectionAnnotation\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\x12\n\nsection_id\x18\x04 \x01(\x03\x1aw\n\x07Section\x12\x14\n\nsection_id\x18\x01 \x01(\x03H\x00\x12\x46\n\rsection_group\x18\x02 \x01(\x0b\x32-.tensorflow.magenta.NoteSequence.SectionGroupH\x00\x42\x0e\n\x0csection_type\x1a]\n\x0cSectionGroup\x12:\n\x08sections\x18\x01 \x03(\x0b\x32(.tensorflow.magenta.NoteSequence.Section\x12\x11\n\tnum_times\x18\x02 \x01(\x05\"\xff\x03\n\tPitchName\x12\x16\n\x12UNKNOWN_PITCH_NAME\x10\x00\x12\x0f\n\x0b\x46_FLAT_FLAT\x10\x01\x12\x0f\n\x0b\x43_FLAT_FLAT\x10\x02\x12\x0f\n\x0bG_FLAT_FLAT\x10\x03\x12\x0f\n\x0b\x44_FLAT_FLAT\x10\x04\x12\x0f\n\x0b\x41_FLAT_FLAT\x10\x05\x12\x0f\n\x0b\x45_FLAT_FLAT\x10\x06\x12\x0f\n\x0b\x42_FLAT_FLAT\x10\x07\x12\n\n\x06\x46_FLAT\x10\x08\x12\n\n\x06\x43_FLAT\x10\t\x12\n\n\x06G_FLAT\x10\n\x12\n\n\x06\x44_FLAT\x10\x0b\x12\n\n\x06\x41_FLAT\x10\x0c\x12\n\n\x06\x45_FLAT\x10\r\x12\n\n\x06\x42_FLAT\x10\x0e\x12\x05\n\x01\x46\x10\x0f\x12\x05\n\x01\x43\x10\x10\x12\x05\n\x01G\x10\x11\x12\x05\n\x01\x44\x10\x12\x12\x05\n\x01\x41\x10\x13\x12\x05\n\x01\x45\x10\x14\x12\x05\n\x01\x42\x10\x15\x12\x0b\n\x07\x46_SHARP\x10\x16\x12\x0b\n\x07\x43_SHARP\x10\x17\x12\x0b\n\x07G_SHARP\x10\x18\x12\x0b\n\x07\x44_SHARP\x10\x19\x12\x0b\n\x07\x41_SHARP\x10\x1a\x12\x0b\n\x07\x45_SHARP\x10\x1b\x12\x0b\n\x07\x42_SHARP\x10\x1c\x12\x11\n\rF_SHARP_SHARP\x10\x1d\x12\x11\n\rC_SHARP_SHARP\x10\x1e\x12\x11\n\rG_SHARP_SHARP\x10\x1f\x12\x11\n\rD_SHARP_SHARP\x10 \x12\x11\n\rA_SHARP_SHARP\x10!\x12\x11\n\rE_SHARP_SHARP\x10\"\x12\x11\n\rB_SHARP_SHARP\x10#\"S\n\x10SequenceMetadata\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x03(\t\x12\x11\n\tcomposers\x18\x04 \x03(\t\")\n\rVelocityRange\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x62\x06proto3')
)



_NOTESEQUENCE_KEYSIGNATURE_KEY = _descriptor.EnumDescriptor(
  name='Key',
  full_name='tensorflow.magenta.NoteSequence.KeySignature.Key',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='C', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_SHARP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_FLAT', index=2, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D', index=3, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_SHARP', index=4, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_FLAT', index=5, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E', index=6, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F', index=7, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F_SHARP', index=8, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_FLAT', index=9, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G', index=10, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_SHARP', index=11, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_FLAT', index=12, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A', index=13, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_SHARP', index=14, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B_FLAT', index=15, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B', index=16, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=1736,
  serialized_end=1919,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_KEYSIGNATURE_KEY)

_NOTESEQUENCE_KEYSIGNATURE_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='tensorflow.magenta.NoteSequence.KeySignature.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAJOR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINOR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_SPECIFIED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIXOLYDIAN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DORIAN', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHRYGIAN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LYDIAN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCRIAN', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1921,
  serialized_end=2035,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_KEYSIGNATURE_MODE)

_NOTESEQUENCE_SOURCEINFO_SOURCETYPE = _descriptor.EnumDescriptor(
  name='SourceType',
  full_name='tensorflow.magenta.NoteSequence.SourceInfo.SourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SOURCE_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCORE_BASED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERFORMANCE_BASED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2606,
  serialized_end=2683,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_SOURCEINFO_SOURCETYPE)

_NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE = _descriptor.EnumDescriptor(
  name='EncodingType',
  full_name='tensorflow.magenta.NoteSequence.SourceInfo.EncodingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ENCODING_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUSIC_XML', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDI', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUSICNET', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2685,
  serialized_end=2774,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE)

_NOTESEQUENCE_SOURCEINFO_PARSER = _descriptor.EnumDescriptor(
  name='Parser',
  full_name='tensorflow.magenta.NoteSequence.SourceInfo.Parser',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PARSER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUSIC21', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRETTY_MIDI', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGENTA_MUSIC_XML', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGENTA_MUSICNET', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGENTA_ABC', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TONEJS_MIDI_CONVERT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2777,
  serialized_end=2922,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_SOURCEINFO_PARSER)

_NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE = _descriptor.EnumDescriptor(
  name='TextAnnotationType',
  full_name='tensorflow.magenta.NoteSequence.TextAnnotation.TextAnnotationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHORD_SYMBOL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEAT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3088,
  serialized_end=3149,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE)

_NOTESEQUENCE_PITCHNAME = _descriptor.EnumDescriptor(
  name='PitchName',
  full_name='tensorflow.magenta.NoteSequence.PitchName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PITCH_NAME', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F_FLAT_FLAT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_FLAT_FLAT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_FLAT_FLAT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_FLAT_FLAT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_FLAT_FLAT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_FLAT_FLAT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B_FLAT_FLAT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F_FLAT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_FLAT', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_FLAT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_FLAT', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_FLAT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_FLAT', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B_FLAT', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F_SHARP', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_SHARP', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_SHARP', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_SHARP', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_SHARP', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_SHARP', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B_SHARP', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F_SHARP_SHARP', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_SHARP_SHARP', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='G_SHARP_SHARP', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D_SHARP_SHARP', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='A_SHARP_SHARP', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_SHARP_SHARP', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B_SHARP_SHARP', index=35, number=35,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3585,
  serialized_end=4096,
)
_sym_db.RegisterEnumDescriptor(_NOTESEQUENCE_PITCHNAME)


_NOTESEQUENCE_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='tensorflow.magenta.NoteSequence.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch', full_name='tensorflow.magenta.NoteSequence.Note.pitch', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch_name', full_name='tensorflow.magenta.NoteSequence.Note.pitch_name', index=1,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='tensorflow.magenta.NoteSequence.Note.velocity', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tensorflow.magenta.NoteSequence.Note.start_time', index=3,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantized_start_step', full_name='tensorflow.magenta.NoteSequence.Note.quantized_start_step', index=4,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tensorflow.magenta.NoteSequence.Note.end_time', index=5,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantized_end_step', full_name='tensorflow.magenta.NoteSequence.Note.quantized_end_step', index=6,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numerator', full_name='tensorflow.magenta.NoteSequence.Note.numerator', index=7,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denominator', full_name='tensorflow.magenta.NoteSequence.Note.denominator', index=8,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='tensorflow.magenta.NoteSequence.Note.instrument', index=9,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program', full_name='tensorflow.magenta.NoteSequence.Note.program', index=10,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_drum', full_name='tensorflow.magenta.NoteSequence.Note.is_drum', index=11,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part', full_name='tensorflow.magenta.NoteSequence.Note.part', index=12,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice', full_name='tensorflow.magenta.NoteSequence.Note.voice', index=13,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1501,
)

_NOTESEQUENCE_TIMESIGNATURE = _descriptor.Descriptor(
  name='TimeSignature',
  full_name='tensorflow.magenta.NoteSequence.TimeSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.TimeSignature.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numerator', full_name='tensorflow.magenta.NoteSequence.TimeSignature.numerator', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denominator', full_name='tensorflow.magenta.NoteSequence.TimeSignature.denominator', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1503,
  serialized_end=1572,
)

_NOTESEQUENCE_KEYSIGNATURE = _descriptor.Descriptor(
  name='KeySignature',
  full_name='tensorflow.magenta.NoteSequence.KeySignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.KeySignature.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.magenta.NoteSequence.KeySignature.key', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='tensorflow.magenta.NoteSequence.KeySignature.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTESEQUENCE_KEYSIGNATURE_KEY,
    _NOTESEQUENCE_KEYSIGNATURE_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1575,
  serialized_end=2035,
)

_NOTESEQUENCE_TEMPO = _descriptor.Descriptor(
  name='Tempo',
  full_name='tensorflow.magenta.NoteSequence.Tempo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.Tempo.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qpm', full_name='tensorflow.magenta.NoteSequence.Tempo.qpm', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2037,
  serialized_end=2071,
)

_NOTESEQUENCE_PITCHBEND = _descriptor.Descriptor(
  name='PitchBend',
  full_name='tensorflow.magenta.NoteSequence.PitchBend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.PitchBend.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bend', full_name='tensorflow.magenta.NoteSequence.PitchBend.bend', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='tensorflow.magenta.NoteSequence.PitchBend.instrument', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program', full_name='tensorflow.magenta.NoteSequence.PitchBend.program', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_drum', full_name='tensorflow.magenta.NoteSequence.PitchBend.is_drum', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2073,
  serialized_end=2166,
)

_NOTESEQUENCE_CONTROLCHANGE = _descriptor.Descriptor(
  name='ControlChange',
  full_name='tensorflow.magenta.NoteSequence.ControlChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.ControlChange.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantized_step', full_name='tensorflow.magenta.NoteSequence.ControlChange.quantized_step', index=1,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_number', full_name='tensorflow.magenta.NoteSequence.ControlChange.control_number', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_value', full_name='tensorflow.magenta.NoteSequence.ControlChange.control_value', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='tensorflow.magenta.NoteSequence.ControlChange.instrument', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program', full_name='tensorflow.magenta.NoteSequence.ControlChange.program', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_drum', full_name='tensorflow.magenta.NoteSequence.ControlChange.is_drum', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2169,
  serialized_end=2323,
)

_NOTESEQUENCE_PARTINFO = _descriptor.Descriptor(
  name='PartInfo',
  full_name='tensorflow.magenta.NoteSequence.PartInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='part', full_name='tensorflow.magenta.NoteSequence.PartInfo.part', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.magenta.NoteSequence.PartInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2325,
  serialized_end=2363,
)

_NOTESEQUENCE_SOURCEINFO = _descriptor.Descriptor(
  name='SourceInfo',
  full_name='tensorflow.magenta.NoteSequence.SourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_type', full_name='tensorflow.magenta.NoteSequence.SourceInfo.source_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding_type', full_name='tensorflow.magenta.NoteSequence.SourceInfo.encoding_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parser', full_name='tensorflow.magenta.NoteSequence.SourceInfo.parser', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTESEQUENCE_SOURCEINFO_SOURCETYPE,
    _NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE,
    _NOTESEQUENCE_SOURCEINFO_PARSER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2366,
  serialized_end=2922,
)

_NOTESEQUENCE_TEXTANNOTATION = _descriptor.Descriptor(
  name='TextAnnotation',
  full_name='tensorflow.magenta.NoteSequence.TextAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.TextAnnotation.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantized_step', full_name='tensorflow.magenta.NoteSequence.TextAnnotation.quantized_step', index=1,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='tensorflow.magenta.NoteSequence.TextAnnotation.text', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation_type', full_name='tensorflow.magenta.NoteSequence.TextAnnotation.annotation_type', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2925,
  serialized_end=3149,
)

_NOTESEQUENCE_QUANTIZATIONINFO = _descriptor.Descriptor(
  name='QuantizationInfo',
  full_name='tensorflow.magenta.NoteSequence.QuantizationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steps_per_quarter', full_name='tensorflow.magenta.NoteSequence.QuantizationInfo.steps_per_quarter', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps_per_second', full_name='tensorflow.magenta.NoteSequence.QuantizationInfo.steps_per_second', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='resolution', full_name='tensorflow.magenta.NoteSequence.QuantizationInfo.resolution',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=3151,
  serialized_end=3240,
)

_NOTESEQUENCE_SUBSEQUENCEINFO = _descriptor.Descriptor(
  name='SubsequenceInfo',
  full_name='tensorflow.magenta.NoteSequence.SubsequenceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time_offset', full_name='tensorflow.magenta.NoteSequence.SubsequenceInfo.start_time_offset', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time_offset', full_name='tensorflow.magenta.NoteSequence.SubsequenceInfo.end_time_offset', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3242,
  serialized_end=3311,
)

_NOTESEQUENCE_SECTIONANNOTATION = _descriptor.Descriptor(
  name='SectionAnnotation',
  full_name='tensorflow.magenta.NoteSequence.SectionAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.magenta.NoteSequence.SectionAnnotation.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section_id', full_name='tensorflow.magenta.NoteSequence.SectionAnnotation.section_id', index=1,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3313,
  serialized_end=3366,
)

_NOTESEQUENCE_SECTION = _descriptor.Descriptor(
  name='Section',
  full_name='tensorflow.magenta.NoteSequence.Section',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section_id', full_name='tensorflow.magenta.NoteSequence.Section.section_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section_group', full_name='tensorflow.magenta.NoteSequence.Section.section_group', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='section_type', full_name='tensorflow.magenta.NoteSequence.Section.section_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=3368,
  serialized_end=3487,
)

_NOTESEQUENCE_SECTIONGROUP = _descriptor.Descriptor(
  name='SectionGroup',
  full_name='tensorflow.magenta.NoteSequence.SectionGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sections', full_name='tensorflow.magenta.NoteSequence.SectionGroup.sections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_times', full_name='tensorflow.magenta.NoteSequence.SectionGroup.num_times', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3489,
  serialized_end=3582,
)

_NOTESEQUENCE = _descriptor.Descriptor(
  name='NoteSequence',
  full_name='tensorflow.magenta.NoteSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.magenta.NoteSequence.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorflow.magenta.NoteSequence.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_number', full_name='tensorflow.magenta.NoteSequence.reference_number', index=2,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='tensorflow.magenta.NoteSequence.collection_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticks_per_quarter', full_name='tensorflow.magenta.NoteSequence.ticks_per_quarter', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_signatures', full_name='tensorflow.magenta.NoteSequence.time_signatures', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_signatures', full_name='tensorflow.magenta.NoteSequence.key_signatures', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tempos', full_name='tensorflow.magenta.NoteSequence.tempos', index=7,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='tensorflow.magenta.NoteSequence.notes', index=8,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='tensorflow.magenta.NoteSequence.total_time', index=9,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_quantized_steps', full_name='tensorflow.magenta.NoteSequence.total_quantized_steps', index=10,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch_bends', full_name='tensorflow.magenta.NoteSequence.pitch_bends', index=11,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='control_changes', full_name='tensorflow.magenta.NoteSequence.control_changes', index=12,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part_infos', full_name='tensorflow.magenta.NoteSequence.part_infos', index=13,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_info', full_name='tensorflow.magenta.NoteSequence.source_info', index=14,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_annotations', full_name='tensorflow.magenta.NoteSequence.text_annotations', index=15,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section_annotations', full_name='tensorflow.magenta.NoteSequence.section_annotations', index=16,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='section_groups', full_name='tensorflow.magenta.NoteSequence.section_groups', index=17,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantization_info', full_name='tensorflow.magenta.NoteSequence.quantization_info', index=18,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subsequence_info', full_name='tensorflow.magenta.NoteSequence.subsequence_info', index=19,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_metadata', full_name='tensorflow.magenta.NoteSequence.sequence_metadata', index=20,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NOTESEQUENCE_NOTE, _NOTESEQUENCE_TIMESIGNATURE, _NOTESEQUENCE_KEYSIGNATURE, _NOTESEQUENCE_TEMPO, _NOTESEQUENCE_PITCHBEND, _NOTESEQUENCE_CONTROLCHANGE, _NOTESEQUENCE_PARTINFO, _NOTESEQUENCE_SOURCEINFO, _NOTESEQUENCE_TEXTANNOTATION, _NOTESEQUENCE_QUANTIZATIONINFO, _NOTESEQUENCE_SUBSEQUENCEINFO, _NOTESEQUENCE_SECTIONANNOTATION, _NOTESEQUENCE_SECTION, _NOTESEQUENCE_SECTIONGROUP, ],
  enum_types=[
    _NOTESEQUENCE_PITCHNAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=4096,
)


_SEQUENCEMETADATA = _descriptor.Descriptor(
  name='SequenceMetadata',
  full_name='tensorflow.magenta.SequenceMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='tensorflow.magenta.SequenceMetadata.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artist', full_name='tensorflow.magenta.SequenceMetadata.artist', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genre', full_name='tensorflow.magenta.SequenceMetadata.genre', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='composers', full_name='tensorflow.magenta.SequenceMetadata.composers', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4098,
  serialized_end=4181,
)


_VELOCITYRANGE = _descriptor.Descriptor(
  name='VelocityRange',
  full_name='tensorflow.magenta.VelocityRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='tensorflow.magenta.VelocityRange.min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='tensorflow.magenta.VelocityRange.max', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4183,
  serialized_end=4224,
)

_NOTESEQUENCE_NOTE.fields_by_name['pitch_name'].enum_type = _NOTESEQUENCE_PITCHNAME
_NOTESEQUENCE_NOTE.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_TIMESIGNATURE.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_KEYSIGNATURE.fields_by_name['key'].enum_type = _NOTESEQUENCE_KEYSIGNATURE_KEY
_NOTESEQUENCE_KEYSIGNATURE.fields_by_name['mode'].enum_type = _NOTESEQUENCE_KEYSIGNATURE_MODE
_NOTESEQUENCE_KEYSIGNATURE.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_KEYSIGNATURE_KEY.containing_type = _NOTESEQUENCE_KEYSIGNATURE
_NOTESEQUENCE_KEYSIGNATURE_MODE.containing_type = _NOTESEQUENCE_KEYSIGNATURE
_NOTESEQUENCE_TEMPO.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_PITCHBEND.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_CONTROLCHANGE.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_PARTINFO.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_SOURCEINFO.fields_by_name['source_type'].enum_type = _NOTESEQUENCE_SOURCEINFO_SOURCETYPE
_NOTESEQUENCE_SOURCEINFO.fields_by_name['encoding_type'].enum_type = _NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE
_NOTESEQUENCE_SOURCEINFO.fields_by_name['parser'].enum_type = _NOTESEQUENCE_SOURCEINFO_PARSER
_NOTESEQUENCE_SOURCEINFO.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_SOURCEINFO_SOURCETYPE.containing_type = _NOTESEQUENCE_SOURCEINFO
_NOTESEQUENCE_SOURCEINFO_ENCODINGTYPE.containing_type = _NOTESEQUENCE_SOURCEINFO
_NOTESEQUENCE_SOURCEINFO_PARSER.containing_type = _NOTESEQUENCE_SOURCEINFO
_NOTESEQUENCE_TEXTANNOTATION.fields_by_name['annotation_type'].enum_type = _NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE
_NOTESEQUENCE_TEXTANNOTATION.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_TEXTANNOTATION_TEXTANNOTATIONTYPE.containing_type = _NOTESEQUENCE_TEXTANNOTATION
_NOTESEQUENCE_QUANTIZATIONINFO.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_QUANTIZATIONINFO.oneofs_by_name['resolution'].fields.append(
  _NOTESEQUENCE_QUANTIZATIONINFO.fields_by_name['steps_per_quarter'])
_NOTESEQUENCE_QUANTIZATIONINFO.fields_by_name['steps_per_quarter'].containing_oneof = _NOTESEQUENCE_QUANTIZATIONINFO.oneofs_by_name['resolution']
_NOTESEQUENCE_QUANTIZATIONINFO.oneofs_by_name['resolution'].fields.append(
  _NOTESEQUENCE_QUANTIZATIONINFO.fields_by_name['steps_per_second'])
_NOTESEQUENCE_QUANTIZATIONINFO.fields_by_name['steps_per_second'].containing_oneof = _NOTESEQUENCE_QUANTIZATIONINFO.oneofs_by_name['resolution']
_NOTESEQUENCE_SUBSEQUENCEINFO.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_SECTIONANNOTATION.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_SECTION.fields_by_name['section_group'].message_type = _NOTESEQUENCE_SECTIONGROUP
_NOTESEQUENCE_SECTION.containing_type = _NOTESEQUENCE
_NOTESEQUENCE_SECTION.oneofs_by_name['section_type'].fields.append(
  _NOTESEQUENCE_SECTION.fields_by_name['section_id'])
_NOTESEQUENCE_SECTION.fields_by_name['section_id'].containing_oneof = _NOTESEQUENCE_SECTION.oneofs_by_name['section_type']
_NOTESEQUENCE_SECTION.oneofs_by_name['section_type'].fields.append(
  _NOTESEQUENCE_SECTION.fields_by_name['section_group'])
_NOTESEQUENCE_SECTION.fields_by_name['section_group'].containing_oneof = _NOTESEQUENCE_SECTION.oneofs_by_name['section_type']
_NOTESEQUENCE_SECTIONGROUP.fields_by_name['sections'].message_type = _NOTESEQUENCE_SECTION
_NOTESEQUENCE_SECTIONGROUP.containing_type = _NOTESEQUENCE
_NOTESEQUENCE.fields_by_name['time_signatures'].message_type = _NOTESEQUENCE_TIMESIGNATURE
_NOTESEQUENCE.fields_by_name['key_signatures'].message_type = _NOTESEQUENCE_KEYSIGNATURE
_NOTESEQUENCE.fields_by_name['tempos'].message_type = _NOTESEQUENCE_TEMPO
_NOTESEQUENCE.fields_by_name['notes'].message_type = _NOTESEQUENCE_NOTE
_NOTESEQUENCE.fields_by_name['pitch_bends'].message_type = _NOTESEQUENCE_PITCHBEND
_NOTESEQUENCE.fields_by_name['control_changes'].message_type = _NOTESEQUENCE_CONTROLCHANGE
_NOTESEQUENCE.fields_by_name['part_infos'].message_type = _NOTESEQUENCE_PARTINFO
_NOTESEQUENCE.fields_by_name['source_info'].message_type = _NOTESEQUENCE_SOURCEINFO
_NOTESEQUENCE.fields_by_name['text_annotations'].message_type = _NOTESEQUENCE_TEXTANNOTATION
_NOTESEQUENCE.fields_by_name['section_annotations'].message_type = _NOTESEQUENCE_SECTIONANNOTATION
_NOTESEQUENCE.fields_by_name['section_groups'].message_type = _NOTESEQUENCE_SECTIONGROUP
_NOTESEQUENCE.fields_by_name['quantization_info'].message_type = _NOTESEQUENCE_QUANTIZATIONINFO
_NOTESEQUENCE.fields_by_name['subsequence_info'].message_type = _NOTESEQUENCE_SUBSEQUENCEINFO
_NOTESEQUENCE.fields_by_name['sequence_metadata'].message_type = _SEQUENCEMETADATA
_NOTESEQUENCE_PITCHNAME.containing_type = _NOTESEQUENCE
DESCRIPTOR.message_types_by_name['NoteSequence'] = _NOTESEQUENCE
DESCRIPTOR.message_types_by_name['SequenceMetadata'] = _SEQUENCEMETADATA
DESCRIPTOR.message_types_by_name['VelocityRange'] = _VELOCITYRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoteSequence = _reflection.GeneratedProtocolMessageType('NoteSequence', (_message.Message,), dict(

  Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_NOTE,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.Note)
    ))
  ,

  TimeSignature = _reflection.GeneratedProtocolMessageType('TimeSignature', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_TIMESIGNATURE,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.TimeSignature)
    ))
  ,

  KeySignature = _reflection.GeneratedProtocolMessageType('KeySignature', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_KEYSIGNATURE,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.KeySignature)
    ))
  ,

  Tempo = _reflection.GeneratedProtocolMessageType('Tempo', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_TEMPO,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.Tempo)
    ))
  ,

  PitchBend = _reflection.GeneratedProtocolMessageType('PitchBend', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_PITCHBEND,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.PitchBend)
    ))
  ,

  ControlChange = _reflection.GeneratedProtocolMessageType('ControlChange', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_CONTROLCHANGE,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.ControlChange)
    ))
  ,

  PartInfo = _reflection.GeneratedProtocolMessageType('PartInfo', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_PARTINFO,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.PartInfo)
    ))
  ,

  SourceInfo = _reflection.GeneratedProtocolMessageType('SourceInfo', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_SOURCEINFO,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.SourceInfo)
    ))
  ,

  TextAnnotation = _reflection.GeneratedProtocolMessageType('TextAnnotation', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_TEXTANNOTATION,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.TextAnnotation)
    ))
  ,

  QuantizationInfo = _reflection.GeneratedProtocolMessageType('QuantizationInfo', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_QUANTIZATIONINFO,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.QuantizationInfo)
    ))
  ,

  SubsequenceInfo = _reflection.GeneratedProtocolMessageType('SubsequenceInfo', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_SUBSEQUENCEINFO,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.SubsequenceInfo)
    ))
  ,

  SectionAnnotation = _reflection.GeneratedProtocolMessageType('SectionAnnotation', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_SECTIONANNOTATION,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.SectionAnnotation)
    ))
  ,

  Section = _reflection.GeneratedProtocolMessageType('Section', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_SECTION,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.Section)
    ))
  ,

  SectionGroup = _reflection.GeneratedProtocolMessageType('SectionGroup', (_message.Message,), dict(
    DESCRIPTOR = _NOTESEQUENCE_SECTIONGROUP,
    __module__ = 'music_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence.SectionGroup)
    ))
  ,
  DESCRIPTOR = _NOTESEQUENCE,
  __module__ = 'music_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.magenta.NoteSequence)
  ))
_sym_db.RegisterMessage(NoteSequence)
_sym_db.RegisterMessage(NoteSequence.Note)
_sym_db.RegisterMessage(NoteSequence.TimeSignature)
_sym_db.RegisterMessage(NoteSequence.KeySignature)
_sym_db.RegisterMessage(NoteSequence.Tempo)
_sym_db.RegisterMessage(NoteSequence.PitchBend)
_sym_db.RegisterMessage(NoteSequence.ControlChange)
_sym_db.RegisterMessage(NoteSequence.PartInfo)
_sym_db.RegisterMessage(NoteSequence.SourceInfo)
_sym_db.RegisterMessage(NoteSequence.TextAnnotation)
_sym_db.RegisterMessage(NoteSequence.QuantizationInfo)
_sym_db.RegisterMessage(NoteSequence.SubsequenceInfo)
_sym_db.RegisterMessage(NoteSequence.SectionAnnotation)
_sym_db.RegisterMessage(NoteSequence.Section)
_sym_db.RegisterMessage(NoteSequence.SectionGroup)

SequenceMetadata = _reflection.GeneratedProtocolMessageType('SequenceMetadata', (_message.Message,), dict(
  DESCRIPTOR = _SEQUENCEMETADATA,
  __module__ = 'music_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.magenta.SequenceMetadata)
  ))
_sym_db.RegisterMessage(SequenceMetadata)

VelocityRange = _reflection.GeneratedProtocolMessageType('VelocityRange', (_message.Message,), dict(
  DESCRIPTOR = _VELOCITYRANGE,
  __module__ = 'music_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.magenta.VelocityRange)
  ))
_sym_db.RegisterMessage(VelocityRange)


_NOTESEQUENCE_KEYSIGNATURE_KEY._options = None
# @@protoc_insertion_point(module_scope)
