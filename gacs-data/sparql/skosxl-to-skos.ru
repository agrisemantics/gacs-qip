PREFIX skos:   <http://www.w3.org/2004/02/skos/core#> 
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>

INSERT {
  ?c skos:prefLabel ?pref . 
  ?c skos:altLabel ?alt . 
} WHERE {
  { ?c skosxl:prefLabel/skosxl:literalForm ?pref } 
  UNION 
  { ?c skosxl:altLabel/skosxl:literalForm ?alt } 
}
