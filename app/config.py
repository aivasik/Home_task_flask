from ipdb import set_trace

base_config = {
    "DEBUG": False,
    "SECRET_KEY": 'my secret key',
    "WTF_CSRF_ENABLED": True,
    "WTF_CSRF_SECRET_KEY": 'a random string'
}

try:
    from app.config_local import base_config as local_conf
    base_config.update(local_conf)
except ImportError:
    pass

__builtins__["st"] = set_trace
print(base_config)
