from rest_framework import serializers, viewsets
from .utils import levenshtein_distance
from .models import File
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

@csrf_exempt
@require_GET
def search_objects(request):
    search_query = request.GET.get('search', '')  # Получаем значение параметра 'search' из запроса
    files = File.objects.all()
    sorted_files = sorted(files, key=lambda x: levenshtein_distance(x.file_name, search_query))  # Сортируем результаты по расстоянию Левенштейна
    top_files = sorted_files[:5]  # Берем 5 наиболее близких файлов
    serialized_files = FileSerializer(top_files, many=True).data
    return JsonResponse(serialized_files, safe=False)