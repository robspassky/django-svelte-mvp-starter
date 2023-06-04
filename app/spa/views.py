from django.views.generic import TemplateView
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required  # for function-based views
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('spa')
        else:
            return super().dispatch(request, *args, **kwargs)

class SpaView(LoginRequiredMixin, TemplateView):
    template_name = 'spa/index.html'
