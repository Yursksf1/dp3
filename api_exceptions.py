class BaseError(ValueError):
    pass


class ApiException(Exception):
    """Class for lendingfront api exceptions."""

    def __init__(self, user_friendly_message, status_code=500):
        self._user_friendly_message = user_friendly_message
        self._status_code = status_code

    def __str__(self):
        return repr(self._user_friendly_message)

    @property
    def user_friendly_message(self):
        """The _user_friendly_message property - the getter"""
        return self._user_friendly_message

    @property
    def status_code(self):
        """Status code from exception"""
        return self._status_code


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
