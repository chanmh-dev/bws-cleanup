from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('vdeed_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('index/', include('vdeed_app.urls')),
    path('view_offerings/', include('vdeed_app.urls')),
    path('view_merits/', include('vdeed_app.urls')),
    path('view_merits_detail/', include('vdeed_app.urls')),
    path('view_home/', include('vdeed_app.urls')),
    path('view_add_counter/', include('vdeed_app.urls')),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
