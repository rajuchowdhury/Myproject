from django.conf.urls import url
from . import views
from django.urls import path

# from django.urls import include
# from django.views.generic import RedirectView
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('catalog/', include('catalog.urls')),
#     path('/', RedirectView.as_view(url='/catalog/', permanent=True)),
# ] + + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]