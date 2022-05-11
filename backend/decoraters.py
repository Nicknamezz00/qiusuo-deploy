from functools import wraps

SAFE_ACTIONS = ('list',)
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


def pass_safe_method(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        # Locally import to avoid circular import.
        # Be careful.
        from rest_framework.request import Request
        from rest_framework import viewsets

        request = None
        view = None
        for arg in args:
            # Argument not a class.

            if isinstance(arg, Request):
                request = arg
            if isinstance(arg, viewsets.ModelViewSet):
                view = arg
        res = func(*args, **kwargs)
        if res:
            return res
        assert request

        safe: bool = True
        # Safe methods?
        safe &= request.method in SAFE_METHODS
        # Safe actions?
        if view:
            safe &= view.action in SAFE_ACTIONS
        return safe

    return decorated

# TODO: Staff override.
