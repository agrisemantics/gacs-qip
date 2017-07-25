### Purpose of GACS

These guidelines provide documentation for the maintenance of the Global
Agricultural Concept Scheme (GACS).  Principles of its construction, direction
for decision-making during maintenance, and ultimately provides a record of its
history.  The guidelines are not seen as a one-time creation, but a living
document that will be amended as GACS evolves.  

The maintenance of GACS is envisioned to be distributed among organizations
across the globe in the agricultural community.  The guidelines provide a
central location for the norms executed in the concept scheme and therefore
aids in communication and understanding across organizations.  Adherence to the
guidelines and best practices outlined here will enable GACS Editors to create
and maintain a concept scheme with usable and consistent vocabulary regardless
of location.  

The guidelines are created not to supplant any standard, but to address
specific items from standards that apply to GACS.  Certainly, not all
individuals have access to the standards (i.e. ISO 25964, SKOS) or have full
understanding of these lengthy documents. The guidelines for GACS serve as a
list of best practices to meet the various needs of the partners without
assuming knowledge of or experience with any standards. 

[What GACS is.  GACS as a 'concept scheme'.  Origins in three thesauri. How
'concept scheme' differs (or not!) from 'thesaurus'.  Use of standards in its
construction, such as ISO 25964.  Use of SKOS in its expression.  Concepts
(identified with unique URIs) versus labels (terms).  Use of concept URIs in
Linked Data.  Use of preferred labels (unique terms) for indexing in retrieval
systems.  Multilinguality.]

Uses of GACS

* Controlled set of concepts (controlled vocabulary?) for the subject indexing
  of agricultural research projects, agricultural literature, and other
  agricultural materials.  Use in Linked Data: when tagged with GACS URIs and
  indexed by search engines, resources discoverable on global scale.  

* "Smart searching": provides a means of enhancing recall and precision for the
  searcher without the searcher's knowledge of the thesaurus.  Hierarchy can be
  used to make searches more inclusive: an inclusive search is where terms
  narrower than the search terms are added to queries.  Searches may also be
  enhanced by use of related concepts.  

* Support to automated indexing systems

* Multilinguality: terminology across languages.

Principles for GACS concepts

* Each concept in GACS is identified with a unique URI.  [Stability of URIs can
  be discussed elsewhere] 
* Each concept has at least one preferred label, which has a language
  designation or designated as a scientific name.
* Each concept has only one preferred label per language.  [Note: en-us and
  en-gb considered as separate languages].
* All labels (either preferred or alternative) in one language (or designated
  as scientific name) are unique strings.
* Alternate labels are optional for each concept.
* Hidden labels, which are in the SKOS Reference are not used in GACS at 
  this time.

See [GACS browser](http://browser.agrisemantics.org/gacs/en/).
