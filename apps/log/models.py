from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


#临时登录
class TemporaryLogin(models.Model):
    user_id=models.ManyToManyField(User,default=1)
    big_category = models.CharField(max_length=32,verbose_name='大分类')
    mid_category = models.CharField(max_length=32,verbose_name='中分类')
    small_category = models.CharField(max_length=64,verbose_name='小分类')
    price = models.IntegerField(verbose_name='采购价')
    site = models.CharField(max_length=128,verbose_name='位置')
    department=models.CharField(max_length=32,verbose_name='用户所属部门')
    Resident=models.CharField(max_length=32,verbose_name='担当驻在员')
    LocalPeople=models.CharField(max_length=32,verbose_name='担当现地人')
    log_time = models.DateTimeField(auto_now_add=True,verbose_name='登录时间')
    Specifications=models.FileField(upload_to='specifications',verbose_name='规格书')
    operation = models.FileField(upload_to='ma',verbose_name='操作手册')
    Drawing = models.FileField(upload_to='drawing',verbose_name='图纸')
    align=models.CharField(max_length=128,verbose_name='校准特殊事项')
    maintain=models.CharField(max_length=128,verbose_name='大保养特殊事项')
    images=models.ImageField(upload_to='img',verbose_name='上传图片')
    stage_choices = (
        (1, '临时登录'),
        (2, '正式登录'),
    )
    stage = models.PositiveSmallIntegerField(choices=stage_choices, default=1)  # 阶段

    state_choices = (
        (0, '未决裁'),
        (1, '通过'),
        (2, '驳回'),
    )
    state = models.PositiveSmallIntegerField(choices=state_choices, default=0)  # 当前阶段状态

    status_choices = (
        (0, '取消'),
        (1, '申请中'),
        (2, '进行中'),
        (3, '完结'),
        (4, '驳回'),
    )
    status = models.PositiveSmallIntegerField(choices=status_choices, default=1)  # 当前状态

    examine_stage_choices = (
        (0, '提交'),
        (1, 'Part长'),
        (2, '部门长'),
        (3, '设施担当'),
        (4, '设施部门长'),
        (5, '完结'),
    )
    examine_stage = models.PositiveSmallIntegerField(choices=examine_stage_choices, default=1)  # 当前审核阶段
    reason = models.CharField(blank=True, max_length=128)  # 驳回理由

    is_push_formal_choices = (
        (0, '否'),
        (1, '是')
    )
    is_push_formal = models.PositiveSmallIntegerField(choices=is_push_formal_choices, default=0)  # 是否已提交正式登录信息

    formal_information_id = models.ForeignKey('FormalLogin', null=True,on_delete=models.CASCADE)  # Judgement_Flow的ID
    add_datetime = models.DateTimeField(auto_now_add=True)
    up_datetime = models.DateTimeField(auto_now=True)

    all_state_choices = (
        (0, '无'),
        (1, '临时校准'),
        (2, '正式校准'),
        (4, '维修'),
        (5, '大保养'),
        (6, '废弃'),
        (7, '丢失'),
    )
    all_state = models.PositiveSmallIntegerField(choices=all_state_choices, default=0)  # 当前审核阶段


    class Meta:
        db_table='TemporaryLogin'


#正式登录
class FormalLogin(models.Model):
    user_id = models.ManyToManyField(User,default=1)
    asset_number=models.IntegerField(blank=False,verbose_name='资产编号')
    S_N_Code=models.CharField(max_length=64,verbose_name='S/N码')
    storage_time=models.DateTimeField(default=datetime.now,verbose_name='入库时间')
    supplier=models.CharField(max_length=64,verbose_name='供应商联系方式')
    manufacturer=models.CharField(max_length=64,verbose_name='制造商联系方式')
    A_S=models.CharField(max_length=64,verbose_name='A_S商联系方式')
    place_origin=models.CharField(max_length=64,verbose_name='原产地')
    special=models.CharField(max_length=64,verbose_name='特殊事项')
    is_calibration_choices = (
        (0, '否'),
        (1, '是')
    )
    is_calibration = models.PositiveSmallIntegerField(choices=is_calibration_choices, default=0)  # 是否校准
    calibration_cycle = models.IntegerField(blank=True, null=True)  # 校准周期
    calibration_cycle_unit_choices = (
        (1, '日'),
        (2, '周'),
        (3, '月'),
        (4, '季'),
        (5, '年')
    )
    calibration_cycle_unit = models.PositiveSmallIntegerField(choices=calibration_cycle_unit_choices,
                                                              default=1)  # 校准周期单位
    last_calibration_datetime = models.DateTimeField(blank=True, null=True)  # 上次校准时间

    is_maintenance_choices = (
        (0, '否'),
        (1, '是')
    )
    is_maintenance = models.PositiveSmallIntegerField(choices=is_maintenance_choices, default=0)  # 是否大保养

    maintenance_cycle = models.IntegerField(blank=True, null=True)  # 校准大保养周期
    maintenance_cycle_unit_choices = (
        (1, '日'),
        (2, '周'),
        (3, '月'),
        (4, '季'),
        (5, '年')
    )
    maintenance_cycle_unit = models.PositiveSmallIntegerField(choices=maintenance_cycle_unit_choices,
                                                              default=1)  # 大保养单位
    last_maintenance_datetime = models.DateTimeField(blank=True, null=True)  # 上次大保养时间

    is_capacity_utilization_choices = (
        (0, '否'),
        (1, '是')
    )
    capacity_utilization = models.PositiveSmallIntegerField(choices=is_capacity_utilization_choices, default=0)  # 制动状态
    capacity_utilization_type = models.CharField(blank=True, null=True, max_length=16)  # 1:耐久，2：性能，3：碰撞

    confirmation = models.FileField(upload_to='confirmation/%Y%m%d')  # 确认书

    status_sc_choices = (
        (0, '取消'),
        (1, '申请中'),
        (2, '进行中'),
        (3, '完结'),
        (4, '驳回'),
    )
    status_sc = models.PositiveSmallIntegerField(choices=status_sc_choices, default=1)  # 当前状态
    examine_stage_choices = (
        (0, '提交'),
        (1, 'Part长'),
        (2, '部门长'),
        (3, '设施担当'),
        (4, '设施部门长'),
        (5, '完结'),
    )
    examine_stage = models.PositiveSmallIntegerField(choices=examine_stage_choices, default=1)  # 当前审核阶段

    state_choices = (
        (0, '未决裁'),
        (1, '通过'),
        (2, '不通过'),
    )
    state = models.PositiveSmallIntegerField(choices=state_choices, default=0)  # 当前阶段状态
    reason = models.CharField(blank=True, max_length=128)  # 驳回理由



    class Meta:

        db_table='FormalLogin'
