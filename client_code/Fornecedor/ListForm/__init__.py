from ._anvil_designer import ListFormTemplate
from anvil import *
import anvil.server
from anvil_extras import routing

@routing.route('fornecedores', title="Fornecedores | Compras MV")
class ListForm(ListFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def get_items(self):
        self.data = anvil.server.call(
            "get_fornecedores",
            {
                "projection": {
                    "_id": 1,
                    "razao_social": 1,
                    "cnpj": 1,
                    "marcas": 1,
                    "codigo_tagone": 1,
                },
            },
        )

        def transformer(fornecedor):
            fornecedor["marcas"] = ", ".join(fornecedor["marcas"])
            if "codigo_tagone" in fornecedor:
                fornecedor[
                    "link_tagone"
                ] = "https://modaverao.tagone.com.br/#/pessoa/" + str(
                    fornecedor["codigo_tagone"]
                ).zfill(
                    15
                )
            return fornecedor

        return list(map(transformer, self.data))

    def form_show(self, **event_args):
        self.repeating_panel_1.items = self.get_items()

    def btn_add_fornecedor_click(self, **event_args):
        routing.set_url_hash("fornecedor?id=", load_from_cache=False)
        routing.remove_from_cache("fornecedor?id=")
