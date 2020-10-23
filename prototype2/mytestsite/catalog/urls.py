from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^goods/$', views.GoodListView.as_view(), name='goods'),
    path(r'^good/(?P<pk>\d+)$', views.GoodDetailView.as_view(), name='good-detail'),
    path(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    path(r'^category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
    path(r'^manufacturers/$', views.ManufacturerListView.as_view(), name='manufacturers'),
    path(r'^manufacturer/(?P<pk>\d+)$', views.ManufacturerDetailView.as_view(), name='manufacturer-detail'),

    path(r'^basket/$', views.basket, name='basket'),
    path(r'^favorites/$', views.favorites, name='favorites'),
    path(r'^contacts/$', views.contacts, name='contacts'),
    path(r'^authorization/$', views.authorization, name='authorization'),

    path(r'^find/$', views.find, name='find'),
    path(r'^find/search_goods/$', views.SearchGoodList.as_view(), name='search_goods'),

    path(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    path(r'^login/$', views.LoginFormView.as_view(), name='login'),
    path(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
