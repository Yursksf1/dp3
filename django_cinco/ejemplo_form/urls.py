from django.urls import path

# importing views from views..py
from ejemplo_form import views
from django.views.generic import TemplateView

app_name = "app"
urlpatterns = [

    path('api/create', views.create_table_uno, name='create_table_uno'),


    path(
        route='ejemplo2/new/',
        view=views.CreateTabla_dosView.as_view(),
        name='create'
    ),


    path(
        route='ejemplo1/new/',
        view=views.CreateTabla_unoView.as_view(),
        name='create-uno'
    ),

    path(
        route='ejemplo2/<int:pk>/',
        view=views.Tabla_dosView.as_view(),
        name='detail'
    )
]
