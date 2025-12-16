from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer

class TaskList(APIView):
    """
    Obsługuje GET (lista zadań) i POST (tworzenie nowego zadania).
    Adres URL: /api/tasks/
    """
    def get(self, request):
        # Pobiera wszystkie zadania
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Tworzy nowe zadanie
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Obsługuje PATCH (aktualizacja/done) i DELETE (usuwanie) konkretnego zadania.
    Adresy URL: /api/tasks/<int:id>/ i /api/tasks/<int:id>/done/
    """
    def get_object(self, id):
        # Pomocnicza metoda do pobierania obiektu lub zwracania 404
        return get_object_or_404(Task, id=id)

    def patch(self, request, id):
        # Aktualizuje zadanie (używane dla obu ścieżek: /id/ i /id/done/)
        task = self.get_object(id)
        
        # Używamy partial=True do zezwolenia na aktualizację tylko niektórych pól (np. tylko 'done')
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # Usuwa zadanie
        task = self.get_object(id)
        task.delete()
        # Zwraca 204 No Content, co jest standardem dla udanego usunięcia
        return Response(status=status.HTTP_204_NO_CONTENT)