from django.db import models

class FileUpload(models.Model): 
    excel_file = models.FileField(upload_to='excel/') 
    shartnoma_template = models.FileField(upload_to='templates/',null=True, blank=True) 
    yollanma_template = models.FileField(upload_to='templates/',null=True, blank=True) 
    kundalik_template = models.FileField(upload_to='templates/',null=True, blank=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload {self.id} - {self.excel_file.name}"