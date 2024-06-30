from django.urls import path
from . import views
from .views import SignUpView
from .views import ExpenseCreateView,ExpenseDeleteView,ExpenseListView,ExpenseUpdateView
app_name = 'expenses'

urlpatterns = [
    #path('register/',views.register,name='register'),
    #path('login/',views.login_view,name='login'),
    path('logout/',views.logout,name='logout'),
   # path("work/",views.work),
    path('loginJav/',views.Login,name='trial'),
    path('signup/',SignUpView.as_view(),name="signup"),
    path('add/',ExpenseCreateView.as_view(),name='add'),
    path('list/',ExpenseListView.as_view(),name='list'),
    path('edit/<int:pk>/',ExpenseUpdateView.as_view(),name='edit_expense'),
    path('delete/<int:pk>/',ExpenseDeleteView.as_view(),name='delete_expense')

    #path('<int:pk>/edit/',edit_expense,name='edit_expense'),
    #path('<int:pk>/delete/',delete_expense,name='delete_expense')
    
    


]

