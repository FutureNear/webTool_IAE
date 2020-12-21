from django.contrib import admin
from .models import Income, IncomeType
from .models import ExpenditureType, Expenditure, ExpenditureTypeSub
from .models import DayExpenditure, MonthExpenditure, LoanExpenditure, FixedExpenditure
from .models import Role
from .models import Salary

# Register your models here.


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['R_ID', 'R_ROLENAME', 'R_CREATE_TIME', 'R_UPDATE_TIME']


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['I_ID', 'I_MONEY', 'I_DATE', 'r_rolename', 'it_typename', 'I_CREATE_TIME', 'I_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def it_typename(self, obj):
        return obj.IT_TYPENAME
    it_typename.short_description = '收入类型'


@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ['IT_ID', 'IT_TYPENAME', 'IT_CREATE_TIME', 'IT_UPDATE_TIME']


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ['S_ID', 'S_MONEY', 'r_rolename', 'S_DATE', 'it_typename', 'S_CREATE_TIME', 'S_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def it_typename(self, obj):
        return obj.IT_TYPENAME
    it_typename.short_description = '收入类型'


@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['E_ID', 'E_MONEY', 'r_rolename', 'E_DATE', 'E_CREATE_TIME', 'E_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'


@admin.register(ExpenditureType)
class ExpenditureTypeAdmin(admin.ModelAdmin):
    list_display = ['ET_ID', 'ET_TYPENAME', 'ET_CREATE_TIME', 'ET_UPDATE_TIME']


@admin.register(ExpenditureTypeSub)
class ExpenditureTypeSubAdmin(admin.ModelAdmin):
    list_display = ['ETS_ID', 'ETS_TYPENAME', 'et_typename', 'ETS_CREATE_TIME', 'ETS_UPDATE_TIME']

    def et_typename(self, obj):
        return obj.ET_TYPENAME
    et_typename.short_description = '支出类型'


@admin.register(MonthExpenditure)
class MonthExpenditureAdmin(admin.ModelAdmin):
    list_display = ['ME_ID', 'ME_MONEY', 'r_rolename', 'et_typename', 'ME_CREATE_TIME', 'ME_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def et_typename(self, obj):
        return obj.ET_TYPENAME
    et_typename.short_description = '支出类型'


@admin.register(DayExpenditure)
class DayExpenditureAdmin(admin.ModelAdmin):
    list_display = ['DE_ID', 'DE_MONEY', 'r_rolename', 'ets_typename', 'DE_DATETIME', 'DE_CREATE_TIME', 'DE_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def ets_typename(self, obj):
        return obj.ETS_TYPENAME
    ets_typename.short_description = '支出子类型'


@admin.register(LoanExpenditure)
class LoanExpenditureAdmin(admin.ModelAdmin):
    list_display = ['LE_ID', 'LE_MONEY', 'r_rolename', 'LE_DATE', 'ets_typename', 'LE_CREATE_TIME', 'LE_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def ets_typename(self, obj):
        return obj.ETS_TYPENAME
    ets_typename.short_description = '支出子类型'


@admin.register(FixedExpenditure)
class FixedExpenditureAdmin(admin.ModelAdmin):
    list_display = ['FE_ID', 'FE_MONEY', 'r_rolename', 'FE_DATE', 'ets_typename', 'FE_CREATE_TIME', 'FE_UPDATE_TIME']

    def r_rolename(self, obj):
        return obj.R_ROLENAME
    r_rolename.short_description = '角色'

    def ets_typename(self, obj):
        return obj.ETS_TYPENAME
    ets_typename.short_description = '支出子类型'
