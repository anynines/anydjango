from django.views.generic import TemplateView
from django.template import Context
import sys

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        cur_version = sys.version
        context = Context({
            'greeting': 'Hello Python, welcome to anynines.com !',
            'python_version': cur_version,
        })
        return self.render_to_response(context)
