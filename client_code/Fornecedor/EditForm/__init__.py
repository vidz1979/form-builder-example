from ._anvil_designer import EditFormTemplate
from anvil import *
import anvil.server
from anvil_extras import routing
from ...utils.nested_dict import NestedDict
from ..schemas import schemas
from ..form_configs import form_configs
from ...utils.form_builder import form_builder

@routing.route(
    "fornecedor", url_keys=["id", routing.ANY], title="Fornecedor | Compras MV"
)
class EditForm(EditFormTemplate):
    def __init__(self, **properties):
        self.changed = False
        self.item = {}
        if self.url_dict["id"]:
            self.item = anvil.server.call(
                "get_fornecedores",
                params={"filter": {"_id": self.url_dict["id"]}},
                one=True,
            )
            if not self.item:
                Notification(f"Fornecedor não encontrado!", style="danger")
                routing.set_url_hash(
                    "fornecedores", replace_current_url=True, load_from_cache=False
                )
                return
        self.item = NestedDict(self.item)
        self.init_components(**properties)

        # build form and store output fields in self.inputs
        self.inputs = form_builder(
            container=self.fields_panel,
            form_config=form_configs['fornecedor'],
            validate_event=self.validate_field,
            initial_data=self.item,
        )
        self.validation_errors = {}

    def before_unload(self):
        if self.changed:
            r = confirm(
                "Gostaria de salvar as mudanças?",
                buttons=[("Sim", "S"), ("Não", "N"), ("Cancelar", "C")],
            )
            if r == "C":
                # stop unload
                return True
            if r == "S":
                self.save_button_click()
            if r == "N":
                self.btn_back_click()
                
    def btn_back_click(self, **event_args):
        url = "fornecedores"
        routing.set_url_hash(url, load_from_cache=False)

    def save_button_click(self, **event_args):
        for input in self.inputs:
            self.validate_field(sender=input)

        error_count = len(self.validation_errors.keys())
        if error_count > 0:
            print(self.validation_errors)
            Notification(
                "Existem erros de validação. Corrija-os antes de gravar!",
                title="Erros de validação",
                style="warning",
            ).show()
            return

        anvil.server.call("upsert_fornecedores", data=self.item)
        self.changed = False
        self.btn_back_click()

    def validate_field(self, **event_args):
        sender = event_args["sender"]

        # handle nested schemas like in "section.title"
        key_path = sender.key.split(".")
        schema = schemas['fornecedor']
        for k in key_path:
            schema = schema.shape[k]

        # validate value against schema
        result = schema.safe_parse(sender.value)

        # set item value with cleaned data
        self.item.set_value(sender.key, result.data)

        # remember validation errors to prevent saving
        if result.error:
            self.validation_errors[sender.key] = result.error
        else:
            if sender.key in self.validation_errors:
                del self.validation_errors[sender.key]

        # display error message in field
        sender.error = result.error

        self.changed = True

