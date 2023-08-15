import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_client_suppliers():
    # if user_is_authorised():
    return app_tables.suppliers.client_readable()
      
@anvil.server.callable
def upsert_supplier(item, id):
    # if user_is_authorised():
    if id:
        row = app_tables.suppliers.get_by_id(id)
        if not row:
            raise Exception(f"Supplier not found! ID {id}")
        row.update(**item)
    else:
        row = app_tables.suppliers.add_row(**data)
    return row
        
      