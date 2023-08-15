import anvil.server
from anvil_extras import zod as z
from datetime import date, timedelta
from ..utils import validateCnpj, to_upper

enums = {}
enums['divisoes'] = ["MASC", "FEM", "INF", "CMB", "ORP", "BAGAGEM", "ESPORT"]
enums['tipos_frete'] = ["", "CIF", "FOB", "Dividido"]

schemas = {}
schemas['contato'] = z.typed_dict({
    "nome": z.string().optional(),
    "telefone": z.string().optional(),
    "email": z.string().optional(),
    "obs": z.string().optional(),
})
schemas['fornecedor'] = z.typed_dict(
    {
        "_id": z.string().min(24).max(24).optional(),
        "razao_social": (z.string()
                         .min(3, message="Razão social é obrigatória")
                        .strip()
                        .transform(to_upper)),
                        # .refine(lambda s: s != "Admin", message="You can't be an admin"),
        "cnpj": z.string().refine(validateCnpj, message="CNPJ inválido"),
        "codigo_tagone": z.string().optional(),
        "tags": z.list(z.string()).optional(),
        "marcas": z.list(z.string()).min(1, message="É necessário ao menos uma marca"),
        "divisoes": z.list(z.enum(enums['divisoes'], invalid_type_error="Opção inválida")),
        "contato_1": schemas['contato'],
        "contato_2": schemas['contato'],
        "contato_3": schemas['contato'],
        "condicoes": z.typed_dict({
            "prazo_pagto": z.list(
                z.coerce.integer(invalid_type_error="Prazos devem ser dias")
            ).optional(),
            "desconto_com": z.list(
                z.coerce.integer(invalid_type_error="Descontos devem ser números")
            ).optional(),
            "desconto_financ": z.number().optional(),
            "frete": z.enum(
                enums['tipos_frete'], invalid_type_error="Opção inválida"
            ).optional(),
            "perc_frete": z.number().optional(),
            "taxa_divisao": z.number().optional(),
            "obs": z.string().optional(),
        }),
        "outras_informacoes": z.typed_dict(
            {
                "eh_simples_nacional": z.boolean().not_required(),
                "perc_cred_icms": z.number().optional(),
                "tempo_faturamento": z.integer(
                    invalid_type_error="Informe um número inteiro"
                ).optional(),
                "tempo_entrega": z.integer(
                    invalid_type_error="Informe um número inteiro"
                ).optional(),
                "eh_pronta_entrega": z.boolean().not_required(),
                "fatura_por_sku": z.boolean().not_required(),
                "utiliza_getin": z.boolean().not_required(),
                "etiqueta_com_referencia": z.boolean().not_required(),
                "envia_etiquetado": z.boolean().not_required(),
                "politica_desconto_titulo": z.string().optional(),
                "markup_padrao": z.number().optional(),
            }
        ),
        "politica_defeito": z.typed_dict(
            {
                "prazo": z.string().optional(),
                "tipo": z.string().optional(),
                "forma_ressarcimento": z.string().optional(),
                "responsavel": z.string().optional(),
                "obs": z.string().optional(),
            }
        ),
        "obs": z.string().optional(),
    }
)

