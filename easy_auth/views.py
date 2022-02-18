from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.views.generic.base import RedirectView


class EasyAuthLoginView(RedirectView):
    pattern_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        user = authenticate(request)
        if not user:
            return LoginView.as_view(template_name=getattr(
                settings, 'LOGIN_TEMPLATE', 'admin/login.html'))(request)

        login(request, user)
        redirect_to = self.get_redirect_url(*args, **kwargs)
        if redirect_to == self.request.path:
            raise ValueError(
                "Redirection loop for authenticated user detected. Check that "
                "your LOGIN_REDIRECT_URL doesn't point to a login page."
            )

        return HttpResponseRedirect(redirect_to)
