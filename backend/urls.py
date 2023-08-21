from django.urls import path
from backend import views

urlpatterns = [
    path('mushrooms/', views.mushrooms_list),
    path('mushrooms/<int:pk>', views.mushroom_detail),
]