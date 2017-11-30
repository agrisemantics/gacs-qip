### Mapping to Wikidata

As an experiment, the 540 place names in GACS (formally: concepts of type
_Geographical_) have been mapped to Wikidata.  Following an [NKOS 2017
paper by Joachim Neubert](http://ceur-ws.org/Vol-1937/paper2.pdf), the 
mapping process involved:

1. Requesting a Wikidata identifier property for GACS concept identifiers
   which, after [discussion in the Wikidata
   community](https://www.wikidata.org/wiki/Wikidata:Property_proposal/GACS_ID),
   resulted in the creation of the property
   [https://www.wikidata.org/wiki/Property:P4427](https://www.wikidata.org/wiki/Property:P4427).
   (See also the [Wikidata entry for GACS](https://www.wikidata.org/wiki/Q42519707).

2. Creating a project (or
   ["catalog"](https://tools.wmflabs.org/mix-n-match/#/catalog/639)) in a
   software tool for mapping, "Mix'n'match", using a [CSV file listing the GACS
   concepts to be
   mapped](https://github.com/agrisemantics/gacs-qip/tree/master/wikidata).

3. Verifying the suggested matches in Mix'n'match, one by one, and manually
   searching for Wikidata entities that match any non-matched GACS concepts.
   Mix'n'match provides a "game mode" usable on mobile phones for crowdsourcing
   the verification process.

4. Querying Wikidata for mappings to GACS and adding the triples to GACS.

The mappings to Wikidata facilitate access from GACS both to information
Wikidata has about geographic places (such as coordinates, population,
language, and religions) and to Wikidata mappings to other geo-oriented
vocabularies such as GeoNames and OpenStreetMap and to library-oriented
authority files such as the Library of Congress Name Authority File, GND
(German union authority), BNF, VIAF and ISNI. As an example, see the Wikidata
entry for [Alberta](https://www.wikidata.org/wiki/Q1951)) and the corresponding
[GACS
concept](http://tester-os-kktest.lib.helsinki.fi/gacsdemo/gacs/en/page/C15421).
(Note that as of November 2017, Wikidata has worked with just one kind of
mapping relationship and does not differentiate among exact, close, broader,
narrower, or related matches; on the GACS side, the mappings were interpreted
as "close" matches -- the natural equivalent for an unspecified mapping
relationship in the SKOS model -- though a facility for expressing relationship
types was [under
development](https://www.wikidata.org/wiki/Wikidata:Property_proposal/mapping_relation_type).

#### Deferring to external authorities

One potential future scenario for GACS involves devolving or delegating
responsibility for specific types of GACS concepts to external authorities.
Geographic places are an obvious candidate for delegation because they are not
specific to agriculture and because they have been given URIs in so many other
sources.  Once mapped to a external source, a given set of GACS concepts could
be reduced to a set of URIs clearly marked as dependent on the external URIs,
and use of the external URIs could be promoted.  Note that GACS concepts cannot
simply be deleted because their URIs need to be credibly persistent, in
accordance with explicit policies, if GACS itself is to be credibly deployable.
The GACS URIs also provide a fallback option if the external authority should
ever cease operation, a contingency that should always be anticipated by
policy.


