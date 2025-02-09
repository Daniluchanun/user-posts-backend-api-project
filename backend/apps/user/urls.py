from django.urls import path

from apps.user.views import UserListCreateView, UserRetrieveUpdateDestroyView, UserSearchByEmailView, UserSearchByIdView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update'),
    path('/search_by_id/<int:pk>', UserSearchByIdView.as_view(), name='user_search_by_id'),
    path('/search_by_email/<str:email>', UserSearchByEmailView.as_view(), name='user_search_by_email'),
]