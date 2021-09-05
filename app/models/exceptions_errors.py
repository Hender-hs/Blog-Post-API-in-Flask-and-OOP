class KeyMissingError(Exception) :

    def __init__(self, message) -> None:

        self.message = f'your missing these keys: {message}'



class ValueTypeError(Exception) :

    def __init__(self, message) -> None:

        self.message = f'Only string type. These props has a different type: {set(message)}'


class InvalidKeysError(Exception) :

    def __init__(self, message) -> None:

        self.message = f'these keys are not allowed: {message}'
