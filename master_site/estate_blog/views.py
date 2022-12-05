from django.views.generic import ListView, DetailView

from .models import Blog, Category


class BlogView(ListView):
    model = Blog
    queryset = Blog.objects.filter(draft=True).order_by('-date')
    template_name = 'blog/blog-grid.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context


class BlogCategory(ListView):
    model = Blog
    slug_field = 'url'
    template_name = 'blog/blog-grid.html'

    def get_queryset(self):
        return Blog.objects.filter(category__url=self.kwargs['cat_slug'], draft=True).order_by('-date')


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'url'
    template_name = 'blog/blog-single.html'
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог | ' + str(context['blog'].name)
        return context
