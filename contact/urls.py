from django.urls import path
from .views import ContactList, ContactDetail

urlpatterns = [
    path("", ContactList.as_view(), name="contact-list"),
    path("<int:pk>/", ContactDetail.as_view(), name="contact-detail"),
]
