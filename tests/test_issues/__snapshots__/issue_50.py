# Auto generated from issue_50.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: example.com
#
# id: http://example.com
# description:
# license:

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



metamodel_version = "1.7.0"
version = None

# Namespaces
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.com/')


# Types
class String(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = URIRef("http://example.com/String")


# Class references
class TestClass1Id(extended_str):
    pass


class TestClass2Id(extended_str):
    pass


class TestClass3Id(extended_str):
    pass


@dataclass(repr=False)
class TestClass1(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 1"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass1")

    id: Union[str, TestClass1Id] = None
    required_mixin_slot: str = None
    optional_mixin_slot: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestClass1Id):
            self.id = TestClass1Id(self.id)

        if self._is_empty(self.required_mixin_slot):
            self.MissingRequiredField("required_mixin_slot")
        if not isinstance(self.required_mixin_slot, str):
            self.required_mixin_slot = str(self.required_mixin_slot)

        if self.optional_mixin_slot is not None and not isinstance(self.optional_mixin_slot, str):
            self.optional_mixin_slot = str(self.optional_mixin_slot)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TestClass2(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass2")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 2"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass2")

    id: Union[str, TestClass2Id] = None
    required_mixin_slot: str = None
    optional_mixin_slot: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestClass2Id):
            self.id = TestClass2Id(self.id)

        if self._is_empty(self.required_mixin_slot):
            self.MissingRequiredField("required_mixin_slot")
        if not isinstance(self.required_mixin_slot, str):
            self.required_mixin_slot = str(self.required_mixin_slot)

        if self.optional_mixin_slot is not None and not isinstance(self.optional_mixin_slot, str):
            self.optional_mixin_slot = str(self.optional_mixin_slot)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TestClass3(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "test class 3"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.com/TestClass3")

    id: Union[str, TestClass3Id] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestClass3Id):
            self.id = TestClass3Id(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.optional_mixin_slot = Slot(uri=DEFAULT_.optional_mixin_slot, name="optional_mixin_slot", curie=DEFAULT_.curie('optional_mixin_slot'),
                   model_uri=DEFAULT_.optional_mixin_slot, domain=None, range=Optional[str])

slots.required_mixin_slot = Slot(uri=DEFAULT_.required_mixin_slot, name="required_mixin_slot", curie=DEFAULT_.curie('required_mixin_slot'),
                   model_uri=DEFAULT_.required_mixin_slot, domain=None, range=str)

slots.optional_domain_slot = Slot(uri=DEFAULT_.optional_domain_slot, name="optional_domain_slot", curie=DEFAULT_.curie('optional_domain_slot'),
                   model_uri=DEFAULT_.optional_domain_slot, domain=TestClass3, range=Optional[str])

slots.required_domain_slot = Slot(uri=DEFAULT_.required_domain_slot, name="required_domain_slot", curie=DEFAULT_.curie('required_domain_slot'),
                   model_uri=DEFAULT_.required_domain_slot, domain=TestClass3, range=str)
