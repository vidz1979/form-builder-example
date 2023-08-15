import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_suppliers():
    # if user_is_authorised():
    return app_tables.suppliers.client_writable()
      
