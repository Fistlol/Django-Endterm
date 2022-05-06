from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
from main.views.views_cbv import *
from main.views.views_fbv import *
from main.views.views_set import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view()),
    path('sales/', SaleListAPIView.as_view()),
    path('login/', obtain_jwt_token),
    path('search/<search_request>/', get_needed_products),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('subcategories/<int:id>/products', subcat_products),
    path('categories/<int:id>/subcategories', subcategory_list),
    path('subcategories/<int:id>', getSubcategory),
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('appeals/', AppealListAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
