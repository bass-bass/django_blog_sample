from django.urls import path
from blog.views import IndexView, AboutView, ContactFormView, ContactResultView, PostDetailView, TagListView, SearchPostView, TagPostView, CommentFormView, comment_approve, comment_remove, ReplyFormView, reply_approve, reply_remove
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("contact/contact_result/", ContactResultView.as_view(), name="contact_result"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    path('comment/<int:pk>/', CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', ReplyFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', reply_remove, name='reply_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)