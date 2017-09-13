# This Makefile specifies rules for creating the published version of GACS.
# The starting point is an export file from VocBench in N-Triples format.
#

# ** CONFIGURATION **

# Paths to tools required in the rules below
# These can be overridden using environment variables of the same names

# path to Skosify installation
SKOSIFYHOME ?= ~/git/Skosify

# rapper tool from raptor2-utils (part of the Redland / librdf suite)
RAPPER ?= rapper

# tools from the Apache Jena suite
RIOT ?= riot
SPARQL ?= sparql

# JVM options to avoid running out of memory
JAVA_OPTS = -Xmx2G

# Slices of the VocBench export that constitute GACS
SLICES ?= $(wildcard slices/gacs-lang-*) slices/gacs-mapping.nt slices/gacs-structure.nt slices/gacs-product.nt slices/gacs-types.nt slices/gacs-extra.nt slices/gacs-group-defs.nt slices/gacs-group-members.nt

# ** RULES **

# Specify the end result
all: gacs.rdf

gacs-merged.nt: $(SLICES)
	$(RIOT) $^ >$@

# Merge the slices and expand GACS with scientific names
gacs-expanded.nt: sparql/expand-gacs.rq gacs-merged.nt
	JVM_ARGS=$(JAVA_OPTS) $(SPARQL) --query $< --data $(filter-out $<,$^) --results=NT >$@

# Process the already expanded GACS via Skosify
# - SKOS XL labels will be converted to SKOS
gacs.ttl: sparql/skosxl-to-skos.ru gacs-metadata.ttl gacs-expanded.nt
	$(SKOSIFYHOME)/skosify/skosify.py \
		--no-enrich-mappings \
		--set-modified \
		--eliminate-redundancy \
		--update-query @$< \
		--debug \
		$(filter-out $<,$^) \
		-o $@ \
		2>skosify.log


# General pattern rule for Turtle to RDF/XML conversion
%.rdf: %.ttl
	$(RAPPER) -i turtle -o rdfxml-abbrev $< >$@

# General pattern rule for uncompressing gzipped N-Triple files
%.nt: %.nt.gz
	zcat $< >$@

clean:
	rm -f gacs.rdf gacs.ttl gacs-expanded.nt skosify.log

# mark that some intermediate files should not be deleted immediately
.SECONDARY: gacs.ttl

# mark that the "all" and "clean" targets are not actually files
.PHONY: all clean
