import anvil.server
from ..utils import form_config_prefix_key as prefix_key
from .schemas import enums, schemas

form_configs = {}

form_configs["contato"] = [
    {"key": "nome", "type": "text", "label": "Nome"},
    {"key": "telefone", "type": "tel", "label": "Telefone", "mask": "00 00000-0000"},
    {"key": "email", "type": "email", "label": "E-mail"},
    {"key": "obs", "type": "text", "label": "Obs"},
]

form_configs["fornecedor"] = [
    {
        "type": "section",
        "label": "Fornecedor",
        "content": [
            {"key": "razao_social", "type": "text", "label": "Razão social"},
            [
                {"key": "cnpj", "type": "text", "label": "CNPJ", "mask": "00.000.000/0000-00"},
                {
                    "key": "codigo_tagone",
                    "type": "text",
                    "label": "Código TagOne",
                    "mask": "000000000000000",
                },
            ],
            [
                {"key": "marcas", "type": "text_list", "label": "Marcas"},
                {"key": "tags", "type": "text_list", "label": "Tags"},
            ],
            [
                {
                    "key": "divisoes",
                    "type": "multi_select",
                    "label": "Divisões",
                    "options": enums["divisoes"],
                    "tooltip": "Quais divisões de compra são atendidas por esse fornecedor",
                },
                {"key": "obs", "type": "text_area", "label": "Observações"},
            ],
        ],
    },
    {
        "type": "section",
        "label": "Contatos",
        "content": [
            prefix_key(form_configs["contato"], "contato_1."),
            prefix_key(form_configs["contato"], "contato_2."),
            prefix_key(form_configs["contato"], "contato_3."),
        ],
    },
    {
        "type": "section",
        "label": "Condições",
        "content": [
            [
                {
                    "key": "condicoes.prazo_pagto",
                    "type": "text_list",
                    "label": "Prazo de pagamento",
                },
                {
                    "key": "condicoes.desconto_com",
                    "type": "text_list",
                    "label": "Desconto comercial",
                },
                {
                    "key": "condicoes.desconto_financ",
                    "type": "number",
                    "label": "Desconto financeiro",
                },
            ],
            [
                {
                    "key": "condicoes.frete",
                    "type": "select",
                    "label": "Tipo de frete",
                    "options": enums["tipos_frete"],
                },
                {
                    "key": "condicoes.perc_frete",
                    "type": "number",
                    "label": "% frete",
                    "tooltip": "Percentual de frete para simulação de custo",
                },
            ],
            [
                {
                    "key": "condicoes.taxa_divisao",
                    "type": "number",
                    "label": "Taxa divisão",
                    "tooltip": "NF",
                },
                {
                    "key": "condicoes.obs",
                    "type": "text_area",
                    "label": "Obs. condições",
                },
            ],
        ],
    },
    {
        "type": "section",
        "label": "Outras informações",
        "content": [
            [
                {
                    "key": "outras_informacoes.perc_cred_icms",
                    "type": "number",
                    "label": "% crédito ICMS",
                },
                {
                    "key": "outras_informacoes.tempo_faturamento",
                    "type": "number",
                    "label": "Tempo p/ faturamento",
                },
                {
                    "key": "outras_informacoes.tempo_entrega",
                    "type": "number",
                    "label": "Tempo p/ entrega",
                },
            ],
            [
                {
                    "key": "outras_informacoes.eh_simples_nacional",
                    "type": "checkbox",
                    "label": "É Simples Nacional?",
                },
                {
                    "key": "outras_informacoes.eh_pronta_entrega",
                    "type": "checkbox",
                    "label": "É pronta entrega?",
                },
                {
                    "key": "outras_informacoes.fatura_por_sku",
                    "type": "checkbox",
                    "label": "Fatura por SKU?",
                },
            ],
            [
                {
                    "key": "outras_informacoes.utiliza_getin",
                    "type": "checkbox",
                    "label": "Utiliza GETIN/EAN",
                },
                {
                    "key": "outras_informacoes.etiqueta_com_referencia",
                    "type": "checkbox",
                    "label": "Etiqueta possui referência?",
                },
                {
                    "key": "outras_informacoes.envia_etiquetado",
                    "type": "checkbox",
                    "label": "Envia etiquetado",
                },
            ],
            [
                {
                    "key": "outras_informacoes.politica_desconto_titulo",
                    "type": "text",
                    "label": "Política de desconto de título",
                },
                {
                    "key": "outras_informacoes.markup_padrao",
                    "type": "number",
                    "label": "Markup padrão",
                },
            ],
        ],
    },
]
