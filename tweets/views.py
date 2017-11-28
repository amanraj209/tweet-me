from django.views.generic import ListView, DetailView, CreateView

from .models import Tweet
from .forms import TweetModelForm


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/tweet_form.html'
    success_url = '/tweet/create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


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

