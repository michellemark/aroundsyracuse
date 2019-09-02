from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

from sellers.forms import SellerProfileForm
from sellers.models import SellerProfile


class SellerProfileView(TemplateView):
    """First step in seller free evaluation workflow"""
    template_name = 'seller-free-evaluation-profile.html'
    form = SellerProfileForm

    def get_context_data(self, **kwargs):
        context = super(SellerProfileView, self).get_context_data(**kwargs)
        context['page_title'] = "Free home evaluation request - Step 1"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form(
            initial={'property_type': SellerProfile.SINGLE_FAMILY_HOME}
        )

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form(request.POST)

        if context['form'].is_valid():
            context['form'].save()

            return redirect('sellerstep1')

        return render(request, self.template_name, context)

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):

        return super(SellerProfileView, self).dispatch(*args, **kwargs)
