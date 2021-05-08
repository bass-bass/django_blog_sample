from django.db.models import Count, Q

from blog.models import Tag


def common(request):
    context = {
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
    }
    return context