import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..utils import form_config_prefix_key as prefix_key
from .schemas import enums, schemas

form_configs = {}

form_configs["contact"] = [
    {"key": "name", "type": "text", "label": "Name"},
    {"key": "phone", "type": "tel", "label": "Phone number", "mask": "00 00000-0000"},
    {"key": "email", "type": "email", "label": "E-mail"},
    {"key": "notes", "type": "text", "label": "Notes"},
]

form_configs["supplier"] = [
    {
        "type": "section",
        "label": "Supplier",
        "content": [
            [
                {"key": "name", "type": "text", "label": "Name"},
                {"key": "document", "type": "text", "label": "Document", "mask": "00.000.000/0000-00"},
            ],
            [
                {"key": "brands", "type": "text_list", "label": "Brands"},
                {"key": "tags", "type": "text_list", "label": "Tags"},
            ],
            [
                {
                    "key": "areas",
                    "type": "multi_select",
                    "label": "Areas",
                    "options": enums["areas"],
                    "tooltip": "Which areas this supplier operates in",
                },
                {"key": "notes", "type": "text_area", "label": "Observações"},
            ],
        ],
    },
    {
        "type": "section",
        "label": "Contacts",
        "content": [
            prefix_key(form_configs["contact"], "contact_1."),
            prefix_key(form_configs["contact"], "contact_2."),
            prefix_key(form_configs["contact"], "contact_3."),
        ],
    },
    {
        "type": "section",
        "label": "Conditions",
        "content": [
            [
                {
                    "key": "conditions.due_days",
                    "type": "text_list",
                    "label": "Prazo de pagamento",
                },
                {
                    "key": "conditions.discount",
                    "type": "number",
                    "label": "Discount",
                },
            ],
        ],
    },
    {
        "type": "section",
        "label": "Other information",
        "content": [
            [
                {
                    "key": "other_info.production_time",
                    "type": "number",
                    "label": "Production time (in days)",
                },
                {
                    "key": "other_info.delivery_time",
                    "type": "number",
                    "label": "Delivery time (in days)",
                },
            ],
            [
                {
                    "key": "other_info.uses_ean",
                    "type": "checkbox",
                    "label": "Uses EAN barcodes?",
                },
                {
                    "key": "other_info.default_margin",
                    "type": "number",
                    "label": "Default margin (%)",
                },
            ],
        ],
    },
]
