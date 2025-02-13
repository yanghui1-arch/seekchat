from typing import List, Dict
from openai import OpenAI

from backend.app.core.decorators import calc_tokens
from backend.app.core.llm import DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY


def load_config():
    return {
        "model": "deepseek-v3",
        "base_url": DEEPSEEK_BASE_URL,
        "api_key": DEEPSEEK_API_KEY
    }

config = load_config()

class ChatService:

    def __init__(self):
        print(f"base_url={config['base_url']}")
        self.deepseek = OpenAI(
            base_url=config['base_url'],
            api_key=config['api_key']
        )
        print(f"deepseek:{self.deepseek}")
        self.context = 0

    @calc_tokens
    def chat(self, messages:List[Dict], model=config['model']):
        """
        chat for messages which user passes
        :param messages: messages data from user
        :return: reply information which generated from deepseek.
        """

        print(f"现在用的模型是{model}")
        completion = self.deepseek.chat.completions.create(
            model=model,
            messages=messages,
        )
        delete = False
        # thinking_process = completion.choices[0].message.reasoning_content
        reply = completion.choices[0].message.content

        if self.context > 32 * 1000 * 0.8:
            self.context = 0
            self.load_deepseek()
            delete = True

        return {
            "reply": reply,
            # "thinking_process": thinking_process
            "del": delete
        }

    def load_deepseek(self):
        self.deepseek = OpenAI(
            base_url=config['base_url'],
            api_key=config['api_key']
        )

    def repost(self, messages):
        result = self.chat(messages=messages, model="qwen-plus")
        return result


def get_chat_service():
    return ChatService()