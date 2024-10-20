# blog/apps/post/views.py
from django.views.generic import TemplateView
# TODO: Cambiar TemplateView por DetailView para que se pueda ver el detalle de un post
class PostDetailView(TemplateView):
    template_name = 'post/post_detail.html'
    

class PostUpdateView(TemplateView):
    template_name = 'post/post_update.html'

class PostDeleteView(TemplateView):
    template_name = 'post/post_delete.html'