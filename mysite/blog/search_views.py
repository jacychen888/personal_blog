from haystack.views import SearchView
from .models import *


class MySearchView(SearchView):
    def __call__(self, request):
        """
        Generates the actual response to the search.

        Relies on internal, overridable methods to construct the response.
        """
        self.request = request

        self.form = self.build_form()
        self.query = self.get_query()
        self.results = self.get_results()
        print(self.results)

        return self.create_response()
