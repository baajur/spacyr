#!/usr/local/bin/python

# Sources:
#  Google universal: http://www.petrovi.de/data/universal.pdf
#  Penn treebank: http://web.mit.edu/6.863/www/PennTreebankTags.html
# Requires installation of spaCy: https://honnibal.github.io/spaCy/
#
# written by Paul Nulty, 19 March 2015

# from __future__ import unicode_literals 
import os
import sys
import argparse
import codecs
import spacy.en
from spacy.parts_of_speech import *
from spacy.lemmatizer import Lemmatizer
import re
import time

#nlp = spacy.en.English()


class spacyr:
    def __init__(self):
        self.nlp = spacy.en.English()
        self.documents = {}
    
    def parse(self, texts):
        epoch_nanos = []
        if isinstance(texts, list) == False:
            texts = [texts]
        for text in texts:
            epoch_nano = int(time.time() * 1000000)
            doc = self.nlp(unicode(text))
            self.documents[epoch_nano] = doc
            epoch_nanos.append(epoch_nano)
        return epoch_nanos 
    
    def attributes(self, timestamps, attrname):
        all_attrs = {}
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            c_document = self.documents[ts]
            attrs = []
            for w in c_document:
                attrs.append(getattr(w, attrname))
            all_attrs[ts] = attrs
        return all_attrs
    
    def tokens(self, timestamps):
        all_tokens = self.attributes(timestamps, 'orth_')
        return all_tokens

    def tags(self, timestamps, tag_type):
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
        attr_name = "tag_" if tag_type == "penn" else "pos_"
        all_tokens = self.attributes(timestamps, attr_name)
        return all_tokens
        
    def run_entity(self, timestamps):
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            self.nlp.entity(self.documents[ts])
    
    def run_tagger(self, timestamps):
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            self.nlp.tagger(self.documents[ts])

    def run_dependency_parser(self, timestamps):
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            self.nlp.parser(self.documents[ts])
            
    def list_entities(self, timestamps):
        all_entities = {}
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            c_document = self.documents[ts]
            ents = list(c_document.ents)
            entities = []
            for entity in ents:
                entities.append((entity.label_, ' '.join(t.orth_ for t in entity)))
            all_entities[ts] = entities
        return all_entities
        
    def dep_head_id(self, timestamps):
        all_head_ids = {}
        if isinstance(timestamps, list) == False:
            timestamps = [timestamps]
        for ts in timestamps:
            ts = int(ts)
            c_document = self.documents[ts]
            head_ids = []
            for w in c_document:
                head_ids.append(w.head.i)
            all_head_ids[ts] = head_ids
        return all_head_ids

# def tokens(self, timestamps):
    #     all_tokens = {}
    #     if isinstance(timestamps, list) == False:
    #         timestamps = [timestamps]
    #     for ts in timestamps:
    #         ts = int(ts)
    #         c_document = self.documents[ts]
    #         tokens = []
    #         for w in c_document:
    #             tokens.append(w.orth_)
    #         all_tokens[ts] = tokens
    #     return all_tokens
    # 
    # def tags(self, timestamps):
    #     all_tags = {}
    #     if isinstance(timestamps, list) == False:
    #         timestamps = [timestamps]
    #     for ts in timestamps:
    #         ts = int(ts)
    #         c_document = self.documents[ts]
    #         tags = []
    #         for w in c_document:
    #             tags.append(w.tag_)
    #         all_tags[ts] = tags
    #     return all_tags
    # 
    # def entities(self, timestamps):
    #     all_entities = {}
    #     for ts in timestamps:
    #         ts = int(ts)
    #         c_document = self.documents[ts]
    #         ts = int(ts)
    #         entities = []
    #         for w in c_document:
    #             entities.append(w.ent_type_)
    #         all_entities[ts] = entities
    #     return all_entities

spobj = spacyr()

# def parse(texts):
#     epoch_nano = int(time.time() * 1000)
#     spacy_documents[epoch_nano] = nlp(texts)
# 
# def tag(timestamp, mode):
#     return 0
# 
    
  