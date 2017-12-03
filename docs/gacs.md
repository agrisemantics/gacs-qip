### [Placeholder text - to be completed]

[What GACS is.  GACS as a 'concept scheme'.  Origins in three thesauri. How
'concept scheme' differs (or not!) from 'thesaurus'.  Use of standards in its
construction, such as ISO 25964.  Use of SKOS in its expression.  Concepts
(identified with unique URIs) versus labels (terms).  Use of concept URIs in
Linked Data.  Use of preferred labels (unique terms) for indexing in retrieval
systems.  Multilinguality.]

GACS QIP

See [GACS browser](http://browser.agrisemantics.org/gacs/en/).

The Food and Agricultural Organization of the United Nations
(FAO), CAB International (CABI), and the National Agricultural Library of the
USA (NAL) [agreed in 2013](http://aims.fao.org/community/agrovoc/blogs/national-agricultural-library-usa-cabi-and-fao-agree-collaboration-developme)
to collaborate
in the development of their respective thesauri: the NAL Thesaurus, CAB
Thesaurus, and the AGROVOC Concept Scheme.  This collaboration led the development of 
a Global Agricultural Concept Scheme (GACS).

UAT-classified version of CAB Thesaurus

So we're not just minting yet another URI for Alberta, but also saying
that it exactly matches agrovoc:c_243, cabt:7687 and nalt:5999 (and
exact matches are transitive, so we can infer e.g. that cabt:7687
matches nalt:5999). These statements didn't exist before GACS came
along, and there was no natural place to state them, so GACS concepts
were defined. In the case of countries, territories etc. these mappings
may feel a bit trivial (often just exact matches, as in this case), but
for conceptual entities there was quite a lot of manual work required to
align the concepts of the three thesauri, since they often had different
points of view and granularity.
The most frequently used concepts from AGROVOC, CABT, and NALT -- three major
thesauri in the area of food and agriculture -- have been merged into a Global
Agricultural Concept Scheme, with 15,000 concepts and over 350,000 terms in 28
languages in its beta release of May 2016.  This set of core concepts (``GACS
Core'') is seen as the first step towards a more comprehensive Global
Agricultural Concept Scheme.  In the context of a new Agrisemantics initiative,
GACS is intended to serve as hub linking user-oriented thesauri with
semantically more precise and specialized domain ontologies linked, in turn, to
quantitative datasets.  The goal is to improve the discoverability and semantic
interoperability of agricultural information and data for the benefit of
researchers, policy-makers, and farmers in support of innovative responses to
the challenges of food security under conditions of climate change.

The process began in March 2014 with the formation of a joint GACS Working
Group.  After a preliminary analysis found that some 98\% of the indexing
fields in AGRIS used just 10,000 out of the 32,000--plus concepts in AGROVOC,
mapping began with three selections of 10,000 most frequently used concepts.
These were algorithmically mapped to each other, pairwise, by adapting the
AgreementMakeLight ontology matching
system\footnote{\url{https://github.com/AgreementMakerLight/AML-Jar}}; mappings
were verified by hand; a second algorithm checked for clusters of inconsistent
mappings (``lumps''); the lumps were discussed online or in meetings; as a
result of decisions taken, the mappings were corrected by hand (to remove
mappings or to change their meaning); and the corrected mappings were used to
generate new concepts algorithmically.  Concepts in the new concept scheme were
given URIs in a new namespace\footnote{\url{http://id.agrisemantics.org/gacs/}}
and represented in RDF using the W3C standard, Simple Knowledge Organization
Scheme (SKOS).\footnote{\url{https://www.w3.org/TR/skos-reference/}}  This
initial set of core concepts is called GACS Core in the expectation that GACS
will become more comprehensive in scope and less centralized in its
maintenance.

ABOUT GACS

The idea for GACS emerged out of discussions at the World Congress of IAALD, the International Association of Agricultural Information Specialists, in July 2013. The Food and Agricultural Organization of the United Nations (FAO), CAB International (CABI), and the National Agricultural Library of the USA (NAL) agreed in October 2013 to explore the feasibility of developing a shared concept scheme by integrating their three thesauri: the AGROVOC Concept Scheme, the CAB Thesaurus (CABT), and NAL Thesaurus (NALT).

The goal of the GACS project is to create a Global Agricultural Concept Scheme as a hub for thesauri in the agricultural field, in multiple languages, for use in Linked Data.

GACS IN THREE PHASES

The GACS project foresees three phases:

Phase One: Feasibility Study (concluded).
The publication of a paper on the status quo of each thesaurus and a report on how to integrate the three thesauri into a Global Agricultural Concept Scheme (both accessible from this post).

Phase Two: GACS Beta
The creation and refinement of a new concept scheme mapped to and from a selection of circa 10,000 frequently used concepts from AGROVOC, CABT, and NALT.

Phase Three: GACS 1.0 and beyond
If resources are available for building GACS into more than the circa 10,000 concepts of GACS Beta, the GACS editorial team will develop an integrated semantic super-structure for the concept scheme, collaborate with concept providers on naming things like species, viruses, and chemicals with Linked Data URIs, and extend the GACS partnership to additional organizations and partner thesauri.
The process began in March 2014 with the formation of a joint GACS Working
Group.  After a preliminary analysis found that some 98\% of the indexing
fields in AGRIS used just 10,000 out of the 32,000--plus concepts in AGROVOC,
mapping began with three selections of 10,000 most frequently used concepts.
These were algorithmically mapped to each other, pairwise, by adapting the
AgreementMakeLight ontology matching
system\footnote{\url{https://github.com/AgreementMakerLight/AML-Jar}}; mappings
were verified by hand; a second algorithm checked for clusters of inconsistent
mappings (``lumps''); the lumps were discussed online or in meetings; as a
result of decisions taken, the mappings were corrected by hand (to remove
mappings or to change their meaning); and the corrected mappings were used to
generate new concepts algorithmically.  Concepts in the new concept scheme were
given URIs in a new namespace\footnote{\url{http://id.agrisemantics.org/gacs/}}
and represented in RDF using the W3C standard, Simple Knowledge Organization
Scheme (SKOS).\footnote{\url{https://www.w3.org/TR/skos-reference/}}  This
initial set of core concepts is called GACS Core in the expectation that GACS
will become more comprehensive in scope and less centralized in its
maintenance.
