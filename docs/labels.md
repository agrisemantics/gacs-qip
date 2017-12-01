A concept scheme, GACS is based on "concepts" -- abstract entities, or
"units of thought", seen as independent from the natural-language terms used to
express them.  Concepts are identified with URIs, and these URIs are often 
used to tag resources for purposes of indexing and retrieval.

As GACS vocabulary has its origins in three thesauri, it is natural that the
thesaurus standards concerning concepts and labels along with the SKOS
Reference guidelines are considered. 

In thesaurus standards, natural-language "terms" are used to express concepts,
usually in the form of single nouns or noun phrases (e.g., "habitats" or
"habitat conservation").   According to ISO 25964-1 5.1.1, each term in the
thesaurus is required to be unique and only represent one concept. In other
words, if the word "lime" denotes both a fruit and a mineral it is not allowed
to label the two separate concepts for lime with the same label ("lime") -- the
labels must be made unique, perhaps by adding parenthetical qualification
("lime (mineral)") or by unambiguously expressing the concept so that the
meaning is clear ("lime fruits").

Terms in a thesaurus can be either "preferred terms" or "non-preferred terms". 

Terms that are used for subject indexing, "preferred terms", are also known as
"descriptors". In the decades-old tradition of information-retrieval thesauri,
resources are tagged for the purposes of indexing and retrieval using
"preferred terms". The precision of term-based indexing depends on the
uniqueness of the strings used to encode the terms. In production environments,
for example when thesauri are used in complex workflows, it is important that
preferred terms also remain stable. 

Terms other than preferred terms are "non-preferred terms", or non-descriptors.
Because non-descriptors are used to direct users to preferred terms, they are
also known as "lead-in-terminology".  According to thesaurus standards,
non-descriptors may not be used to tag resources for indexing and retrieval.

In SKOS, the distinction between preferred and non-preferred terms is expressed
with the properties skos:prefLabel and skos:altLabel.  In accordance with
thesaurus practice, the SKOS specification prescribes that a concept not have
two preferred labels in a given language and recommends that preferred labels
in a given language be unique within the context of a given concept scheme
(e.g., that no two concepts share the prefLabel "lime"@en).  In accordance with
the SKOS specification, it is an error if a concept has a same literal both as
its preferred label and as an alternative label.

In GACS (as approved 2016-02-09):

1. Preferred labels MUST be unique for the core languages of GACS. That 
   is, one concept MUST NOT have the same preferred label as another 
   concept in the same (core) language.
   Note: "unique" is case insensitive.

2. Preferred labels SHOULD be unique for the other (non-core) languages 
   of GACS. That is, one concept SHOULD NOT have the same preferred label as 
   another concept in the same (non-core) language.

3. In core languages, an alternate label MUST NOT be identical to a 
   preferred label of another concept.

4. In other (non-core) languages, an alternate label SHOULD NOT be 
   identical to a preferred label of another concept.

5. Alternate labels MUST be unique for the core languages of GACS. That 
   is, one concept MUST NOT have the same alternate label as another 
   concept in the same (core) language.

6. Alternate labels SHOULD be unique for the other (non-core) languages 
   of GACS. That is, one concept SHOULD NOT have the same alternate label as 
   another concept in the same (non-core) language.

Given sufficient resources for translation, labels in all languages should
ideally follow the restrictions for English, Spanish, and scientific names.

