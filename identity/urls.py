# coding=utf-8
from django.urls import path, register_converter
from identity import views

from django.urls.converters import UUIDConverter, IntConverter

app_name = 'identity'

register_converter(UUIDConverter, 'uuid')
register_converter(IntConverter, 'id')
# <to_url:to_python>

urlpatterns = [
    path('user/login/', views.Login.as_view(), name='user_login'),
    path('user/logout/', views.Logout.as_view(), name='user_logout'),
    path('user/create/', views.UserCreate.as_view(), name='user_create'),
    path('user/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/detail/', views.UserDetail.as_view(), name='user_detail'),
    path('group/', views.GroupList.as_view(), name='group_list'),
    path('group/create/', views.GroupCreate.as_view(), name='group_create'),
    path('group/detail/<id:gid>/', views.GroupDetail.as_view(),
         name='group_detail'),
    path('group/update/', views.GroupUpdate.as_view(), name='group_update'),
    path('permission/', views.PermissionList.as_view(), name='permission_list'),

    # path('users/perms/update/', views.UserPermissionUpdate.as_view(),
    #      name='user_perms_update'),
    # path('group/perms/update/', views.GroupPermissionUpdate.as_view(),
    #      name='group_perms_update'),

    path('users/password/change/', views.PasswordChange.as_view(),
         name='users_password_change')
]