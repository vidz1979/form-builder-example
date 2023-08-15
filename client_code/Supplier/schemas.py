import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil_extras import zod as z
from datetime import date, timedelta
from ..utils import to_upper

enums = {}
enums['areas'] = ["CLOTHES", "SHOES", "APPARELS"]

schemas = {}
schemas['contact'] = z.typed_dict({
    "name": z.string().optional(),
    "phone": z.string().optional(),
    "email": z.string().optional(),
    "notes": z.string().optional(),
})

schemas['supplier'] = z.typed_dict(
    {
        "_id": z.string().min(24).max(24).optional(),
        "name": (z.string().min(3, message="Mandatory information").strip().transform(to_upper)),
        "document": z.string().min(18).max(18),
            # .refine(myValidationFunction, message="Invalid document"),
        "tags": z.list(z.string()).optional(),
        "brands": z.list(z.string()).min(1, message="Fill at least one brand"),
        "areas": z.list(z.enum(enums['areas'], invalid_type_error="Invalid option")),
        "contact_1": schemas['contact'],
        "contact_2": schemas['contact'],
        "contact_3": schemas['contact'],
        "conditions": z.typed_dict({
            "due_days": z.list(
                z.coerce.integer(invalid_type_error="Must be integers")
            ).optional(),
            "discount": z.number().optional(),
        }),
        "other_info": z.typed_dict(
            {
                "production_time": z.integer(
                    invalid_type_error="Fill with an integer number"
                ).optional(),
                "delivery_time": z.integer(
                    invalid_type_error="Fill with an integer number"
                ).optional(),
                "uses_ean": z.boolean().not_required(),
                "default_margin": z.number().optional(),
            }
        ),
        "notes": z.string().optional(),
    }
)

