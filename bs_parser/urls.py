#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:19:48 2020

@author: drew
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]