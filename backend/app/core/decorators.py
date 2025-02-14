from functools import wraps


def calc_tokens(func):
    """
    calculate tokens consuming..
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
