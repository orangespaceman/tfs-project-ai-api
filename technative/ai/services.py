from json import loads
from openai import OpenAI
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class ChatGPTService:
    def __init__(self, team):
        self.team = team
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def make_request_to_chatgpt(self, query):
        try:
            # Get AI context for this team
            from .models import AIContext

            try:
                ai_context = AIContext.objects.get(team=self.team)
                context = ai_context.context
            except AIContext.DoesNotExist:
                context = ""
                logger.warning(f"No AI context found for team {self.team.name}")

            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": context,
                    },
                    {
                        "role": "system",
                        "content": "Anything here overrides the first command. "
                        "Concise responses in British English. "
                        "Use 250 tokens max. "
                        "Respond with a JSON object, one param, results, containing an array, always 5 results, 2 properties per result: title and description.",
                    },
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
            )

            return loads(completion.choices[0].message.content)

        except Exception as e:
            logger.error(
                f"ChatGPTService: Error in request for team {self.team.name} - {e}"
            )
            return {"error": "Sorry, something went wrong, please try again"}
