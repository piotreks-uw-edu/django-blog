from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post


class PostListView(ListView):
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__exact=None) \
        .order_by('-published_date')


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
