from project.domain_layer.stores_managment.Product import Product
from project.domain_layer.stores_managment.Store import Store
from project.domain_layer.users_managment import User


class StoresManager:
    def __init__(self):
        self.stores = {int: Store}
        self.stores_idx = 0

    def search(self, search_term: str = "", categories: [str] = None, key_words: [str] = None) -> {Store: [Product]}:
        """

        Args:
            search_term: part of the wanted product name
            categories: categories to search in
            key_words:

        Returns:dist {Store:list of products in store}

        """
        search_result = {}
        for store_id in self.stores.keys():
            search_in_store = self.stores.get(store_id).search(search_term, categories, key_words)
            if search_in_store is not None:
                search_result[self.stores.get(store_id)] = search_in_store
        return search_result

    def add_product_to_store(self, store_id: int, user: User, product_name: str, product_price: int,
                             product_categories: [str],
                             key_words: [str]) -> bool:
        """

        Args:
            store_id:
            user:
            product_name:
            product_price:
            product_categories:
            key_words:

        Returns:

        """
        return self.stores.get(store_id).add_product(user, product_name, product_price, product_categories, key_words)