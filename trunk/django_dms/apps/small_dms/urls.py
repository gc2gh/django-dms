#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
      Title: 
    Project: 
     Author: Will Hardy
       Date:  2008
      Usage: 
  $Revision$

Description: 

"""

from django.conf.urls.defaults import *
from django_dms.apps.small_dms.views import document_view

urlpatterns = patterns('',
    url(r'^',  include(document_view),  name="document_view"),
)
