from django.db import models


class FixedAssets(models.Model):
    date_time = models.DateTimeField(blank=True, null=True)
    responsible_person = models.CharField(max_length=30, blank=True, null=True)
    main_face = models.CharField(max_length=30, blank=True, null=True)
    accounting_account = models.IntegerField(blank=True, null=True)
    property_code = models.IntegerField(blank=True, null=True)
    initial_cost = models.IntegerField(blank=True, null=True)
    percent_annual_depr = models.IntegerField(blank=True, null=True)
    upgrade_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    inventory_number = models.IntegerField(blank=True, null=True)
    depreciation_account = models.IntegerField(blank=True, null=True)
    commissioning_date = models.DateTimeField(blank=True, null=True)
    period_of_execution = models.IntegerField(blank=True, null=True)
    accumulated_depreciation = models.IntegerField(blank=True, null=True)
    book_value = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'fixed_assets'
        verbose_name = 'Принятие на счет ОС'
        verbose_name_plural = "Принятия на счет ОС"

    def __str__(self):
        return str(self.property_code)


class Assets(models.Model):
    operation = models.CharField(max_length=128, blank=True, null=True, )
    asset_selection = models.CharField(max_length=128, blank=True, null=True)
    order = models.CharField(max_length=128, blank=True, null=True)
    order_date = models.IntegerField(blank=True, null=True)
    storage = models.CharField(max_length=128, blank=True, null=True)
    choose_assets = models.CharField(max_length=128, blank=True, null=True)
    inventory_number = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=128, blank=True, null=True)
    passport_number = models.CharField(max_length=128, blank=True, null=True)
    initial_cost = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    method_of_entry = models.CharField(max_length=128, blank=True, null=True)
    current_state = models.IntegerField(blank=True, null=True)
    accounting_account = models.IntegerField(blank=True, null=True)
    responsible_person = models.CharField(max_length=30, blank=True, null=True)
    factory_number = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    present_value = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)

    class Meta:
        db_table = 'assets'
        verbose_name = 'Средства'
        verbose_name_plural = "Средства"

    def __str__(self):
        return str(self.order_date)


class CommissionMember(models.Model):
    assets = models.ForeignKey('Assets', on_delete=models.CASCADE, related_name='commission_members')
    fio = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        db_table = 'commission_member'
        verbose_name = 'Члены комиссии'
        verbose_name_plural = "Члены комиссии"

    def __str__(self):
        return str(self.status)


class Depreciation(models.Model):
    assets = models.OneToOneField('Assets', on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='depreciation')
    depreciation_account = models.IntegerField(blank=True, null=True)
    depreciation_method = models.CharField(max_length=30, blank=True, null=True)
    preliminary_work = models.IntegerField(blank=True, null=True)
    depreciation_schedule = models.IntegerField(blank=True, null=True)
    period_of_execution = models.IntegerField(blank=True, null=True)
    current_depreciation = models.IntegerField(blank=True, null=True)
    depreciation_per_year = models.IntegerField(blank=True, null=True)
    percent_annual_depr = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'depreciation'
        verbose_name = 'Амортизация'
        verbose_name_plural = "Амортизации"

    def __str__(self):
        return str(self.preliminary_work)
