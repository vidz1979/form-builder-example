from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import routing
from anvil_extras import routing

from ..HomeForm import HomeForm
from ..ErrorForm import ErrorForm
from ..Supplier.ListForm import ListForm as SupplierListForm
from ..Supplier.EditForm import EditForm as SupplierEditForm

@routing.main_router
class MainForm(MainFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.links = [self.link_fornecedores]
        self.link_home.tag.url_hash = "home"
        self.link_fornecedores.tag.url_hash = "fornecedores"

    def nav_link_click(self, **event_args):
        url_hash = event_args["sender"].tag.url_hash
        routing.set_url_hash(url_hash, load_from_cache=False)

    def btn_refresh_click(self, **event_args):
        routing.reload_page()

routing.logger.debug = True  # Toggle this setting for logging print statements
routing.clear_cache()
routing.launch()
