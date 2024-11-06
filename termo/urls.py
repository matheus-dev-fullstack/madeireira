from django.urls import path
from termo import views

urlpatterns = [
    path('', views.list_terms, name='termos'),
    path('termo/<int:id>/', views.get_term, name='get-term'),
    path('search/', views.search_term, name='search_term'),
    path('users/', views.list_users, name='list-users'), 
    path('print_pdf/<int:id>/pdf/', views.render_pdf_view, name='print_pdf'),
    path('termo/<int:pk>/editar/', views.TermoUpdateView.as_view(), name='termo-edit'),
    path('termo/<int:pk>/editar/', views.TermoUpdateView.as_view(), name='termo-edit'),

]