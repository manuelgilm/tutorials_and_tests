from typing import Optional 

def say_something(text: Optional[str] = None):
    """
    Say something to the user. If no text is provided, say 'Hello from util_package'

    :param text: The text to say
    :return: None
    """
    if text is None:
        print('Hello from util_package')
    else:
        print(text)
    