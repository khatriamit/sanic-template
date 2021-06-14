from sanic.views import HTTPMethodView, CompositionView
from sanic import response


class DummyView(HTTPMethodView):
    def get(self, request, param, *args, **kwargs):
        return response.text(
            f"I am get method {param}",
        )

    def put(self, request, *args, **kwargs):
        return response.text("I am put method")
