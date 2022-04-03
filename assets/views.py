from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from assets.forms import *
from assets.models import *
from django.forms import formset_factory


class AssetsListView(TemplateView):
    template_name = 'assets/demo.html'

    def get(self, request, *args, **kwargs):
        results = Assets.objects.all()
        assets_form = AssetsForm()
        commission_form = CommissionMemberForm()
        depreciation_form = DepreciationForm()
        context = {
            'results': results,
            'assets_form': assets_form,
            'commission_form': commission_form,
            'depreciation_form': depreciation_form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            assets_form = AssetsForm(request.POST)
            commission_form = CommissionMemberForm(request.POST)
            depreciation_form = DepreciationForm(request.POST)
            if assets_form.is_valid():
                initial_form = assets_form.save(commit=True)
                initial_form.save()
                if commission_form.is_valid():
                    commission_form = commission_form.save(commit=False)
                    commission_form.assets_id = initial_form.id
                    commission_form.save()
                if depreciation_form.is_valid():
                    depreciation_form = depreciation_form.save(commit=True)
                    depreciation_form.assets_id = initial_form.id
                    depreciation_form.save()
                else:
                    print(depreciation_form.errors)
        return redirect('index')


class AssetsUpdateView(TemplateView):
    template_name = 'assets/update_demo.html'

    def get(self, request, *args, **kwargs):
        assets = Assets.objects.get(pk=kwargs['pk'])
        DepreciationFormSet = formset_factory(DepreciationForm, min_num=1, extra=0)
        CommissionMemberFormSet = formset_factory(CommissionMemberForm, min_num=1, extra=0)
        form_a = AssetsForm(instance=assets)
        form_d = DepreciationFormSet()
        formset = CommissionMemberFormSet()
        return render(request, self.template_name,
                      context={'form_a': form_a, 'form_d': form_d, 'formset': formset})

    def post(self, request, *args, **kwargs):
        assets = Assets.objects.get(pk=kwargs['pk'])
        commission_member = CommissionMember.objects.filter(assets_id=kwargs['pk']).first()
        form_a = AssetsForm(request.POST, instance=assets)
        form_c = CommissionMemberForm(request.POST, instance=commission_member)
        form_d = DepreciationForm()
        if form_a.is_valid():
            form_a.save()
            if form_d.is_valid():
                form_d.save()
            return redirect('index')
        return render(request, self.template_name,
                      context={'form_a': form_a, 'form_d': form_d})
