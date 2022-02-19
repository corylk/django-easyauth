from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect


class EasyAuthLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated is False:
            user = authenticate(request)
            if user is not None:
                login(request, user)
                redirect_to = self.get_success_url()
                if redirect_to != self.request.path:
                    return HttpResponseRedirect(redirect_to)
        return LoginView.as_view(template_name=self.template_name,
            redirect_authenticated_user=self.redirect_authenticated_user)(request)
