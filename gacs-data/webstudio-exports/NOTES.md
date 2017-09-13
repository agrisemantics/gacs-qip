# Changes made in WebStudio

Notes about changes made between the first export (with no editorial changes w.r.t. GACS Beta 3.1) and the currently last one (2017-08-28)

## Removed triples, by RDF property

    $ diff -u gacs-webstudio-2017-05-25.nt gacs-webstudio-2017-08-28.nt |grep '^-'|cut -d ' ' -f 2|sort|uniq -c|sort -nr
       1416 <http://www.w3.org/2004/02/skos/core#broader>
        507 <http://www.w3.org/2004/02/skos/core#topConceptOf>
         81 <http://www.temis.com/luxid-schema#memberOf>
         18 <http://www.w3.org/2004/02/skos/core#related>
          8 <http://www.w3.org/2004/02/skos/core#scopeNote>
          8 <http://www.w3.org/2004/02/skos/core#prefLabel>
          4 <http://www.w3.org/2004/02/skos/core#definition>
          1 gacs-webstudio-2017-05-25.nt	2017-09-13

## Added triples, by RDF property	

    $ diff -u gacs-webstudio-2017-05-25.nt gacs-webstudio-2017-08-28.nt |grep '^+'|cut -d ' ' -f 2|sort|uniq -c|sort -nr
       2839 <http://www.temis.com/luxid-schema#memberOf>
       1128 <http://www.w3.org/2004/02/skos/core#broader>
        419 <http://www.w3.org/2004/02/skos/core#related>
         43 <http://www.w3.org/2004/02/skos/core#definition>
         31 <http://www.w3.org/2004/02/skos/core#prefLabel>
         23 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>
          2 <http://www.w3.org/2004/02/skos/core#scopeNote>
          1 gacs-webstudio-2017-08-28.nt	2017-09-13


## Explanations

 * skos:broader: these are the hierarchy changes made by Lori
 * skos:topConceptOf removals: consequence of hierarchy changes (can be
   ignored)
 * luxid:memberOf: changes to thematic group membership made by Lori (note
   that these use a non-standard property, needs to be converted to
   skos:member)
 * skos:related: side effects of hierarchy changes, e.g. sometimes BT becomes RT
 * skos:scopeNote: changes made by Lori, e.g. when the scope note
   is inappropriate for GACS
 * skos:prefLabel: most of these are for newly inserted top-level concepts
   that structure the hierarchy, but the removals need to be investigated
   further and possibly manually copied to the original SKOS-XL labels
 * skos:definition: need to be investigated and possibly manually copied to
   the structured definitions in original GACS data
 * rdf:type: for newly inserted top-level concepts
