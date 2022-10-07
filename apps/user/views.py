from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from social_django.models import UserSocialAuth


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return super().get(request, *args, **kwargs)


class SettingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None

        try:
            twitter_login = user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            twitter_login = None

        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'core/settings.html', {
            'github_login': github_login,
            'twitter_login': twitter_login,
            'facebook_login': facebook_login,
            'can_disconnect': can_disconnect
        })
