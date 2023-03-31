from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('microssatelites.urls')),
    path('admin/', admin.site.urls),
    # Celery progress
	path('celery-progress/', include('celery_progress.urls')),
]
# Corynebacterium_diphtheriae_NCTC11397.fna
#
# Corynebacterium_diphtheriae_NCTC11397.fna
# Corynebacterium_glutamicum_T613_N_1.fas
