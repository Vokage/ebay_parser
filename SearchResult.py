
# Object representation of a search result
class SearchResult:
    def __init__(self, context):
        self._context = context

    def id(self):
        return self._context.get('listingid')

    def price(self):
        # TODO: Make this not so horrendous
        return self._context.find('li', {'class': 'lvprice'}).find('span', {'class': 'bold'}).text.replace('\t', '').replace('\n', '')

    def title(self):
        return self._context.find('h3', {'class': 'lvtitle'}).a.text.replace(
            "New listing", "")
