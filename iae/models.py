from django.db import models


# 定义角色表
class Role(models.Model):
    R_ID = models.AutoField(verbose_name="主键", name="R_ID", primary_key=True)
    R_ROLENAME = models.CharField(verbose_name="角色名", name="R_ROLENAME", max_length=10, null=False)
    R_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="R_CREATE_TIME", auto_now_add=True)
    R_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="R_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "角色"

    def __str__(self):
        return self.R_ROLENAME


# 收入类型
class IncomeType(models.Model):
    IT_ID = models.AutoField(verbose_name="主键", name="IT_ID", primary_key=True)
    IT_TYPENAME = models.CharField(verbose_name="收入类型", name="IT_TYPENAME", max_length=10, null=False)
    IT_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="IT_CREATE_TIME", auto_now_add=True)
    IT_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="IT_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "收入类型字典"

    def __str__(self):
        return self.IT_TYPENAME


# 收入汇总表
class Income(models.Model):
    I_ID = models.AutoField(verbose_name="主键", name="I_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    I_MONEY = models.IntegerField(verbose_name="月收入", name="I_MONEY", null=False)
    IT_TYPENAME = models.ForeignKey(to=IncomeType, to_field="IT_ID", on_delete=models.CASCADE, verbose_name="收入类型", name="IT_TYPENAME", null=False)
    I_DATE = models.CharField(verbose_name="月时间", name="I_DATE", max_length=10, null=False)
    I_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="I_CREATE_TIME", auto_now_add=True)
    I_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="I_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "收入汇总"


# 月工资表
class Salary(models.Model):
    S_ID = models.AutoField(verbose_name="主键", name="S_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    IT_TYPENAME = models.ForeignKey(to=IncomeType, to_field="IT_ID", on_delete=models.CASCADE, verbose_name="收入类型", name="IT_TYPENAME", null=False)
    S_MONEY = models.IntegerField(verbose_name="月工资", name="S_MONEY", null=False)
    S_DATE = models.CharField(verbose_name="工资时间", name="S_DATE", max_length=10, null=False)
    S_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="S_CREATE_TIME", auto_now_add=True)
    S_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="S_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "月工资明细"


# 支出类型表
class ExpenditureType(models.Model):
    ET_ID = models.AutoField(verbose_name="主键", name="ET_ID", primary_key=True)
    ET_TYPENAME = models.CharField(verbose_name="支出类型", name="ET_TYPENAME", max_length=10, null=False)
    ET_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="ET_CREATE_TIME", auto_now_add=True)
    ET_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="ET_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "支出类型字典"

    def __str__(self):
        return self.ET_TYPENAME


# 支出子类型表
class ExpenditureTypeSub(models.Model):
    ETS_ID = models.AutoField(verbose_name="主键", name="ETS_ID", primary_key=True)
    ET_TYPENAME = models.ForeignKey(to=ExpenditureType, to_field="ET_ID", on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    ETS_TYPENAME = models.CharField(verbose_name="支出子类型", name="ETS_TYPENAME", max_length=10, null=False)
    ETS_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="ETS_CREATE_TIME", auto_now_add=True)
    ETS_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="ETS_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "支出子类型字典"

    def __str__(self):
        return self.ETS_TYPENAME


class Expenditure(models.Model):
    E_ID = models.AutoField(verbose_name="主键", name="E_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    ET_TYPENAME = models.ForeignKey(to=ExpenditureType, to_field="ET_ID", on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    E_MONEY = models.IntegerField(verbose_name="支出", name="E_MONEY", null=False)
    E_DATE = models.CharField(verbose_name="子支出类型", name="E_DATE", max_length=10, null=False)
    E_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="E_CREATE_TIME", auto_now_add=True)
    E_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="E_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "支出汇总"


class LoanExpenditure(models.Model):
    LE_ID = models.AutoField(verbose_name="主键", name="LE_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    # ET_TYPENAME = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    ETS_TYPENAME = models.ForeignKey(to=ExpenditureTypeSub, to_field="ETS_ID", on_delete=models.CASCADE, verbose_name="支出子类型", name="ETS_TYPENAME", null=False)
    LE_MONEY = models.IntegerField(verbose_name="借贷支出", name="LE_MONEY", null=False)
    LE_DATE = models.CharField(verbose_name="月时间", name="LE_DATE", max_length=10, null=False)
    LE_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="LE_CREATE_TIME", auto_now_add=True)
    LE_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="LE_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "借贷支出明细表"


class FixedExpenditure(models.Model):
    FE_ID = models.AutoField(verbose_name="主键", name="FE_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    # ET_TYPENAME = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    ETS_TYPENAME = models.ForeignKey(to=ExpenditureTypeSub, to_field="ETS_ID", on_delete=models.CASCADE, verbose_name="支出子类型", name="ETS_TYPENAME", null=False)
    FE_MONEY = models.IntegerField(verbose_name="固定支出", name="FE_MONEY", null=False)
    FE_DATE = models.CharField(verbose_name="月时间", name="FE_DATE", max_length=10, null=False)
    FE_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="FE_CREATE_TIME", auto_now_add=True)
    FE_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="FE_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "固定支出明细"


class DayExpenditure(models.Model):
    DE_ID = models.AutoField(verbose_name="主键", name="DE_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    # ET_TYPENAME = models.ForeignKey(ExpenditureType, on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    ETS_TYPENAME = models.ForeignKey(to=ExpenditureTypeSub, to_field="ETS_ID", on_delete=models.CASCADE, verbose_name="支出子类型", name="ETS_TYPENAME", null=False)
    DE_MONEY = models.IntegerField(verbose_name="日支出", name="DE_MONEY", null=False)
    DE_DATETIME = models.DateField(verbose_name="支出时间", name="DE_DATETIME")
    DE_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="DE_CREATE_TIME", auto_now_add=True)
    DE_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="DE_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "日支出明细"


class MonthExpenditure(models.Model):
    ME_ID = models.AutoField(verbose_name="主键", name="ME_ID", primary_key=True)
    R_ROLENAME = models.ForeignKey(to=Role, to_field="R_ID", on_delete=models.CASCADE, verbose_name="角色名", name="R_ROLENAME", null=False)
    ET_TYPENAME = models.ForeignKey(to=ExpenditureType, to_field="ET_ID", on_delete=models.CASCADE, verbose_name="支出类型", name="ET_TYPENAME", null=False)
    ME_MONEY = models.IntegerField(verbose_name="月支出", name="ME_MONEY", null=False)
    ME_DATE = models.CharField(verbose_name="月时间", name="ME_DATE", max_length=10, null=False)
    ME_CREATE_TIME = models.DateTimeField(verbose_name="创建时间", name="ME_CREATE_TIME", auto_now_add=True)
    ME_UPDATE_TIME = models.DateTimeField(verbose_name="更新时间", name="ME_UPDATE_TIME", auto_now=True)

    class Meta(object):
        verbose_name_plural = "月支出汇总表"
