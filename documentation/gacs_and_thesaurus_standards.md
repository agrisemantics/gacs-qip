### GACS and thesaurus standards

The evolving editorial policies for GACS Core follow best practices of modern
thesaurus design as per ISO 25964, "Thesauri and interoperability with other
vocabularies": concepts, described with natural-language labels, clarified
with definitions and scope notes, mapped to other concepts with associative and
hierarchical relations, and organized into thematic groups.

AGROVOC (created in 1982), CAB Thesaurus (1983), and NAL Thesaurus (2002) were
designed in conformance with the thesaurus practice of their day as laid down
in the [ISO
2788](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=7776)
standard for monolingual thesauri (1974) and the [ISO
5964](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=12159)
standard for multilingual thesauri (1985).  In ISO 2788 and ISO 5964, the
primary entity of interest is the *term* -- a word or phrase with a specified
semantic relationship to other *terms*.  The inherent ambiguity between index
*terms* and the *concepts* underlying those *terms* was acknowledged in the
1986 revision of ISO 2788.  However, the notions of *broader term*, *narrower
term*, and *related term* were so deeply embedded in thesaurus practice (as the
tags *BT*, *NT*, and *RT*), and the use of words as index keys was so deeply
embedded in contemporary database design, that thesauri based on ISO 2788 and
ISO 5964 may be characterized as "term-based".

[ISO
25964](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=53657),
the successor standard to ISO 2788 and ISO 5964 published in 2011 (Part 1) and
2013 (Part 2), explicitly characterizes a thesaurus as a list of *concepts*,
each of which is labelled with a preferred term (in each language) and relevant
synonyms and equivalents.  Thesauri based on ISO 25964 may be characterized as
"concept-based".  [Simple Knowledge Organization
System](http://www.w3.org/TR/skos-reference/) (SKOS), published as a W3C
Recommendation in 2009, provides a vocabulary for expressing a concept-based
thesaurus for use in Semantic Web and Linked Data applications.

Inasmuch as the GACS Project is taking SKOS as its point of departure, it is
worth calling out the sources of potential confusion between the terminology
used in term-based thesaurus practice and the terminology used in SKOS:

* *Term* refers to the word or phrase used to label a *concept* in a thesaurus.
  In an information-technology sense, a *term* is a literal, or string.  From a 
  SKOS perspective, a "term-based" thesaurus is an indexing
  language consisting of what SKOS calls *labels* -- words or phrases
  encoded as strings.  

* A *concept* is a unit of thought that has semantics, or meaning.  As Leonard
  Will puts it in his [glossary of terms related to
  thesauri](http://www.willpowerinfo.co.uk/glossary.htm): "Concepts exist in
  the mind as abstract entities which are independent of the terms used to
  label them".  In a concept-based thesaurus, *terms* (words and phrases)
  correspond to the *labels* of *SKOS concepts*.

* A *concept scheme* is a set of concepts, optionally specified with
  semantic relations between concepts.  AGROVOC, a *SKOS concept scheme*,
  is still referred to either as the AGROVOC Thesaurus or as the AGROVOC 
  Concept Scheme.  Technically, the category *concept scheme* is
  broader than the category *thesaurus* and includes subject heading lists,
  taxonomies, glossaries, classifications, and other types of controlled
  vocabulary.

An *ontology*, as defined by ISO 25964, is "a formal, explicit specification of
a shared conceptualization".  The notion of *ontology* appears only at the
margins of this report but will become more relevant as the GACS Project moves
towards implementation.  The word *ontology* has a wide range of meanings in
current usage.  For the purposes of this report an ontology is a set of
statements about things, groups of things, and relations between things in a
model of the world, expressed in a language that can be used to verify the
logical consistency of that knowledge or to make implicit knowledge explicit.
While there are gray areas between the two, an *ontology* is a construct
engineered to enable logical reasoning and inference, while a *concept scheme*
is a more flexible conceptualization optimized to support the sorts of indexing
and structured browsing for which the three thesauri considered here were
originally designed.

