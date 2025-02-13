from functools import wraps


def calc_tokens(func):
    """
    估算此次调用产生的token数，messages必须是经过app/api/utils/handle_text.py中的format_message_from_user_to_chat方法处理过的
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(self, messages, *args, **kwargs):
        for message in messages:
            self.context += len(message)

        output = func(self, messages, *args, **kwargs)
        self.context += len(output['reply'])
        return output
    return wrapper