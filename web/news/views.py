from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . import views
import datetime
from .models import News
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsDetailView(LoginRequiredMixin,DetailView):
    model = News
    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(News, slug=self.kwargs['slug'])
        obj.ViewCounter = obj.ViewCounter+1
        obj.save()
        return obj

class NewsListView(LoginRequiredMixin,ListView):
    model = News
    ordering = ['-ViewCounter']
    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(NewsClass=self.kwargs['topic']) 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.kwargs['topic']
        return context

        
class NewsTopicsView(LoginRequiredMixin,TemplateView):
    template_name = "news/topics.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = News.NewsClass.field.choices
        return context


