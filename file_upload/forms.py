from django import forms 
from .models import FileUpload

class FileUploadForm(forms.ModelForm): 
    class Meta: 
        model = FileUpload 
        fields = ['excel_file', 'kundalik_template', 'yollanma_template','shartnoma_template']
        def clean_excel_file(self):
            excel_file = self.cleaned_data['excel_file']
            if not excel_file.name.endswith('.xlsx'):
                raise forms.ValidationError('File must be an Excel file (.xlsx)')
            return excel_file

        def clean_kundalik_template(self):
            kundalik_template = self.cleaned_data['kundalik_template']
            if not kundalik_template.name.endswith('.docx'):
                raise forms.ValidationError('File must be a Word document (.docx)')
            return kundalik_template



        def clean_yollanma_template(self):
            yollanma_template = self.cleaned_data['yollanma_template']
            if not yollanma_template.name.endswith('.docx'):
                raise forms.ValidationError('File must be a Word document (.docx)')
            return yollanma_template

        def clean_shartnoma_template(self):
            shartnoma_template = self.cleaned_data['shartnoma_template']
            if not shartnoma_template.name.endswith('.docx'):
                raise forms.ValidationError('File must be a Word document (.docx)')
            return shartnoma_template