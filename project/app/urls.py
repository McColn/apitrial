from .views import StudentDetail,SMSListView
from rest_framework import routers
from django.urls import path,include
from . import views

# router = routers.DefaultRouter()
# router.register(r'api/students', StudentViewSet,'students')

# urlpatterns = router.urls


# router = routers.DefaultRouter()
# router.register(r'students', StudentViewSet)

urlpatterns = [
    # path('', views.home,name='home'),
    # path('api/getdata/', views.get_data, name='get-data'),
    # path('api/adddata/', views.add_data, name='add-data'),
    # path('api/', include(router.urls)),
    path('api/', StudentDetail.as_view(), name='api'),
    path('sms/', SMSListView.as_view(), name='sms-list'),
    path('api/received-sms/', views.received_sms, name='received_sms'),

    
    ]