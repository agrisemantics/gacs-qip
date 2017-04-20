#!/bin/sh

# query first into Turtle file, since Jena is unable to serialize this into RDF/XML (why?)
tdbquery --loc tdb --query gacs-vb-to-webstudio.rq --results TTL >gacs-webstudio.ttl
# convert from Turtle to RDF/XML using rapper
rapper -i turtle -o rdfxml-abbrev gacs-webstudio.ttl >gacs-webstudio.rdf
