from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Tweet


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context

