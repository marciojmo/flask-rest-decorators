import flask

def controller(endpoint):
    def add_blueprint(cls):
        cls.blueprint = flask.Blueprint( cls.__name__, cls.__module__, url_prefix = endpoint )
        
        methods = [getattr(cls, m) for m in dir(cls) if not m.startswith('__') ]
        for m in methods:
            if ( hasattr(m,"__rest__") ):
                cls.blueprint.add_url_rule( m.__rest__["rule"], m.__name__, m, **m.__rest__["options"])
        return cls
    return add_blueprint

def get(rule, **options):
    def method_wrapper(f):
        f.__rest__ = {
            "rule": rule,
            "options": {
                **options,
                **{ "methods": [ "GET" ] }
            }
        }
        return f
    return method_wrapper

def post(rule, **options):
    def method_wrapper(f):
        f.__rest__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "POST" ]}
            }
        }
        return f
    return method_wrapper


def put(rule, **options):
    def method_wrapper(f):
        f.__rest__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "PUT" ]}
            }
        }
        return f
    return method_wrapper

def delete(rule, **options):
    def method_wrapper(f):
        f.__rest__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "DELETE" ]}
            }
        }
        return f
    return method_wrapper
