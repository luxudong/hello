# _*_ coding: utf-8 _*_
from django import forms

class DocumentForm(forms.Form):
	docfile = forms.FileField(
		label = '选择文件',
		help_text = '最大可上传 42M 大小的文件'
	)