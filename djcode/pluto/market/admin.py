from django.contrib import admin
from .models import Quote,Document
# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
	list_display = ('name','opening','code')
						
admin.site.register(Quote,QuoteAdmin)
admin.site.register(Document)