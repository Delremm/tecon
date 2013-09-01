# coding: utf-8

from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
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

    def get_context_data(self, **kwargs):
        ctx = super(
            UserTestsView, self).get_context_data(**kwargs)
        ctx['tests'] = Trial.objects.filter(user=self.request.user)
        return ctx


class TestDetailView(TeconBase):
    template_name = "tecon/test_details.html"

    def get_context_data(self, **kwargs):
        ctx = super(
            TestDetailView, self).get_context_data(**kwargs)
        ctx['test'] = get_object_or_404(Trial, id=kwargs.get('test_id', None))
        return ctx


class EditTestView(TeconBase):
    template_name = 'tecon/edit_test.html'

    def get_context_data(self, **kwargs):
        ctx = super(
            EditTestView, self).get_context_data(**kwargs)
        trial = get_object_or_404(Trial, id=kwargs.get('test_id', None))
        ctx['test'] = trial
        ctx['test_form'] = TrialForm(instance=trial)
        return ctx

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        if not (request.user == ctx['test'].user):
            raise Http404
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        form = TrialForm(request.POST or None)
        if form.is_valid():
            trial = ctx['test']
            trial.title = form.cleaned_data['title']
            trial.description = form.cleaned_data['description']
            trial.data = request.POST.get('data', '')
            print trial, trial.id
            trial.save()
            return HttpResponseRedirect(reverse('tecon:success_test_creation'))
        return self.render_to_response(ctx)


class DeleteTestView(LoginRequiredMixin, generic.DeleteView):
    #login_required mixin settings
    raise_exception = True

    template_name = 'tecon/delete_test_confirmation.html'
    success_url = reverse_lazy('tecon:user_tests')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = get_object_or_404(Trial, id=self.kwargs.get('test_id', None))
        if not obj.user == self.request.user:
            raise Http404
        return obj

    # def get_context_data(self, **kwargs):
    #     ctx = super(
    #         DeleteTestView, self).get_context_data(**kwargs)
    #     ctx['test'] = get_object_or_404(Trial, id=kwargs.get('test_id', None))
    #     return ctx
