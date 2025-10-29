
from django.db import models


class Acudiente(models.Model):
    id_acu = models.AutoField(primary_key=True)
    num_doc_acu = models.CharField(max_length=20)
    tel_acu = models.CharField(max_length=20, blank=True, null=True)
    dir_acu = models.CharField(max_length=100, blank=True, null=True)
    id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usu')

    class Meta:
        managed = False
        db_table = 'acudiente'


class Administrativo(models.Model):
    id_adm = models.AutoField(primary_key=True)
    num_doc_adm = models.CharField(max_length=20)
    tel_adm = models.CharField(max_length=20, blank=True, null=True)
    dir_adm = models.CharField(max_length=100, blank=True, null=True)
    tip_carg_adm = models.CharField(max_length=50, blank=True, null=True)
    id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usu')

    class Meta:
        managed = False
        db_table = 'administrativo'


class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True)
    grd_cur = models.CharField(max_length=10)
    num_alum_cur = models.IntegerField(blank=True, null=True)
    cup_disp_cur = models.IntegerField(blank=True, null=True)
    id_inst = models.ForeignKey('Institucion', models.DO_NOTHING, db_column='id_inst')

    class Meta:
        managed = False
        db_table = 'curso'


class Documento(models.Model):
    id_doc = models.AutoField(primary_key=True)
    reg_civil_doc = models.CharField(max_length=100, blank=True, null=True)
    doc_idn_acu = models.CharField(max_length=100, blank=True, null=True)
    doc_idn_alum = models.CharField(max_length=100, blank=True, null=True)
    cnt_vac_doc = models.CharField(max_length=100, blank=True, null=True)
    adres_doc = models.CharField(max_length=100, blank=True, null=True)
    fot_alum_doc = models.CharField(max_length=100, blank=True, null=True)
    visa_extr_doc = models.CharField(max_length=100, blank=True, null=True)
    cer_med_disca_doc = models.CharField(max_length=100, blank=True, null=True)
    cer_esc_doc = models.CharField(max_length=100, blank=True, null=True)
    id_mat = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_mat')

    class Meta:
        managed = False
        db_table = 'documento'


class Estudiante(models.Model):
    id_est = models.AutoField(primary_key=True)
    tip_doc_est = models.CharField(max_length=20, blank=True, null=True)
    num_doc_est = models.CharField(max_length=20)
    fch_nac_estu = models.DateField(blank=True, null=True)
    tel_estu = models.CharField(max_length=20, blank=True, null=True)
    id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usu')
    id_acu = models.ForeignKey(Acudiente, models.DO_NOTHING, db_column='id_acu')

    class Meta:
        managed = False
        db_table = 'estudiante'


class Institucion(models.Model):
    id_inst = models.AutoField(primary_key=True)
    nom_inst = models.CharField(max_length=100)
    tip_inst = models.CharField(max_length=20, blank=True, null=True)
    cod_dane_inst = models.CharField(max_length=20, blank=True, null=True)
    dep_inst = models.CharField(max_length=50, blank=True, null=True)
    mun_inst = models.CharField(max_length=50, blank=True, null=True)
    dire_inst = models.CharField(max_length=100, blank=True, null=True)
    tel_inst = models.CharField(max_length=20, blank=True, null=True)
    ema_inst = models.CharField(max_length=100, blank=True, null=True)
    id_adm = models.ForeignKey(Administrativo, models.DO_NOTHING, db_column='id_adm')

    class Meta:
        managed = False
        db_table = 'institucion'


class Matricula(models.Model):
    id_mat = models.AutoField(primary_key=True)
    fch_reg_mat = models.DateField()
    est_mat = models.CharField(max_length=20, blank=True, null=True)
    obs_mat = models.CharField(max_length=255, blank=True, null=True)
    id_cur = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_cur')
    id_est = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_est')

    class Meta:
        managed = False
        db_table = 'matricula'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nom_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True)
    nom_usu = models.CharField(max_length=50)
    ape_usu = models.CharField(max_length=50)
    ema_usu = models.CharField(unique=True, max_length=100)
    con_usu = models.CharField(max_length=255)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuario'
