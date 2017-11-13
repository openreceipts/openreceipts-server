from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, HTML
from django import forms

from .models import ReceiptScan
from s3direct.widgets import S3DirectWidget
    

class ReceiptScanForm(forms.ModelForm):
    cropped_image = forms.CharField(max_length=999999999999999999, required=False)
    #cropped_image = forms.URLField(widget=S3DirectWidget(dest='example_destination'))
    class Meta:
        model = ReceiptScan
        fields = ('image', 'cropped_image',)

        widgets = {
            'cropped_image': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(ReceiptScanForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': "image/*"})

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Scan your receipt",
                Div(css_id='views'),
                'image',
                'cropped_image'
            ),
            HTML(
                """
                <div class="row">
                    <div class="col-xs-12" id="image-edit-buttons">
                        <button id="rotatebuttonLeft" type="button" class="btn btn-danger btn-sm"><i class="fa fa-undo" aria-hidden="true"></i> Rotate left
                        </button>
                        <button id="rotatebuttonRight" type="button" class="btn btn-danger btn-sm"><i class="fa fa-repeat" aria-hidden="true"></i> Rotate right
                        </button>
                        <button id="cropbutton" type="button" class="btn btn-danger btn-sm"><i class="fa fa-crop" aria-hidden="true"></i>
                            Crop
                        </button>
                    </div>
                </div>
                """
            ),
            FormActions(
                Submit('save', "Send", css_class='pull-right'),
            )
        )

        self.helper.form_id = "image_upload_form"
