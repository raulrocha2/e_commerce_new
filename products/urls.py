from django.conf.urls import url

from products.views import ProductListView, ProductDetailSlugView, product_list_view, ProductDetailView, product_detail_view, ProductFeaturedListView, ProductFeaturedDetailView
app_name = "products"

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    #url(r'^produtos/', ProductDetailView.as_view()),
    #url(r'^produtos-fbv/', product_detail_view),
    # url(r'^produtos', ProductListView.as_view()),
    url(r'(?P<slug>[\w_-]+)/', ProductDetailSlugView.as_view(), name='detail')


]