from django.conf.urls import url

from .views import ProductListView, ProductDetailSlugView

urlpatterns = [
    url(r'', ProductListView.as_view()),
    url('<slug:slug>/', ProductDetailSlugView.as_view())
    #url(r'^(?P<slug>[\w_-]+)/', ProductDetailSlugView.as_view(), ),
    # url(r'^produtos/', ProductDetailView.as_view()),
    #url(r'^produtos-fbv/', product_detail_view),
    # url(r'^produtos', ProductListView.as_view()),
    #url(r'^produtos-fbv', product_list_view),
    #url(r'^destaque/', ProductFeaturedListView.as_view()),
    #url(r'^destaque/', ProductFeaturedDetailView.as_view()),
]