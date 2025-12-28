from config.settings import Settings
import openai

import os


setting = Settings()


class Engine:
    def __init__(self):
        pass

    def groq_openai_response(
        self, prompt: str, model: str = "openai/gpt-oss-20b"
    ) -> str:

        # Initialize client
        client = openai.OpenAI(
            api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
        )

        # Call the model
        response = client.responses.create(model=model, input=prompt)

        return response.output_text
