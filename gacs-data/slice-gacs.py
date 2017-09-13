#!/usr/bin/env python3

import fileinput
import subprocess

from rdflib import Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL, SKOS, DCTERMS

SKOSXL = Namespace('http://www.w3.org/2008/05/skos-xl#')
DWC = Namespace('http://rs.tdwg.org/dwc/terms/')
VB = Namespace('http://art.uniroma2.it/ontologies/vocbench#')
AGVOC = Namespace('http://id.agrisemantics.org/vocab#')
LUXID = Namespace('http://www.temis.com/luxid-schema#')

TYPE_PROPS = set([
    RDF.type,
])

STRUCTURAL_PROPS = set([
    SKOS.inScheme,
    SKOS.hasTopConcept,
    SKOS.topConceptOf,
    SKOS.broader,
    SKOS.related,
])

PRODUCT_PROPS = set([
    AGVOC.hasProduct,
    AGVOC.productOf,
    LUXID.hasProduct,
])

MAPPING_PROPS = set([
    SKOS.exactMatch,
    SKOS.closeMatch,
    SKOS.broadMatch,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
])

DEFERRED_PROPS = set([
    SKOS.definition,
    SKOSXL.prefLabel,
    SKOSXL.altLabel,
])

DEFERRED_SUBJECT_PROPS = set([
    DWC.scientificNameAuthorship,
    DCTERMS.source,
])

LANGUAGE_PROPS = set([
    SKOS.note,
    SKOS.scopeNote,
    SKOS.editorialNote,
    SKOSXL.literalForm,
    RDF.value,
])

ONTOLOGY_PROPS = set([
    RDFS.subClassOf,
    RDFS.subPropertyOf,
    RDFS.label,
    RDFS.domain,
    RDFS.range,
    OWL.inverseOf,
    OWL.versionInfo,
])
    

VOCBENCH_PROPS = set([
    VB.hasStatus,
    DCTERMS.created,
    DCTERMS.modified,
])

def parse_uri(uri):
    """strip < > and convert to URIRef"""
    return URIRef(uri[1:-1])
    
def slice_filename(slice):
    return "gacs-%s.nt" % slice

def choose_slice(s, p, o):
    p = parse_uri(p)
    if p in TYPE_PROPS:
        if o.startswith('_'): # what are these blank node types???
            return 'misc'
        
        o = parse_uri(o)
        if o == SKOS.Concept or o == SKOS.ConceptScheme:
            return 'structure'
        elif o == SKOSXL.Label or o == AGVOC.Definition:
            return 'defer-subj'
        elif o.startswith(OWL):
            return 'ontology'
        else:
            return 'types'
    if p in STRUCTURAL_PROPS:
        return 'structure'
    if p in PRODUCT_PROPS:
        return 'product'
    if p in MAPPING_PROPS:
        return 'mapping'
    if p in ONTOLOGY_PROPS:
        return 'ontology'
    if p in VOCBENCH_PROPS:
        return 'vocbench'
    if p in DEFERRED_PROPS:
        # try to parse language in case it's a literal
        if '@' in o:
            lang = o.split('@')[1].split()[0]
            return 'lang-%s' % lang
        return 'defer' # defer until we know the language of the object
    if p in DEFERRED_SUBJECT_PROPS:
        return 'defer-subj' # defer until we know the language of the subject
    if p in LANGUAGE_PROPS:
        lang = o.split('@')[1].split()[0]
        lang_of_deferred[parse_uri(s)] = lang
        return 'lang-%s' % lang
    if p == SKOS.narrower:
        return 'narrower' # not really useful, but...
    return 'misc'

outfiles = {} # key: slice, value: file object
deferred = {} # key: object URIRef, value: list of lines (N-Triples syntax)
lang_of_deferred = {} # key: subject URIRef, value: language code

for line in fileinput.input():
    line = line.strip()
    s, p, o = line.split(' ', maxsplit=2)
    o = o[:-1].strip() # remove trailing dot
    slice = choose_slice(s, p, o)
#    print(s, p, o, slice)
    if slice == 'defer':
        deferred.setdefault(parse_uri(o), [])
        deferred[parse_uri(o)].append(line)
    elif slice == 'defer-subj':
        deferred.setdefault(parse_uri(s), [])
        deferred[parse_uri(s)].append(line)
    else:
        if slice not in outfiles:
            # pipe the output through a sort command to ensure ordered outputs
            outfile = open(slice_filename(slice), 'w')
            sort = subprocess.Popen(['sort'], stdin=subprocess.PIPE, stdout=outfile)
            outfiles[slice] = sort.stdin
        outfiles[slice].write((line + "\n").encode('UTF-8'))

for uri, lines in deferred.items():
    slice = 'lang-%s' % lang_of_deferred[uri]
    for line in lines:
        file=outfiles[slice].write((line + "\n").encode('UTF-8'))
