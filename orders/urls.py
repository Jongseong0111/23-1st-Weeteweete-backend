from django.urls  import path
from .views       import OrderView

urlpatterns = [
    path('/item/<int:item_id>', OrderView.as_view()),
    path('', OrderView.as_view()),
]