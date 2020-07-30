from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import recipes.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", recipes.views.home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("recipes/", include("recipes.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)