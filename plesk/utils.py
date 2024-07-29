def ensure_panel_set(method):
    def wrapper(cls, *args, **kwargs):
        if cls._panel is None:
            from plesk.PleskPanel import PleskPanel
            cls._panel = PleskPanel.get_singleton()

        return method(cls, *args, **kwargs)
    return wrapper


def generate_password():
    import random
    import string

    allowed_specials = '!@#$%^&*(),.<>/?;:[]{}-=_+'
    return ''.join(random.choices(string.ascii_letters + string.digits + allowed_specials, k=12))


def generate_guid():
    import uuid
    return str(uuid.uuid4())
