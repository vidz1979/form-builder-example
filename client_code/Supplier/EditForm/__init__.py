from ._anvil_designer import EditFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import routing
from ...utils.nested_dict import NestedDict
from ..schemas import schemas
from ..form_configs import form_configs
from ...utils.form_builder import form_builder

@routing.route(
    "supplier", url_keys=["id", routing.ANY], title="Supplier"
)
class EditForm(EditFormTemplate):
    def __init__(self, **properties):
        self.changed = False
        if self.url_dict["id"]:
            self.item = app_tables.suppliers.get_by_id(self.url_dict["id"])
            if not self.item:
                Notification(f"Supplier not found!", style="danger")
                routing.set_url_hash(
                    "suppliers", replace_current_url=True, load_from_cache=False
                )
                return
        else: 
            self.item = app_tables.suppliers.add_row(name="", document="")
        self.init_components(**properties)

        # build form and store output fields in self.inputs
        self.inputs = form_builder(
            container=self.fields_panel,
            form_config=form_configs['supplier'],
            validate_event=self.validate_field,
            initial_data=self.item,
        )
        self.validation_errors = {}

    def before_unload(self):
        if self.changed:
            r = confirm(
                "Would you like to save changes?",
                buttons=[("Yes", "Y"), ("No", "N"), ("Cancel", "C")],
            )
            if r == "C":
                # stop unload
                return True
            if r == "Y":
                self.save_button_click()
            if r == "N":
                self.btn_back_click()
                
    def btn_back_click(self, **event_args):
        url = "suppliers"
        routing.set_url_hash(url, load_from_cache=False)

    def save_button_click(self, **event_args):
        for input in self.inputs:
            self.validate_field(sender=input)

        error_count = len(self.validation_errors.keys())
        if error_count > 0:
            print(self.validation_errors)
            Notification(
                "There are validation errors. Please correct it before saving.",
                title="Validation errors",
                style="warning",
            ).show()
            return

        if self.url_dict["id"]:
            pass
            # app_tables.suppliers.client_writable(data=)
        anvil.server.call("upsert_supplieres", data=self.item)
        self.changed = False
        self.btn_back_click()

    def validate_field(self, **event_args):
        sender = event_args["sender"]

        # handle nested schemas like in "section.title"
        key_path = sender.key.split(".")
        schema = schemas['supplier']
        for k in key_path:
            schema = schema.shape[k]

        # validate value against schema
        result = schema.safe_parse(sender.value)

        # set item value with cleaned data
        self.item[sender.key] = result.data

        # remember validation errors to prevent saving
        if result.error:
            self.validation_errors[sender.key] = result.error
        else:
            if sender.key in self.validation_errors:
                del self.validation_errors[sender.key]

        # display error message in field
        sender.error = result.error

        self.changed = True

