# Auto generated from timepoint.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: timepoint
#
# id: http://example.org/tests/timepoint
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Time
from linkml_runtime.utils.metamodelcore import XSDTime

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.org/tests/timepoint/')


# Types
class TimeType(Time):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD["time"]
    type_class_curie = "xsd:time"
    type_name = "time type"
    type_model_uri = URIRef("http://example.org/tests/timepoint/TimeType")


# Class references
class GeographicLocationK(extended_str):
    pass


class GeographicLocationAtTimeK(GeographicLocationK):
    pass


@dataclass(repr=False)
class GeographicLocation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "geographic location"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocation")

    k: Union[str, GeographicLocationK] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.k):
            self.MissingRequiredField("k")
        if not isinstance(self.k, GeographicLocationK):
            self.k = GeographicLocationK(self.k)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeographicLocationAtTime(GeographicLocation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "geographic location at time"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/timepoint/GeographicLocationAtTime")

    k: Union[str, GeographicLocationAtTimeK] = None
    timepoint: Optional[Union[str, TimeType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.k):
            self.MissingRequiredField("k")
        if not isinstance(self.k, GeographicLocationAtTimeK):
            self.k = GeographicLocationAtTimeK(self.k)

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.k = Slot(uri=DEFAULT_.k, name="k", curie=DEFAULT_.curie('k'),
                   model_uri=DEFAULT_.k, domain=GeographicLocation, range=Union[str, GeographicLocationK])

slots.timepoint = Slot(uri=DEFAULT_.timepoint, name="timepoint", curie=DEFAULT_.curie('timepoint'),
                   model_uri=DEFAULT_.timepoint, domain=GeographicLocationAtTime, range=Optional[Union[str, TimeType]])

