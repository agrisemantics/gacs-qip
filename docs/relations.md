### Semantic relations among concepts

A GACS concept is formally defined by its "semantic neighborhood" of
associative and hierarchical relations with other concepts in GACS.  The
concept
[_alfalfa_](http://tester-os-kktest.lib.helsinki.fi/gacsdemo/gacs/en/page/C1235),
for example, is defined by the following relations:

* _alfalfa_ hasType _Product_
* _alfalfa_ BT _legumes_
* _alfalfa_ RT _fodder plants_ 
* _fodder plants_ RT _livestock feeding_
* _fodder plants_ RT _forage_
* _fodder plants_ RT _hay_

These relations are reflected in the GACS definition of _alfalfa_ as: "A
valuable _leguminous crop_ for _forage_ or _hay_ used in _livestock feeding_".
Adding definitions to the 80% of concepts in GACS that lack them would be
expensive, especially across translations in multiple languages.  Narrative
definitions are less useful than semantic relations for automated processing,
which would need to infer the relation of _alfalfa_ to other concepts on the
basis of label strings, grammatical parsing, and the co-occurrence of words.  

Narrative definitions are less useful
than semantic relations in checking the consistency of concept usage, and they
are more vulnerable to "semantic creep" when translated into multiple
languages.  Narrative definitions do not provide a basis for expanding queries
or for browsing broader, narrower, or related concepts.  In GACS, definitions
are considered "nice to have" but not essential.

#### Broader, narrower, and related

GACS concepts are linked among themselves with _related_, _broader_, and
_narrower_ relations as defined in SKOS, which are themselves based on standard
thesaurus relations (_RT_, _BT_, and _NT_).  _Broader_ and _narrower_ do not
formally distinguish between "is a" and "part of" relations. In practice,
_broader_ and _narrower_ are generally intended to imply "is a" relations,
though not in a formally strict ontological sense, and there are plenty of
exceptions (for example,
[Maryland](http://tester-os-kktest.lib.helsinki.fi/gacsdemo/gacs/en/page/C10429)
is "part of" the [North Eastern States
(USA)](http://tester-os-kktest.lib.helsinki.fi/gacsdemo/gacs/en/page/C20128)).

#### Top-level concepts

All concepts in GACS are grouped under 

[Top level concepts. Assumptions about their use - or non-use. How they
relate to semantic types.]

#### Custom relations

[About custom relations.  Rationale for limited use.]

#### Mapping relations

[Mapping relations to concepts outside of GACS.]

