from django.contrib import admin
from django.forms.extras import widgets
from django.db.models import DateField
from elearning import models

#class SiswaAdmin(admin.ModelAdmin):
    #formfield_overrides = {DateField: {'widget': widgets.SelectDateWidget}}
    
admin.site.register(models.UserProfile)
admin.site.register(models.UserActivity)
admin.site.register(models.Alamat)
admin.site.register(models.Kabupaten)
admin.site.register(models.Kecamatan)
admin.site.register(models.TahunAjaran)
admin.site.register(models.TingkatKelas)
admin.site.register(models.Provinsi)
admin.site.register(models.LatihanSoal)
admin.site.register(models.MataPelajaran)
admin.site.register(models.MateriPelajaran)
admin.site.register(models.OrangTua)
admin.site.register(models.PilihanJawaban)
admin.site.register(models.RuangKelas)
admin.site.register(models.Sekolah)
admin.site.register(models.Guru)
admin.site.register(models.GuruMataPelajaran)
admin.site.register(models.Sesi)
admin.site.register(models.Siswa)
admin.site.register(models.Soal)



