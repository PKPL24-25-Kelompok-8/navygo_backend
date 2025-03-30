from rest_framework.request import Request
import jwt

public_key = "hello there this is a mock public key"


def requires_auth(wrapped):
    """
    This decorator is used to protect view functions that require authorization.

    It works on both class based views and function based views.

    Use it as follows:

    ```python
    @requires_auth
    def view_function(self, request):
        pass
    ```
    """

    def wrapper(self, *args, **kwargs):

        if len(args) < 2:
            request: Request = args[0]
        else:
            request: Request = args[1]

        jwt_access = request._request.COOKIES["jwt_access"]

        decoded = jwt.decode(jwt_access, public_key, algorithms=["ES256"])

        wrapped(self, *args, **kwargs)

    return wrapper
