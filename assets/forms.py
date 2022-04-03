from django.forms import *

from assets.models import *


class AssetsForm(ModelForm):
    class Meta:
        model = Assets
        fields = '__all__'


class CommissionMemberForm(ModelForm):
    class Meta:
        model = CommissionMember
        exclude = ('assets',)


class DepreciationForm(ModelForm):
    class Meta:
        model = Depreciation
        exclude = ('assets',)




