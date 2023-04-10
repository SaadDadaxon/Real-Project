from django.urls import path

from product.api.views import CategoryListCreate, SubImageListCreate, ProductListCreate, DescriptionListCreate, \
    DescriptionRUD, ProductRUD, CharacteristicListCreate, CharacteristicRUD

urlpatterns = [
    path('category-list-create/', CategoryListCreate.as_view()),
    path('product-list-create/', ProductListCreate.as_view()),
    path('product-rud/<int:pk>/', ProductRUD.as_view()),
    path('sub-image-list-create/', SubImageListCreate.as_view()),
    path('descriptions-list-create/', DescriptionListCreate.as_view()),
    path('descriptions-rud/<int:pk>/', DescriptionRUD.as_view()),
    path('Characteristic-list-create/', CharacteristicListCreate.as_view()),
    path('Characteristic-rud/<int:pk>/', CharacteristicRUD.as_view()),
]
