from ._anvil_designer import ErrorFormTemplate
from anvil import *
import anvil.server
from anvil_extras import routing

@routing.error_form
class ErrorForm(ErrorFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
