from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from teams.models import Team
from .services import ChatGPTService


def team_ai_query(request, team_slug):
    # Get the team (no authentication required)
    team = get_object_or_404(Team, slug=team_slug)

    query = request.GET.get("query")
    if query is None or len(query) == 0:
        return JsonResponse({"error": "No query specified"}, status=500)

    chatgpt_service = ChatGPTService(team)
    response = chatgpt_service.make_request_to_chatgpt(query)
    status = 500 if "error" in response else 200

    return JsonResponse(response, status=status)
