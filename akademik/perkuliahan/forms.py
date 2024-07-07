from django import forms
from .models import Jurusan,Mahasiswa,Dosen
from django.core.exceptions import ValidationError
from django.forms import NumberInput

class Tambah_jurusan(forms.ModelForm):
    class Meta:
        model = Jurusan #model tabel jurusan
        fields = '__all__'

    def clean_kodejurusan(self):
        kojur = self.cleaned_data.get('kodejurusan')

        if Jurusan.objects.filter(kodejurusan = kojur).exists():
            raise ValidationError("Kode jurusan Sudah Ada")
        return kojur

    def clean_namajurusan(self):
        najur = self.cleaned_data.get('namajurusan')

        if Jurusan.objects.filter(namajurusan = najur).exists():
            raise ValidationError("nama jurusan sudah ada")
        return najur

class Edit_Jurusan(forms.ModelForm):
    class Meta:
        model = Jurusan #model tabel jurusan
        fields = '__all__'

class TambahMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa #model tabel jurusan
        fields = '__all__'

    def clean_nim(self):
        nimMhs = self.cleaned_data.get('nim')

        if Mahasiswa.objects.filter(nim=nimMhs).exists():
            raise ValidationError("NIM Sudah Ada")
        return nimMhs

    def clean_email(self):
        emailMhs = self.cleaned_data.get('email')

        if Mahasiswa.objects.filter(email=emailMhs).exists():
            raise ValidationError("EMAIL Sudah Ada")
        return emailMhs

class EditMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa #model tabel jurusan
        fields = '__all__'

class TambahDosen(forms.ModelForm):
    class Meta:
        model = Dosen #model tabel jurusan
        fields = '__all__'
    tgllahir = forms.DateField(label='Tanggal Lahir',widget=NumberInput(attrs={'type': 'date'}))