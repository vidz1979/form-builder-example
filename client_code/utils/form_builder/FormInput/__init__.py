from ._anvil_designer import FormInputTemplate
from anvil import *
from anvil.js.window import IMask
import anvil.server
from anvil_extras.ChipsInput import ChipsInput
from anvil_extras.MultiSelectDropDown import MultiSelectDropDown

# add value properties for convenience
DatePicker.value = property(
    lambda self: self.date, lambda self, val: setattr(self, "date", val)
)
TextBox.value = property(
    lambda self: self.text, lambda self, val: setattr(self, "text", val)
)
ChipsInput.value = property(
    lambda self: self.chips, lambda self, val: setattr(self, "chips", val)
)
TextArea.value = property(
    lambda self: self.text, lambda self, val: setattr(self, "text", val)
)
MultiSelectDropDown.value = property(
    lambda self: self.selected, lambda self, val: setattr(self, "selected", val)
)
DropDown.value = property(
    lambda self: self.selected_value, lambda self, val: setattr(self, "selected_value", val)
)
CheckBox.value = property(
    lambda self: self.checked, lambda self, val: setattr(self, "checked", val)
)

class FormInput(FormInputTemplate):
    def __init__(
        self,
        error=None,
        key="",
        label="",
        type="",
        mask="",
        options="",
        tooltip="",
        **properties
    ):
        self.init_components(
            error=error,
            key=key,
            label=label,
            type=type,
            mask=mask,
            options=options,
            tooltip=tooltip,
        )
        self.label = Label(text=label, role="form-label")
        if tooltip:
            self.label.tooltip = tooltip
            self.label.icon = "fa:question-circle"
            self.label.icon_align = "right"
        self.add_component(self.label)

        if self.type == "text_list":
            self.input = ChipsInput(role="form-input")
            self.input.add_event_handler("chips_changed", self.validate)
        elif self.type == "multi_select":
            self.input = MultiSelectDropDown(
                role="form-input", items=self.options, placeholder="Selecione..."
            )
            self.input.add_event_handler("change", self.validate)
        elif self.type == "select":
            self.input = DropDown(
                role="form-input", items=self.options, placeholder="Selecione..."
            )
            self.input.add_event_handler("change", self.validate)
        elif self.type == "checkbox":
            self.input = CheckBox(role="form-input")
            self.input.add_event_handler("change", self.validate)
        # elif self.type == "radio":
        #   for option in self.options:
        #     self.input = RadioButton(role="form-input", group_name=self.key, text=self.options)
        #     self.input.add_event_handler("clicked", self.validate)
        elif self.type == "date":
            self.input = DatePicker(role="form-input", format="DD/MM/YYYY")
            self.input.add_event_handler("lost_focus", self.validate)
        elif self.type == "text_area":
            self.input = TextArea(role="form-input")
            self.input.add_event_handler("lost_focus", self.validate)
        else:
            self.input = TextBox(role="form-input")
            self.input.type = self.type
            self.input.add_event_handler("lost_focus", self.validate)

        self.add_component(self.input, expand=True)
        if self.mask:
            IMask(anvil.js.get_dom_node(self.input), {"mask": self.mask})

        self.error_label = Label(text="", role="error-label", visible=False)
        self.add_component(self.error_label)

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error
        if hasattr(self, "error_label"):
            if error:
                messages = list(map(lambda e: e.message, error.issues))
            if not error or len(messages) == 0:
                self.error_label.text = " "
                self.error_label.visible = False
            else:
                self.error_label.text = "\n".join(messages) or " "
                self.error_label.visible = True

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        self.input.value = value

    def validate(self, **event_args):
        self.raise_event("validate", key=self.key, value=self.value)
