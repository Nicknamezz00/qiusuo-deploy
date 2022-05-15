"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

import index

schema_view = get_schema_view(
    openapi.Info(
        title="请求文档",
        default_version='v1.0.2',
        description='',
        terms_of_service='',
        contact=openapi.Contact(email='1315098969@qq.com'),
        license=openapi.License(name='')
    ),
    public=True,
    # permission_classes=rest_framework.permissions.IsAuthenticated
)

admin.autodiscover()

urlpatterns = [
    path('', index.root),
    # --- admin-site ---
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    # --- apps ---
    path('post-manage/', include('posts.urls')),
    path('user-manage/', include('users.urls')),
    path('comment-manage/', include('comments.urls')),
    path('operation-manage/', include('operations.urls')),
    path('subject-manage/', include('subjects.urls')),
    path('favorite-manage/', include('favorite.urls')),
    path('examine/', include('examine.urls')),
    path('feedback/', include('feedback.urls')),
    path('informations/', include('informations.urls')),
    path('notification/', include('notice.urls')),
    path('scratch/', include('scratch.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# drf-yasg Swagger
urlpatterns += [
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger'),
    path('docs/', include_docs_urls(title="API说明文档"))
]

# drf jwt
urlpatterns += [
    # path('jwt-auth/', obtain_jwt_token),
]
