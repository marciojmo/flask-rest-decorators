# Flask REST Decorators


Flask REST Decorators makes easy to define controllers for routing purposes on flask applications. It automatically creates a blueprint for the annotated classes and methods given.

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

The following example shows how to use flask-rest-decorators on your controller class:

```python
# controllers.py

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

This will create a class variable `HelloWorld.blueprint` contaning all the routing information defined. You should also register the blueprint to your flask app as follows:

```python
# app.py

import flask
import controllers

app = flask.Flask(__name__)
app.register_blueprint(controllers.HelloWorld.blueprint)

if __name__ == "__main__":
    app.run(host="localhost",port=5000)

```

# Advantages

- Simple way of defining routes.
- Inheritance. You may have a BaseController that handles a certain routing and use the same method on derived classes under another url_prefix.
- Define all controllers in a single module instead of having a folder with multiple files.
- Don't worry about clashing method names since they are bounded by the controller class.
- Flexible and simple alternative to flask-restful (freedom over your endpoint definitions, single classed).
- Relies on flask blueprints behind scenes. 

```python
# controllers.py

from flask_rest_decorators import controller, get, post, put, delete

class BaseController:
    meta = {
        "abstract": True
    }

    @get("/<string:id>")
    def get_by_id(id):
        return f"Getting {id}!"

        

@controller("/api/v1/hello")
class HelloWorld(BaseController):
    pass

# Hello world inherits get_by_id method and handles the '/<string:id>' route under the '/api/v1/hello' endpoint.
```

Links
-----

-   Source Code: https://github.com/marciojmo/flask-rest-decorators/
-   Issue Tracker: https://github.com/marciojmo/flask-rest-decorators/issues
