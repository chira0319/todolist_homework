from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),  # 將應用程式的 URL 路由包含進來
]

