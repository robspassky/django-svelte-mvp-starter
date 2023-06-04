from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required  # for function-based views
from django.contrib.auth.mixins import LoginRequiredMixin

class SpaView(LoginRequiredMixin, TemplateView):
    template_name = 'spa/index.html'
