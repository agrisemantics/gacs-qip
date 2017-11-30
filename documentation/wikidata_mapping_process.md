### Process for mapping to Wikidata

2017-11-30

Following an [NKOS 2017
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

Note that as of November 2017, Wikidata has worked with just one kind of
mapping relationship and does not differentiate among exact, close, broader,
narrower, or related matches; on the GACS side, the mappings were interpreted
as "close" matches -- the natural equivalent for an unspecified mapping
relationship in the SKOS model -- though a facility for expressing relationship
types was [under
development](https://www.wikidata.org/wiki/Wikidata:Property_proposal/mapping_relation_type).
