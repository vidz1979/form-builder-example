from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import routing

class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def title_link_click(self, **event_args):
        url = f"supplier?id={self.item.get_id()}"
        routing.set_url_hash(url, load_from_cache=False, item=self.item)
    


