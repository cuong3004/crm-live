from django.urls import path
from .views import list_class, image_class, image_puture_class

urlpatterns = [
    path('', list_class, name="class"),
    # id member for class
    path('<int:list_id>', image_class, name="image"),
    path('puture', image_puture_class, name="puture"),
    path('classroom', image_puture_class, name="classroom"),
]
