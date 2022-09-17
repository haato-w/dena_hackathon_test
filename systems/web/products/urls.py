from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductDummyApiView, product_list

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)), # includeはrouter要素を指す時に使いそう

    # 追加
    path("dummy/", ProductDummyApiView.as_view()),

    # 追加
    path('list/', product_list),
]
