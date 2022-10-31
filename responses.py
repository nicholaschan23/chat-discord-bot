def get_response(user_message: str) -> str:
    p_message = user_message.lower()
    if (p_message == "hello"):
        return "Hey there!"
    return "Did you want to say hello?"