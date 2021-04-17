# Flask REST Decorators


Flask REST Decorators makes easy to define controllers for routing purposes on flask applications.

# Installing

Install and update using [`pip`](https://pip.pypa.io/en/stable/quickstart/):

```shell
$ pip install -U flask-rest-decorators
```
or
```shell
pip install -U git+git://github.com/marciojmo/flask-rest-decorators.git
```

# A Full Example

The following example shows how to use flask-rest-decorators on your controller classes:

```python
# controllers.py module

from flask_rest_decorators import controller, get, post, put, delete

@controller("/api/v1/hello")
class HelloWorld:
    @get("/")
    def index():
        return "Hello, world!"

    @post("/")
    def post():
        return "Nice post!"

    @get("/<string:id>")
    def get_by_id(id):
        return f"Getting {id}!"

    @put("/<string:id>")
    def update_by_id(id):
        return f"Updating {id}!"

    @delete("/<string:id>")
    def delete_by_id(id):
        return f"Deleting {id}!"

```

Behind the scenes, each method decorator `(@get, @post, @put, @delete)` will store metadata into a variable named `__rest_metainfo__` within the method itself and the `@controller` decorator will create a class variable `HelloWorld.__blueprint__` contaning all the routing information defined by these methods. 

The controller decorator also adds the utility method `register_routes` to the class. This method takes a flask app instance as argument and registers the controller routes on the flask application.

You may now register the controller routes on your app as follows:

```python
# app.py module

import flask
import controllers

app = flask.Flask(__name__)

# Registering controller routes
controllers.HelloWorld.register_routes(app)

if __name__ == "__main__":
    app.run(host="localhost",port=5000)

```

That is the same as the following (you can do both ways):
```python
app.register_blueprint(controllers.HelloWorld.__blueprint__)
```

# Advantages

- Simple way of defining and handling routes.
- Freedom over your endpoint definitions.
- Relies on flask blueprints behind scenes. 

# Future work
- Make the decorators work for controller instances instead of a static class and class methods in order to take advantage of inheritance.
- Add tests.

# Links

-   Source Code: https://github.com/marciojmo/flask-rest-decorators/
-   Issue Tracker: https://github.com/marciojmo/flask-rest-decorators/issues
