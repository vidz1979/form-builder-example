from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..nested_dict import NestedDict
from .FormInput import FormInput

def form_builder(container, form_config, validate_event, initial_data = {}):
    output_fields = []
    initial_data = NestedDict(initial_data)
    for entry in form_config:
        if type(entry) == dict:
            if entry["type"] == "section":
                section_card = ColumnPanel(role="outlined-card")
                section_card.add_component(Label(text=entry["label"], role="title"))
                output_fields += form_builder(
                    container=section_card, 
                    form_config=entry["content"],
                    validate_event=validate_event,
                    initial_data=initial_data,
                )
                container.add_component(section_card)
            else:
                input = FormInput(**entry)
                input.add_event_handler("validate", validate_event)
                input.value = initial_data.get_value(entry['key'])
                output_fields.append(input)
                container.add_component(input, expand=True)
        elif type(entry) == list:            
            row_container = FlowPanel()
            output_fields += form_builder(
                container=row_container, 
                form_config=entry,
                validate_event=validate_event,
                initial_data=initial_data,
            )
            container.add_component(row_container)
        else:
            raise Exception(f"Invalid form config entry: {entry}")
    return output_fields
