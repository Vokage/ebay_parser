# Object representation of a search result
class SearchResult(object):
    def __init__(self, listing_id, title, price, account_name):
        """
        :param listing_id: The listing's id
        :param title: The listing's title
        :param price: The listing's price
        """
        self.listing_id = listing_id
        self.title = title
        self.price = price
        self.account_name = account_name

    def to_arr(self):
        return [self.account_name, self.listing_id, self.title, self.price]

    def __str__(self):
        """
        String representation of object
        :return: string representation of object
        """
        return self.account_name + ' ' + self.listing_id + ' ' + self.title + ' ' + self.price
