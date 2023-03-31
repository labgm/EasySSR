from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class UploadFileForm(forms.Form):
    name = forms.CharField(label='Project Name (*)', max_length = 100, widget=forms.TextInput(attrs={
                                    'placeholder':'Enter your project name...',
                                    'class': 'form-control',
                                 }))
    email = forms.CharField(required=False, label='E-mail', widget=forms.EmailInput(attrs={
                                    'placeholder':'Enter your e-mail...',
                                    'class': 'form-control',
                                 }))
    fileFasta = forms.FileField(label='Upload your Fasta files (*) (\'.fasta\' | \'.fna\' | \'.fa\' | \'.ffn\')',
                widget=forms.ClearableFileInput(attrs={
                'multiple': True,
                'accept': '.fasta,.fna,.fa,.ffn',
                'class': 'file-input'
                }))
    fileGBK = forms.FileField(required=False, label='Upload your GenBank Annotation files (\'.gbk\' | \'.gb\' | \'.gbff\')',
                widget=forms.ClearableFileInput(attrs={
                'multiple': True,
                'accept': '.gbk,.gbff,.gb',
                'class': 'file-input'
                }))
   #  params = forms.ChoiceField(label='', choices=[('0', 'Default'), ('1', 'Custom')],widget=forms.Select(attrs = {
   #                              'onchange' : "exibir_ocultar();",
   #                              'class': 'form-select',
   #                              'id': 'params'
   #                              }))

   #  mismatches_mono = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))
   #  mismatches_di = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))
   #  mismatches_tri = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))
   #  mismatches_tetra = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))
   #  mismatches_penta = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))
   #  mismatches_hexa = forms.CharField(label='Imp Mono', max_length=10, widget=forms.TextInput(attrs={
   #                                  'class': 'col-lg-3',
   #                                  'style': 'border-radius: 10px'
   #                               }))

   #  Size_FlankingSequences = forms.CharField(max_length = 2, widget=forms.TextInput(attrs={
   #                                                           'class': 'form-control col-lg-1',
   #                                                           'placeholder' : 'Size of Flanking'
   #                                                        }))
   #  generate_Alignment = forms.CharField(label='Do you wish to generate alignment?', widget=forms.RadioSelect(choices=[('0', 'Não'), ('1', 'Sim')], attrs = {
   #                                  'class':'form-check',
   #                              }))
   #  generate_TXT = forms.CharField(label='Do you wish to generate outputs in both formats HTML and TXT?', widget=forms.RadioSelect(choices=[('0', 'Não'), ('1', 'Sim')], attrs = {
   #                                  'class':'form-check',
   #                              }))
   #  code_Regions = forms.CharField(label='o you wish to Identify Coding/No Coding Regions?', widget=forms.RadioSelect(choices=[('0', 'Não'), ('1', 'Sim')], attrs = {
   #                                  'class':'form-check',
   #                              }))


class DownloadForm(forms.Form):
	url = forms.CharField(max_length = 255, widget=forms.TextInput({
				'class':'form-control',
				'placeholder':'Enter URL to download...',
			}))
