from django.contrib import admin
from assets.models import FixedAssets
from assets.models import Assets
from assets.models import CommissionMember
from assets.models import Depreciation


admin.site.register(FixedAssets)
admin.site.register(CommissionMember)
admin.site.register(Assets)
admin.site.register(Depreciation)
