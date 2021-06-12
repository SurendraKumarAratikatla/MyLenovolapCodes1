from threading import local

_thread_locals = local()


class CurrentUserMiddleware(object):

    def process_request(self, request):
        _thread_locals.user = getattr(request, 'user', None)


def get_current_user():
    return getattr(_thread_locals, 'user', None)
