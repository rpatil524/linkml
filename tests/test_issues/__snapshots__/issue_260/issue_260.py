# Auto generated from issue_260.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: issue_260
#
# id: http://example.org/tests/issue_260
# description: Test relative imports
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

from . issue_260a import C260a, String
from ..issue_260.issue_260b import C260b
from .issue_260c import C260c

metamodel_version = "1.7.0"
version = None

# Namespaces
DEFAULT_ = CurieNamespace('', 'http://example.org/tests/issue_260/')


# Types

# Class references



class C2601(C260a):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2601")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2601"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2601")


class C2602(C260b):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2602")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2602"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2602")


class C2603(C260c):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2603")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "c2603"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/tests/issue_260/C2603")


# Enumerations


# Slots
class slots:
    pass
