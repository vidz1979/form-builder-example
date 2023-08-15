from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from anvil_extras import routing

@routing.route('home', title='Form Builder Example')  #multiple decorators allowed
@routing.route('', title='Form Builder Example')
class HomeForm(HomeFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.btn_supplier.tag.url_hash = "suppliers"

    def nav_button_click(self, **event_args):
        url_hash = event_args["sender"].tag.url_hash
        routing.set_url_hash(url_hash, load_from_cache=False)

