# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'UserProfile.nama_lengkap'
        db.delete_column('elearning_userprofile', 'nama_lengkap')

        # Deleting field 'MataPelajaran.tingkat_kelas'
        db.delete_column('elearning_matapelajaran', 'tingkat_kelas')

        # Deleting field 'MataPelajaran.sekolah'
        db.delete_column('elearning_matapelajaran', 'sekolah_id')
    
    
    def backwards(self, orm):
        
        # Adding field 'UserProfile.nama_lengkap'
        db.add_column('elearning_userprofile', 'nama_lengkap', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'MataPelajaran.tingkat_kelas'
        db.add_column('elearning_matapelajaran', 'tingkat_kelas', self.gf('django.db.models.fields.CharField')(default=1, max_length=255), keep_default=False)

        # Adding field 'MataPelajaran.sekolah'
        db.add_column('elearning_matapelajaran', 'sekolah', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['elearning.Sekolah']), keep_default=False)
    
    
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
        'elearning.aktivitas': {
            'Meta': {'object_name': 'Aktivitas'},
            'aktivitas': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'waktu': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'elearning.alamat': {
            'Meta': {'object_name': 'Alamat'},
            'alamat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kabupaten': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Kabupaten']"}),
            'kecamatan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Kecamatan']"}),
            'kodepos': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'provinsi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Provinsi']"})
        },
        'elearning.kabupaten': {
            'Meta': {'object_name': 'Kabupaten'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provinsi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Provinsi']"})
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
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'elearning.provinsi': {
            'Meta': {'object_name': 'Provinsi'},
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
        'elearning.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'alamat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['elearning.Alamat']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_kelamin': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {'max_length': '255'}),
            'tempat_lahir': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['elearning']
