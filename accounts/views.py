from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

User = get_user_model()


class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/user_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))