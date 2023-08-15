from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
from anvil_extras import routing

class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def title_link_click(self, **event_args):
        url = f"fornecedor?id={self.item['_id']}"
        routing.set_url_hash(url, load_from_cache=False)
    


