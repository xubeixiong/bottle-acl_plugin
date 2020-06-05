from abc import abstractmethod, ABCMeta
from bottle import redirect, abort, request


class AclPlugin(metaclass=ABCMeta):
    name = 'acl'
    api = 2

    @abstractmethod
    def get_roles(self, arg):
        pass

    def setup(self, app):
        pass

    def apply(self, callback, route):

        def wrapper(*args, **kwargs):
            result = callback(*args, **kwargs)
            return result

        return wrapper

    def check(self, roles):
        client_roles = set(request.environ["user_roles"])
        filter_roles = set(roles)
        if len(client_roles) < len(filter_roles):
            return False
        set_diff = (client_roles | filter_roles) ^ client_roles
        return len(set_diff) == 0

    def roles_required(self, roles=None, url=None):
        if roles is None:
            roles = {"user"}

        def decorator(callback):

            def wrapper(*args, **kwargs):
                request.environ["user_roles"] = set(self.get_roles(request))
                if request.environ["user_roles"]:
                    if not self.check(roles):
                        return abort(403, "Insufficient authority.")

                    else:
                        return callback(*args, **kwargs)

                if url:
                    return redirect(url)

                return abort(403, "Insufficient authority.")

            return wrapper

        return decorator

