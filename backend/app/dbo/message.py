import datetime
import json
from typing import List
from uuid import uuid4

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.core.mysql import get_db
from backend.app.models.models import Message


class MessageDBO:

    def __init__(self, db:Session):
        self.db = db

    def add_message(self, message):
        """
        add a piece of message
        :param message: message from user
        :return:
        """
        message = json.dumps(message, ensure_ascii=False)
        to_add_message = Message(
            message=message,
            message_time=datetime.datetime.now()
        )
        self.db.add(to_add_message)
        self.db.commit()
        self.db.refresh(to_add_message)
        return to_add_message

    def access_message(self) -> List:
        messages = self.db.query(Message.message).all()
        print(messages)
        if len(messages) == 0:
            return messages
        else:
            new_messages = []
            for message in messages:
                new_messages.append(json.loads(message[0]))
            return new_messages

    def del_messages(self):
        """
        del some messages
        :return:
        """
        total_messages = self.db.query(Message.message).count()
        half_count = total_messages // 2
        messages_to_delete = self.db.query(Message).order_by(Message.id).limit(half_count).all()
        for message in messages_to_delete:
            self.db.delete(message)
        self.db.commit()
        return len(messages_to_delete)

def get_message_dbo(
        db:Session=Depends(get_db)
):
    return MessageDBO(db=db)