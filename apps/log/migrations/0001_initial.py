# Generated by Django 2.2.7 on 2020-08-11 07:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormalLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_number', models.IntegerField(verbose_name='资产编号')),
                ('S_N_Code', models.CharField(max_length=64, verbose_name='S/N码')),
                ('storage_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='入库时间')),
                ('supplier', models.CharField(max_length=64, verbose_name='供应商联系方式')),
                ('manufacturer', models.CharField(max_length=64, verbose_name='制造商联系方式')),
                ('A_S', models.CharField(max_length=64, verbose_name='A_S商联系方式')),
                ('place_origin', models.CharField(max_length=64, verbose_name='原产地')),
                ('special', models.CharField(max_length=64, verbose_name='特殊事项')),
                ('is_calibration', models.PositiveSmallIntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('calibration_cycle', models.IntegerField(blank=True, null=True)),
                ('calibration_cycle_unit', models.PositiveSmallIntegerField(choices=[(1, '日'), (2, '周'), (3, '月'), (4, '季'), (5, '年')], default=1)),
                ('last_calibration_datetime', models.DateTimeField(blank=True, null=True)),
                ('is_maintenance', models.PositiveSmallIntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('maintenance_cycle', models.IntegerField(blank=True, null=True)),
                ('maintenance_cycle_unit', models.PositiveSmallIntegerField(choices=[(1, '日'), (2, '周'), (3, '月'), (4, '季'), (5, '年')], default=1)),
                ('last_maintenance_datetime', models.DateTimeField(blank=True, null=True)),
                ('capacity_utilization', models.PositiveSmallIntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('capacity_utilization_type', models.CharField(blank=True, max_length=16, null=True)),
                ('confirmation', models.FileField(upload_to='confirmation/%Y/%m/%d')),
                ('status_sc', models.PositiveSmallIntegerField(choices=[(0, '取消'), (1, '申请中'), (2, '进行中'), (3, '完结'), (4, '驳回')], default=1)),
                ('examine_stage', models.PositiveSmallIntegerField(choices=[(0, '提交'), (1, 'Part长'), (2, '部门长'), (3, '设施担当'), (4, '设施部门长'), (5, '完结')], default=1)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, '未决裁'), (1, '通过'), (2, '不通过')], default=0)),
                ('reason', models.CharField(blank=True, max_length=128)),
                ('user_id', models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_category', models.CharField(max_length=32, verbose_name='大分类')),
                ('mid_category', models.CharField(max_length=32, verbose_name='中分类')),
                ('small_category', models.CharField(max_length=64, verbose_name='小分类')),
                ('price', models.IntegerField(verbose_name='采购价')),
                ('site', models.CharField(max_length=128, verbose_name='位置')),
                ('department', models.CharField(max_length=32, verbose_name='用户所属部门')),
                ('Resident', models.CharField(max_length=32, verbose_name='担当驻在员')),
                ('LocalPeople', models.CharField(max_length=32, verbose_name='担当现地人')),
                ('log_time', models.DateTimeField(auto_now_add=True, verbose_name='登录时间')),
                ('Specifications', models.FileField(upload_to='specifications', verbose_name='规格书')),
                ('operation', models.FileField(upload_to='ma', verbose_name='操作手册')),
                ('Drawing', models.FileField(upload_to='drawing', verbose_name='图纸')),
                ('align', models.CharField(max_length=128, verbose_name='校准特殊事项')),
                ('maintain', models.CharField(max_length=128, verbose_name='大保养特殊事项')),
                ('images', models.ImageField(upload_to='img', verbose_name='上传图片')),
                ('stage', models.PositiveSmallIntegerField(choices=[(1, '临时登录'), (2, '正式登录')], default=1)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, '未决裁'), (1, '通过'), (2, '驳回')], default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '取消'), (1, '申请中'), (2, '进行中'), (3, '完结'), (4, '驳回')], default=1)),
                ('examine_stage', models.PositiveSmallIntegerField(choices=[(0, '提交'), (1, 'Part长'), (2, '部门长'), (3, '设施担当'), (4, '设施部门长'), (5, '完结')], default=1)),
                ('reason', models.CharField(blank=True, max_length=128)),
                ('is_push_formal', models.PositiveSmallIntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('add_datetime', models.DateTimeField(auto_now_add=True)),
                ('up_datetime', models.DateTimeField(auto_now=True)),
                ('all_state', models.PositiveSmallIntegerField(choices=[(0, '无'), (1, '临时校准'), (2, '正式校准'), (4, '维修'), (5, '大保养'), (6, '废弃'), (7, '丢失')], default=0)),
                ('formal_information_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.FormalLogin')),
                ('user_id', models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TemporaryLogin',
            },
        ),
    ]