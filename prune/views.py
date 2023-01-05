from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import *


class TransactionPostView(FormView):
    form_class = TransactionForm
    template_name = 'prune/prune_post.html'
    success_url = '.'

    def form_valid(self, form):
        form.save()
        self.extra_context = {"success": "Data is saved"}
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        return super(TransactionPostView, self).post(request, *args, **kwargs)


class TransactionGetView(TemplateView):
    template_name = 'prune/prune_get.html'

    def get(self, request, *args, **kwargs):
        self.extra_context = {'data': Transactions.objects.all()}
        return super(TransactionGetView, self).get(request, *args, **kwargs)

