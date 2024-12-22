from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarefaViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Adiciona o prefixo /api/
]
