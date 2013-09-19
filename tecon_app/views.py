# coding: utf-8

from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from braces.views import LoginRequiredMixin
from categories.models import Category
from tecon_app.forms import TrialForm
from tecon_app.models import Trial


class TeconView(generic.TemplateView):
    template_name = "tecon/main.html"

    #number of tests in last_tests list on the main page
    LAST_GOOD_TESTS_NUM = 15

    def get_context_data(self, **kwargs):
        ctx = super(
            TeconView, self).get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        ctx['last_good_tests'] = Trial.objects.filter(
            status=Trial.STATUS.good
        ).order_by('-created')[:self.LAST_GOOD_TESTS_NUM]
        #ctx['top_rated_tests'] = Trial.objects.filter().order_by('-rating')
        return ctx


class TestListView(generic.ListView):
    template_name = 'tecon/test_list.html'
    model = Trial

    def get_context_data(self, **kwargs):
        ctx = super(TestListView, self).get_context_data(**kwargs)
        ctx['tests'] = self.filter_qs(ctx['object_list'])
        ctx['category'] = self.get_category()
        ctx['categories'] = Category.objects.all()
        return ctx

    def filter_qs(self, qs):
        category = self.get_category()
        if category:
            categories = category.get_descendants(include_self=True)
            qs = qs.filter(category__in=categories)
        order = self.request.GET.get('order', '-id')
        if order:
            qs = qs.order_by(order)
        return qs

    def get_category(self):
        category_id = self.request.GET.get('category_id', None)
        if category_id:
            category_qs = Category.objects.filter(id=category_id)[:1]
            if category_qs:
                return category_qs[0]
        return None


class CreateTestView(LoginRequiredMixin, generic.TemplateView):
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
            request.session['created_test_id'] = trial.id
            return HttpResponseRedirect(reverse('tecon:success_test_creation'))
        return self.render_to_response(ctx)


class SuccessfullyCreatedView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'tecon/successfully_created.html'

    def get_context_data(self, **kwargs):
        ctx = super(SuccessfullyCreatedView, self).get_context_data(**kwargs)
        created_test_id = self.request.session.get('created_test_id', None)
        if created_test_id:
            ctx['test_url'] = reverse(
                'tecon:test_details', kwargs=dict(test_id=created_test_id))
        ctx['test'] = self.request.session.get('created_test', None)
        return ctx


class UserTestsView(generic.TemplateView):
    template_name = "tecon/user_tests.html"

    def get_context_data(self, **kwargs):
        ctx = super(
            UserTestsView, self).get_context_data(**kwargs)
        ctx['tests'] = Trial.objects.filter(user=self.request.user)
        return ctx


class TestDetailView(generic.TemplateView):
    template_name = "tecon/test_details.html"

    def get_context_data(self, **kwargs):
        ctx = super(
            TestDetailView, self).get_context_data(**kwargs)
        ctx['test'] = get_object_or_404(Trial, id=kwargs.get('test_id', None))
        return ctx


class EditTestView(LoginRequiredMixin, generic.TemplateView):
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
