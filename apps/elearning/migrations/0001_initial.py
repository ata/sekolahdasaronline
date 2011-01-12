# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Propinsi'
        db.create_table('elearning_propinsi', (
            ('nama', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['Propinsi'])

        # Adding model 'Kabupaten'
        db.create_table('elearning_kabupaten', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Propinsi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Propinsi'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['Kabupaten'])

        # Adding model 'Kecamatan'
        db.create_table('elearning_kecamatan', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kabupaten', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Kabupaten'])),
        ))
        db.send_create_signal('elearning', ['Kecamatan'])

        # Adding model 'Alamat'
        db.create_table('elearning_alamat', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('kabupaten', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Kabupaten'])),
            ('kodepos', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('kecamatan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Kecamatan'])),
            ('Propinsi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Propinsi'])),
            ('alamat', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['Alamat'])

        # Adding model 'UserProfile'
        db.create_table('elearning_userprofile', (
            ('nama_lengkap', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tempat_lahir', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tanggal_lahir', self.gf('django.db.models.fields.DateField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('jenis_kelamin', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('alamat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Alamat'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['UserProfile'])

        # Adding model 'UserActivity'
        db.create_table('elearning_useractivity', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('elearning', ['UserActivity'])

        # Adding model 'TingkatKelas'
        db.create_table('elearning_tingkatkelas', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['TingkatKelas'])

        # Adding model 'RuangKelas'
        db.create_table('elearning_ruangkelas', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['RuangKelas'])

        # Adding model 'TahunAjaran'
        db.create_table('elearning_tahunajaran', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['TahunAjaran'])

        # Adding model 'Sekolah'
        db.create_table('elearning_sekolah', (
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alamat', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['elearning.Alamat'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['Sekolah'])

        # Adding model 'OrangTua'
        db.create_table('elearning_orangtua', (
            ('profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['elearning.UserProfile'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('elearning', ['OrangTua'])

        # Adding model 'Siswa'
        db.create_table('elearning_siswa', (
            ('profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['elearning.UserProfile'], unique=True)),
            ('sekolah', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Sekolah'])),
            ('ruuang_kelas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.RuangKelas'])),
            ('tingkat_kelas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.TingkatKelas'])),
            ('orang_tua', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.OrangTua'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('elearning', ['Siswa'])

        # Adding model 'MataPelajaran'
        db.create_table('elearning_matapelajaran', (
            ('tingkat_kelas', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sekolah', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Sekolah'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['MataPelajaran'])

        # Adding model 'Sesi'
        db.create_table('elearning_sesi', (
            ('ringkasan', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mata_pelajaran', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.MataPelajaran'])),
            ('judul', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('elearning', ['Sesi'])

        # Adding model 'LatihanSoal'
        db.create_table('elearning_latihansoal', (
            ('sesi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.Sesi'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('judul', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('elearning', ['LatihanSoal'])

        # Adding model 'Soal'
        db.create_table('elearning_soal', (
            ('latihan_soal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.LatihanSoal'], blank=True)),
            ('pertanyaan', self.gf('django.db.models.fields.TextField')()),
            ('jenis', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('kunci_jawaban', self.gf('django.db.models.fields.TextField')()),
            ('mata_pelajaran', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.MataPelajaran'])),
            ('tingkat_kelas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elearning.TingkatKelas'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('elearning', ['Soal'])

        # Adding model 'PilihanJawaban'
        db.create_table('elearning_pilihanjawaban', (
            ('soal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pilihan_jawaban', to=orm['elearning.Soal'])),
            ('isi_pilihan', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pilihan', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('elearning', ['PilihanJawaban'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Propinsi'
        db.delete_table('elearning_propinsi')

        # Deleting model 'Kabupaten'
        db.delete_table('elearning_kabupaten')

        # Deleting model 'Kecamatan'
        db.delete_table('elearning_kecamatan')

        # Deleting model 'Alamat'
        db.delete_table('elearning_alamat')

        # Deleting model 'UserProfile'
        db.delete_table('elearning_userprofile')

        # Deleting model 'UserActivity'
        db.delete_table('elearning_useractivity')

        # Deleting model 'TingkatKelas'
        db.delete_table('elearning_tingkatkelas')

        # Deleting model 'RuangKelas'
        db.delete_table('elearning_ruangkelas')

        # Deleting model 'TahunAjaran'
        db.delete_table('elearning_tahunajaran')

        # Deleting model 'Sekolah'
        db.delete_table('elearning_sekolah')

        # Deleting model 'OrangTua'
        db.delete_table('elearning_orangtua')

        # Deleting model 'Siswa'
        db.delete_table('elearning_siswa')

        # Deleting model 'MataPelajaran'
        db.delete_table('elearning_matapelajaran')

        # Deleting model 'Sesi'
        db.delete_table('elearning_sesi')

        # Deleting model 'LatihanSoal'
        db.delete_table('elearning_latihansoal')

        # Deleting model 'Soal'
        db.delete_table('elearning_soal')

        # Deleting model 'PilihanJawaban'
        db.delete_table('elearning_pilihanjawaban')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'elearning.alamat': {
            'Meta': {'object_name': 'Alamat'},
            'Propinsi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Propinsi']"}),
            'alamat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kabupaten': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Kabupaten']"}),
            'kecamatan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Kecamatan']"}),
            'kodepos': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'elearning.kabupaten': {
            'Meta': {'object_name': 'Kabupaten'},
            'Propinsi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Propinsi']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'elearning.kecamatan': {
            'Meta': {'object_name': 'Kecamatan'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kabupaten': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Kabupaten']"}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'elearning.latihansoal': {
            'Meta': {'object_name': 'LatihanSoal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judul': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sesi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Sesi']"})
        },
        'elearning.matapelajaran': {
            'Meta': {'object_name': 'MataPelajaran'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sekolah': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Sekolah']"}),
            'tingkat_kelas': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'elearning.orangtua': {
            'Meta': {'object_name': 'OrangTua'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['elearning.UserProfile']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'elearning.pilihanjawaban': {
            'Meta': {'object_name': 'PilihanJawaban'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isi_pilihan': ('django.db.models.fields.TextField', [], {}),
            'pilihan': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'soal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pilihan_jawaban'", 'to': "orm['elearning.Soal']"})
        },
        'elearning.propinsi': {
            'Meta': {'object_name': 'Propinsi'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'elearning.ruangkelas': {
            'Meta': {'object_name': 'RuangKelas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'elearning.sekolah': {
            'Meta': {'object_name': 'Sekolah'},
            'alamat': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['elearning.Alamat']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'elearning.sesi': {
            'Meta': {'object_name': 'Sesi'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'judul': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mata_pelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.MataPelajaran']"}),
            'ringkasan': ('django.db.models.fields.TextField', [], {})
        },
        'elearning.siswa': {
            'Meta': {'object_name': 'Siswa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orang_tua': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.OrangTua']"}),
            'profile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['elearning.UserProfile']", 'unique': 'True'}),
            'ruuang_kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.RuangKelas']"}),
            'sekolah': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Sekolah']"}),
            'tingkat_kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.TingkatKelas']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'elearning.soal': {
            'Meta': {'object_name': 'Soal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'kunci_jawaban': ('django.db.models.fields.TextField', [], {}),
            'latihan_soal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.LatihanSoal']", 'blank': 'True'}),
            'mata_pelajaran': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.MataPelajaran']"}),
            'pertanyaan': ('django.db.models.fields.TextField', [], {}),
            'tingkat_kelas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.TingkatKelas']"})
        },
        'elearning.tahunajaran': {
            'Meta': {'object_name': 'TahunAjaran'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'elearning.tingkatkelas': {
            'Meta': {'object_name': 'TingkatKelas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'elearning.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'elearning.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'alamat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Alamat']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'nama_lengkap': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {'max_length': '255'}),
            'tempat_lahir': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['elearning']
