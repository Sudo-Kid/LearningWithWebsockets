from django.shortcuts import render
from django.views.generic import View


class Index(View):
    template_name = 'chat/index.html'

    def get(self, request, *args, **kwargs):
        chat_room = self.kwargs['chat_room']
        return render(request, self.template_name, {'chat_room': chat_room})
