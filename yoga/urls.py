from django.contrib import admin
from django.urls import path
from django.urls import path
from application_form import views


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.application_form),
    path("user/",views.already_registered_user),
    path("submit/",views.thank_you),
    path("user/submit/",views.next_month_registration_thank_you),
    path("payment/",views.payment,name="payment"),
    path("user/payment/",views.payment),
    path('success/', views.success, name='success')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)