# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:38:54 2022

@author: ASUS
"""

from django.urls import path
from .views import (BlogListView, 
		BlogDetailView, 
		BlogCreateView, 
		BlogDeleteView, 
		BlogUpdateView, 	  
)

urlpatterns = [
        path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name= 'post_delete'),
	path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name= 'post_edit'),
	path('post/new/', BlogCreateView.as_view(), name='post_new'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        path('', BlogListView.as_view(), name='home'),
	
]
