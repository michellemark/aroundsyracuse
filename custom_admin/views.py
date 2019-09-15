from django.contrib.sitemaps import ping_google
from django.http import HttpResponse
from django.views import View


class PingGoogleView(View):
    """Ping Google to come index the sitemap when an admin says so."""
    response = "A request has been sent to Google to crawl the updated sitemap."

    def ping_now(self):

        try:
            ping_google()
        except Exception:
            pass

    def get(self, request, *args, **kwargs):
        self.ping_now()

        return HttpResponse(self.response)

    def post(self, request, *args, **kwargs):
        self.ping_now()

        return HttpResponse(self.response)

    def dispatch(self, *args, **kwargs):

        return super(PingGoogleView, self).dispatch(*args, **kwargs)
