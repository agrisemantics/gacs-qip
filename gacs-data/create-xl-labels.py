#!/usr/bin/env python3

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, SKOS

import sys
import zlib

GACS = Namespace('http://id.agrisemantics.org/gacs/')
AGVOC = Namespace('http://id.agrisemantics.org/vocab#')
SKOSXL = Namespace('http://www.w3.org/2008/05/skos-xl#')

input = Graph()
input.parse(sys.stdin.buffer, format='nt')

output = Graph()

for conc, label in input.subject_objects(SKOS.prefLabel):
    crc = hex(zlib.crc32(label.encode('UTF-8')) & 0xffffffff)[2:].zfill(8)
    xl = URIRef(GACS['xl_%s_%s' % (label.language, crc)])
    output.add((conc, SKOSXL.prefLabel, xl))
    output.add((xl, SKOSXL.literalForm, label))
    output.add((xl, RDF.type, SKOSXL.Label))

output.serialize(destination=sys.stdout.buffer, format='nt')
