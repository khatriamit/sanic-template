from sanic import Sanic
from sanic.response import json, html
import os
from views import DummyView


app = Sanic("my app")

# static files
app.static("/static", "static")


@app.route("/")
async def hello(request):
    return json({"hello": "world"})


# html response
@app.route("/html")
async def html_page(request):
    return html(
        """
        <html>
            <head>
                <link rel="stylesheet" href="/static/css/style.css" />
            </head>
            <body>
                <h1> Hello from html in sanic </h1> 
            </body>
        </html> 
        """
    )


# template response
@app.route("/sanic-template")
async def html_template(request):
    template = open(os.getcwd() + "/templates/index.html").read()
    return html(template)


# class based views
app.add_route(DummyView.as_view(), "/cbv-route")


# class based views with params
app.add_route(DummyView.as_view(), "/cbv-param")


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=8080,
        debug=True,
        auto_reload=True,
    )
