import flask

def controller(endpoint):
    """
    Turns the decorated class into a rest controller.

    This methods creates a class variable '__blueprint__' on the decorated class 
    and then adds url rules for any methods of the class that are decorated 
    with @get, @post, @put or @delete. The '__blueprint__' variable is an 
    instance of flask.Blueprint. It also creates a method 'register_routes' on 
    the decorated class for registering the blueprint on the app.

    Args:
        endpoint (str): The controller endpoint.

    Returns:
        The original class augmented with a '__blueprint__' variable and a 'register_routes' method.
    """
    def add_blueprint(cls):
        cls.__blueprint__ = flask.Blueprint( cls.__name__, cls.__module__, url_prefix = endpoint )
        cls.register_routes = lambda app: app.register_blueprint(cls.__blueprint__)
        
        methods = [getattr(cls, m) for m in dir(cls)]
        for m in methods:
            if ( hasattr(m,"__rest_metainfo__") ):
                cls.__blueprint__.add_url_rule( m.__rest_metainfo__["rule"], m.__name__, m, **m.__rest_metainfo__["options"])
        return cls
    return add_blueprint

def get(rule, **options):
    """
    Maps a GET request for a controller's method.

    This method creates a variable '__rest_metainfo__' on the decorated 
    method with meta-info about the rule and options of the request mapping.
    This info will be used by @controller decorator when building the class' blueprint.

    Args:
        rule (str): The url rule that the method handles.
        options (dict): Extra options. See flask blueprint documentation 
        for learning more.

    Returns:
        The original method augmented with a '__rest_metainfo__' variable.
    """
    def method_wrapper(f):
        f.__rest_metainfo__ = {
            "rule": rule,
            "options": {
                **options,
                **{ "methods": [ "GET" ] }
            }
        }
        return f
    return method_wrapper

def post(rule, **options):
    """
    Maps a POST request for a controller's method.

    This method creates a variable '__rest_metainfo__' on the decorated 
    method with meta-info about the rule and options of the request mapping.
    This info will be used by @controller decorator when building the class' blueprint.

    Args:
        rule (str): The url rule that the method handles.
        options (dict): Extra options. See flask blueprint documentation 
        for learning more.

    Returns:
        The original method augmented with a '__rest_metainfo__' variable.
    """
    def method_wrapper(f):
        f.__rest_metainfo__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "POST" ]}
            }
        }
        return f
    return method_wrapper


def put(rule, **options):
    """
    Maps a PUT request for a controller's method.

    This method creates a variable '__rest_metainfo__' on the decorated 
    method with meta-info about the rule and options of the request mapping.
    This info will be used by @controller decorator when building the class' blueprint.

    Args:
        rule (str): The url rule that the method handles.
        options (dict): Extra options. See flask blueprint documentation 
        for learning more.

    Returns:
        The original method augmented with a '__rest_metainfo__' variable.
    """
    def method_wrapper(f):
        f.__rest_metainfo__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "PUT" ]}
            }
        }
        return f
    return method_wrapper

def delete(rule, **options):
    """
    Maps a DELETE request for a controller's method.

    This method creates a variable '__rest_metainfo__' on the decorated 
    method with meta-info about the rule and options of the request mapping.
    This info will be used by @controller decorator when building the class' blueprint.

    Args:
        rule (str): The url rule that the method handles.
        options (dict): Extra options. See flask blueprint documentation 
        for learning more.

    Returns:
        The original method augmented with a '__rest_metainfo__' variable.
    """
    def method_wrapper(f):
        f.__rest_metainfo__ = {
            "rule": rule,
            "options": {
                **options,
                **{"methods": [ "DELETE" ]}
            }
        }
        return f
    return method_wrapper
