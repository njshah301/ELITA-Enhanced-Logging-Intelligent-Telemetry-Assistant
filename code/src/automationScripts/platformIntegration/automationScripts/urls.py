from django.urls import path
from .views import UpdateGitHubView, ProcessDataView,createFileView

urlpatterns = [
    path('update-github/', UpdateGitHubView.as_view(), name='update_github'),
    path('process-data/', ProcessDataView.as_view(), name='process_data'),
    path('create-file/', createFileView.as_view(), name='create_file'),
]
