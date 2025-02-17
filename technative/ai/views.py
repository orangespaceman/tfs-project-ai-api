from django.http import JsonResponse
from .services import ChatGPTService


def index(query, team):
    if query is None or len(query) == 0:
        return JsonResponse({"error": "No query specified"}, status=500)

    chatgpt_service = ChatGPTService(team)
    response = chatgpt_service.make_request_to_chatgpt(query)
    status = 500 if "error" in response else 200

    return JsonResponse(response, status=status)


def wolf(request):
    query = request.GET.get("query")
    return index(query, "wolf")


def dragon(request):
    query = request.GET.get("query")
    return index(query, "dragon")


def hedgehog(request):
    query = request.GET.get("query")
    return index(query, "hedgehog")


def chicken(request):
    query = request.GET.get("query")
    return index(query, "chicken")


def egg(request):
    query = request.GET.get("query")
    return index(query, "egg")
