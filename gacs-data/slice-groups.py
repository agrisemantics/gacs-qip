#!/usr/bin/env python3

import fileinput
import subprocess

from rdflib import Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DCTERMS

LUXID = Namespace('http://www.temis.com/luxid-schema#')

def parse_uri(uri):
    """strip < > and convert to URIRef"""
    return URIRef(uri[1:-1])
    
def slice_filename(slice):
    return "gacs-group-%s.nt" % slice

outfiles = {} # key: slice, value: file object

for line in fileinput.input():
    line = line.strip()
    s, p, o = line.split(' ', maxsplit=2)
    o = o[:-1].strip() # remove trailing dot
    p = parse_uri(p)
    if p == SKOS.member:
        slice = 'members'
    elif p == LUXID.memberOf:
        slice = 'members'
        # invert the triple
        line = "<%s> <%s> <%s> ." % (parse_uri(o), SKOS.member, parse_uri(s))
    else:
        slice = 'defs'
    if slice not in outfiles:
        # pipe the output through a sort command to ensure ordered outputs
        outfile = open(slice_filename(slice), 'w')
        sort = subprocess.Popen(['sort'], stdin=subprocess.PIPE, stdout=outfile)
        outfiles[slice] = sort.stdin
    outfiles[slice].write((line + "\n").encode('UTF-8'))
