# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2013 NovaReto GmbH
# # cklinger@novareto.de


import re
import spacy
import textacy

from uvc.api import api
from zope.interface import Interface
from gensim.summarization.summarizer import summarize
from plone.app.contenttypes.interfaces import IDocument
from plone.app.layout.viewlets.interfaces import IBelowContent



def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


class SummaryViewlet(api.Viewlet):
    api.context(IDocument)
    api.viewletmanager(IBelowContent)

    def render(self):
        cleaned = cleanhtml(self.context.text.raw)
        return "<div> %s </div>" % summarize(cleaned)
