from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect


class EasyAuthLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        user = authenticate(request)
        if not user:
            return super().dispatch(request, *args, **kwargs)

        login(request, user)
        redirect_to = self.get_success_url()
        if redirect_to == self.request.path:
            raise ValueError(
                "Redirection loop for authenticated user detected. Check that "
                "your LOGIN_REDIRECT_URL doesn't point to a login page."
            )

        return HttpResponseRedirect(redirect_to)
