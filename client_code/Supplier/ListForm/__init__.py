from ._anvil_designer import ListFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import routing

@routing.route('suppliers', title="Suppliers")
class ListForm(ListFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def form_show(self, **event_args):
        self.repeating_panel_1.items = anvil.server.call('get_suppliers').search()

    def btn_add_supplier_click(self, **event_args):
        routing.set_url_hash("supplier?id=", load_from_cache=False)
        routing.remove_from_cache("supplier?id=")

