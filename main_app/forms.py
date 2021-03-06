from django.forms import ModelForm
from .models import Maintenance, Shopping, Task


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ["date", "nutrients"]


# class NoteForm(ModelForm):
#     class Meta:
#         model = Note
#         fields = ["title", "note"]
#         widgets = {
#             "note": Textarea(attrs={"rows": 20}),
#         }
#         readonly_fields = ["updated", "timestamp"]


class ShoppingForm(ModelForm):
    class Meta:
        model = Shopping
        fields = ["item"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["task"]
