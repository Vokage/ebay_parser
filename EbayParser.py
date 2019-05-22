import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup
from SearchResult import SearchResult


class EbayParser:
    def retrieve_single_account_active_listings(account_name):
        """
        Retrieve all active listings for a specific account
        :param account_name: The account_name to parse for
        :return: list of active listings
        :throws ValueError if account name is invalid
        """

        try:
            # Find listings by account name
            url = "https://www.ebay.com/sch/" + account_name + "/m.html?_nkw=&_armrs=1&_ipg=&_from="

            # Use BeautifulSoup to parse html
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')

            # Return all the active listings for this account
            search_results = soup.findAll('li', {'class' : 'sresult'})

            # Go through each result and append to active listings list
            active_listings = []
            for listing in search_results:
                listing_id = listing.get('listingid')
                title = listing.find('h3', {'class': 'lvtitle'}).a.text.replace("New listing", "")
                price = listing.find('li', {'class': 'lvprice'}).text.strip().replace("$", "")

                # Remove the "Trending at ... " if found
                index = price.find("\n");
                if index != -1:
                    price = price[0:index]

                # Add the new Search result
                search_result = SearchResult(int(listing_id), title, float(price), account_name)
                active_listings.append(search_result)

            return active_listings
        except URLError as e:
            raise ValueError("Invalid account: " + account_name)

    def retrieve_multiple_accounts_active_listings(account_names_list):
        # TODO: this can be optimized (one request per thread)
        search_result_list = []
        for account_name in account_names_list:
            search_result_list.extend(EbayParser.retrieve_single_account_active_listings(account_name))
        return search_result_list

    def search_result_list_to_data(search_result_list):
        data = []
        for search_result in search_result_list:
            data.append(search_result.to_arr())
        return data

