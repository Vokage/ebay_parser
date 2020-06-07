import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup
from SearchResult import SearchResult


class Account:
    def __init__(self, account_name):
        self._account_name = account_name

    def retrieve_active_listings(self):
        # Make a request to the active listings page
        # TODO: Handle multiple pages (Probably visiting all pages, slow ...)
        url = self.active_listings_url(self._account_name)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        # Get all the search results listing on the page
        search_results_context = soup.findAll('li', {'class': 'sresult'})
        active_listings = []

        # Pass each li context to construct a search result object representation
        for listing_context in search_results_context:
            search_result = SearchResult(listing_context)
            active_listings.append(search_result)
        return active_listings

    def active_listings_url(self, account_name):
        return "https://www.ebay.com/sch/" + account_name + \
            "/m.html?_nkw=&_armrs=1&_ipg=&_from="
