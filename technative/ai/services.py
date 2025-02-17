from json import loads
from openai import OpenAI
from django.conf import settings
import logging

from .models import (
    WolfAIContext,
    DragonAIContext,
    HedgehogAIContext,
    ChickenAIContext,
    EggAIContext,
)

logger = logging.getLogger(__name__)


class ChatGPTService:
    def __init__(self, team):
        if team == "wolf":
            key = settings.OPENAI_API_KEY_WOLF
            self.model = WolfAIContext
        elif team == "dragon":
            key = settings.OPENAI_API_KEY_DRAGON
            self.model = DragonAIContext
        elif team == "hedgehog":
            key = settings.OPENAI_API_KEY_HEDGEHOG
            self.model = HedgehogAIContext
        elif team == "chicken":
            key = settings.OPENAI_API_KEY_CHICKEN
            self.model = ChickenAIContext
        elif team == "egg":
            key = settings.OPENAI_API_KEY_EGG
            self.model = EggAIContext
        else:
            key = None

        if key is None:
            self.client = None
            logger.info("ChatGPTService: Not connected")
        else:
            self.client = OpenAI(
                api_key=key,
            )

    def make_request_to_chatgpt(self, query):
        try:
            context = self.model.objects.first().context
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

        # capture errors
        except Exception as e:
            logger.error("ChatGPTService: Error in request - {}".format(e))
            logger.warning(e)

            return {"error": "Sorry, something went wrong, please try again"}
