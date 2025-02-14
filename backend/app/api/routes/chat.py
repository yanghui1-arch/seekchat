import json

from fastapi import APIRouter, Depends, Body
from pydantic import Field

from backend.app.dbo.message import get_message_dbo, MessageDBO
from backend.app.schemas.chat import Chat
from backend.app.service.chat import ChatService, get_chat_service

chat_router = APIRouter()

@chat_router.post("/chat")
def chat(
    request:Chat,
    chat_service:ChatService=Depends(get_chat_service),
    message_dbo:MessageDBO=Depends(get_message_dbo)
):
    content = request.content
    print(content)
    if len(content) > 300:
        return "不要发这么长的文本，这个是免费的做着玩儿的，不要让我承担这么大的成本qwq55555..."

    messages = message_dbo.access_message()
    message = {
        "role": "user",
        "content": content
    }
    messages.append(message)
    message_dbo.add_message(message)
    try:
        result = chat_service.chat(messages=messages)
        print(f"result={result}")
        message_dbo.add_message(
            {
                "role": "assistant",
                "content": result['reply']
            }
        )

        if result['del']:
            message_dbo.del_messages()

        return result['reply']

    except TimeoutError as e:
        result = chat_service.repost(messages=messages)
        message_dbo.add_message(
            {
                "role": "assistant",
                "content": result['reply']
            }
        )

        if result['del']:
            message_dbo.del_messages()

        return result['reply']
    except Exception as e:
        print(e)
        return "出错了，请加群反馈！或者在github上反馈！"
