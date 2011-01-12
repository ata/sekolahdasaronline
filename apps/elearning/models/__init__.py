from django.db import models
from django.contrib.auth.models import User

class Provinsi(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Provinsi'
    
    def __unicode__(self):
        return self.nama

class Kabupaten(models.Model):
    nama = models.CharField(max_length=255)
    provinsi = models.ForeignKey(Provinsi)
    
    class Meta:
        verbose_name_plural = 'Daftar Kota/Kabupaten'
        verbose_name= 'Kota/Kabupaten'
    
    def __unicode__(self):
        return self.nama
    
class Kecamatan(models.Model):
    nama = models.CharField(max_length=255)
    kabupaten = models.ForeignKey(Kabupaten)
    
    class Meta:
        verbose_name_plural = 'Daftar Kecamatan'
    
    def __unicode__(self):
        return self.nama

class Alamat(models.Model):
    nama = models.CharField(max_length=255, blank=True)
    provinsi = models.ForeignKey(Provinsi)
    kabupaten = models.ForeignKey(Kabupaten)
    kecamatan = models.ForeignKey(Kecamatan)
    alamat = models.CharField(max_length=255) 
    kodepos = models.CharField(max_length=16)
    
    class Meta:
        verbose_name_plural = 'Daftar Alamat'
        
    def __unicode__(self):
        return '%s, kecamatan %s, kabupaten %s, provinsi %s, kodepos %s' % (
            self.alamat, 
            self.kecamatan, 
            self.kabupaten, 
            self.provinsi, 
            self.kodepos
        )


class UserProfile(models.Model):
    JENIS_KELAMIN_CHOICES = (
        (u'LAKI-LAKI',u'Laki-laki'),
        (u'PEREMPUAN',u'Perempuan')
    )
    user = models.OneToOneField(User, related_name='profile')
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(max_length=255)
    jenis_kelamin = models.CharField(max_length=16, 
                                     choices=JENIS_KELAMIN_CHOICES)
    alamat = models.ForeignKey(Alamat, blank=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Profil Pengguna'
        
    def __unicode__(self):
        return 'Profil %s' % self.user
        
        
class UserActivity(models.Model):
    user = models.ForeignKey(User)
    activity = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Aktivitas'
    
    def __unicode__(self):
        return '%s : %s' % (self.user, self.activity)
        
class TingkatKelas(models.Model):
    nama = models.CharField(max_length=8)
    
    class Meta:
        verbose_name_plural = 'Daftar Tingkat Kelas'
    
    def __unicode__(self):
        return self.nama
    
class TahunAjaran(models.Model):
    nama = models.CharField(max_length=16)
    
    class Meta:
        verbose_name_plural = 'Daftar Tahun Ajaran'
    
    def __unicode__(self):
        return self.nama

class Sekolah(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.OneToOneField(Alamat)
    
    class Meta:
        verbose_name_plural = 'Daftar Sekolah'
    
    def __unicode__(self):
        return self.nama

class RuangKelas(models.Model):
    nama = models.CharField(max_length=8)
    sekolah = models.ForeignKey(Sekolah)
    tahun_ajaran = models.ForeignKey(TahunAjaran)
    
    class Meta:
        verbose_name_plural = 'Daftar Kelas'
    
    def __unicode__(self):
        return self.nama

class OrangTua(models.Model):
    user = models.OneToOneField(User)
    profile = models.OneToOneField(UserProfile)
    
    class Meta:
        verbose_name_plural = 'Daftar Orang Tua'
    
    def __unicode__(self):
        return '%s' % self.user



class Guru(models.Model):
    user = models.OneToOneField(User)
    profile = models.OneToOneField(UserProfile)
    sekolah = models.ForeignKey(Sekolah)                    
    class Meta:
        verbose_name_plural = 'Daftar Guru'
    
    def __unicode__(self):
        return '%s' % self.user


class Siswa(models.Model):
    user = models.OneToOneField(User)
    profile = models.OneToOneField(UserProfile)
    sekolah = models.ForeignKey(Sekolah)
    tingkat_kelas = models.ForeignKey(TingkatKelas)
    ruang_kelas = models.ForeignKey(RuangKelas)
    orang_tua = models.ForeignKey(OrangTua)
    
    class Meta:
        verbose_name_plural = 'Daftar Siswa'
    
    def __unicode__(self):
        return '%s' % self.user
        
class MataPelajaran(models.Model):
    JENIS_MATA_PELAJARAN = (
        ('UMUM','Umum'),
        ('MUATAN_LOKAL','Muatan Lokal'),
    )
    nama = models.CharField(max_length=255)
    jenis = models.CharField(max_length=255, choices=JENIS_MATA_PELAJARAN)
    sekolah = models.ForeignKey(Sekolah, blank=True, null=True)
    tingkat_kelas = models.ForeignKey(TingkatKelas, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Mata Pelajaran'
    
    def __unicode__(self):
        return self.nama

class GuruMataPelajaran(models.Model):
    guru = models.ForeignKey(Guru)
    mata_pelajaran = models.ForeignKey(MataPelajaran)
    sekolah = models.ForeignKey(Sekolah)
    kelas = models.ForeignKey(RuangKelas)
    
    class Meta:
        verbose_name_plural = 'Daftar Guru Mata Pelajaran'
    
    def __unicode__(self):
        return '%s - %s' % (self.guru ,self.mata_pelajaran)



class Sesi(models.Model):
    judul = models.CharField(max_length=255)
    ringkasan = models.TextField()
    mata_pelajaran = models.ForeignKey(MataPelajaran)
    sekolah = models.ForeignKey(Sekolah, blank=True, null=True)
    ruang_kelas = models.ForeignKey(RuangKelas, blank=True, null=True)
    tingkat_kelas = models.ForeignKey(TingkatKelas, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Sesi'
    
    def __unicode__(self):
        return self.judul

class MateriPelajaran(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    sesi = models.ForeignKey(Sesi, blank=True, null=True)
    sekolah = models.ForeignKey(Sekolah, blank=True, null=True)
    mata_pelajaran = models.ForeignKey(MataPelajaran, blank=True, null=True)
    ruang_kelas = models.ForeignKey(RuangKelas, blank=True, null=True)
    tingkat_kelas = models.ForeignKey(TingkatKelas, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Materi Pelajaran'
    
    def __unicode__(self):
        return self.judul

class LatihanSoal(models.Model):
    judul = models.CharField(max_length=255)
    sesi = models.ForeignKey(Sesi)
    
    class Meta:
        verbose_name_plural = 'Daftar Latihan Soal'
    
    def __unicode__(self):
        return self.judul

class Soal(models.Model):
    JENIS_SOAL_CHOICES = (
        ('ISIAN', 'Isian'),
        ('PILIHAN_GANDA','Pilihan Ganda'),
    )
    jenis = models.CharField(max_length=32, choices=JENIS_SOAL_CHOICES)
    mata_pelajaran = models.ForeignKey(MataPelajaran)
    tingkat_kelas = models.ForeignKey(TingkatKelas)
    pertanyaan = models.TextField()
    kunci_jawaban = models.TextField()
    latihan_soal = models.ForeignKey(LatihanSoal, blank=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Soal'
    
    def __unicode__(self):
        return self.pertanyaan

class PilihanJawaban(models.Model):
    PILIHAN_CHOICES = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('D', 'd'),
        ('E', 'e'),
    )
    pilihan = models.CharField(max_length=8, choices=PILIHAN_CHOICES)
    isi_pilihan = models.TextField()
    soal = models.ForeignKey(Soal, related_name='pilihan_jawaban')
    
    class Meta:
        verbose_name_plural = 'Daftar Pilihan Jawaban'
    
    def __unicode__(self):
        return '%s . %s ' % (self.pilihan, self.isi_pilihan)

