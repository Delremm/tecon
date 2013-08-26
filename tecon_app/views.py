# coding: utf-8

from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin

from tecon_app.forms import TrialForm
from tecon_app.models import Trial


class TeconBase(LoginRequiredMixin, generic.TemplateView):
    """
    Base class contains LoginRequiredMixin
    """
    raise_exception = True


class TeconView(TeconBase):
    template_name = "tecon/main.html"


class CreateTestView(TeconBase):
    template_name = "tecon/create_test.html"

    def get_context_data(self, **kwargs):
        ctx = super(
            CreateTestView, self).get_context_data(**kwargs)
        ctx['test_form'] = TrialForm()
        return ctx

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        form = TrialForm(request.POST or None)
        if form.is_valid():
            trial = Trial()
            trial.title = form.cleaned_data['title']
            trial.description = form.cleaned_data['description']
            trial.user = request.user
            trial.data = request.POST.get('data', '')
            trial.save()
            return HttpResponseRedirect(reverse('tecon:success_test_creation'))
        return self.render_to_response(ctx)


class UserTestsView(TeconBase):
    template_name = "tecon/user_tests.html"
