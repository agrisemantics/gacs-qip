#!/usr/bin/env python3

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, SKOS

import sys
import zlib

GACS = Namespace('http://id.agrisemantics.org/gacs/')
AGVOC = Namespace('http://id.agrisemantics.org/vocab#')

input = Graph()
input.parse(sys.stdin.buffer, format='nt')

output = Graph()

for conc, df in input.subject_objects(SKOS.definition):
    crc = hex(zlib.crc32(df.encode('UTF-8')) & 0xffffffff)[2:].zfill(8)
    defn = URIRef(GACS['def_%s' % crc])
    output.add((conc, SKOS.definition, defn))
    output.add((defn, RDF.value, df))
    output.add((defn, RDF.type, AGVOC.Definition))

output.serialize(destination=sys.stdout.buffer, format='nt')
