from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('home/', views.show_post), 
    path('detail/<int:post_id>', views.post_detail), 
    path('category/', views.categorys, name='categorys'), 
    path('post_list/<int:cat_id>/', views.post_list, name='post_list'), 
    path('saves/' , views.show_user),
    path('saves/<int:user_id>' , views.show_save_posts),
]