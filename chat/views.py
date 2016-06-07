from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = 'chat/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
