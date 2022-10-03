from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    ProductViewSet, CartViewSet, CartProductViewSet
)

router = DR()

router.register('product', ProductViewSet, basename='products')
router.register('cart', CartViewSet, basename='carts')
router.register('cartproduct', CartProductViewSet, basename='cartproducts')


urlpatterns = []

urlpatterns += router.urls