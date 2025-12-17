from django.http import JsonResponse

def greet(request):
    # Pobieramy parametr 'name' z adresu URL (np. ?name=Marek)
    name = request.GET.get("name", "Anon")
    # Zwracamy dane w formacie JSON
    return JsonResponse({"message": f"Hello, {name}!"})