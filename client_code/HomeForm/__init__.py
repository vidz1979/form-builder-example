from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server

from anvil_extras import routing

@routing.route('home', title='Compras MV')  #multiple decorators allowed
@routing.route('', title='Compras MV')
class HomeForm(HomeFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.btn_fornecedor.tag.url_hash = "fornecedores"

    def nav_button_click(self, **event_args):
        url_hash = event_args["sender"].tag.url_hash
        routing.set_url_hash(url_hash, load_from_cache=False)

