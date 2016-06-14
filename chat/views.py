from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = 'chat/index.html'
    chat_group= None

    def get(self, request, *args, **kwargs):
        if self.chat_group is None:
            self.chat_group = self.kwargs['chat_group']
        return render(request, self.template_name, {'chat_group':
                      self.chat_group})

