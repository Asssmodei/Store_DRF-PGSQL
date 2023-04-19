from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Users(BaseModel):
    class Meta:
        db_table = 'users'
        managed = False
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    second_name = models.CharField(null=False, max_length=50)
    phone = models.CharField(null=False, max_length=12)
    email = models.CharField(null=False, max_length=100)

    def __str__(self):
        return f"{self.name} {self.second_name}"


class Colours(BaseModel):
    class Meta:
        db_table = 'colours'
    colour_id = models.BigAutoField(primary_key=True)
    colour_name = models.CharField(null=False, max_length=30)


class Diler(BaseModel):
    class Meta:
        db_table = 'diler'
    diler_id = models.AutoField(primary_key=True)
    diler_name = models.CharField(null=False, max_length=30)
    is_related = models.BooleanField(null=False)


class Shipment(BaseModel):
    class Meta:
        db_table = 'shipment'
    ship_id = models.BigAutoField(primary_key=True)
    ship_date = models.DateField(null=False)
    weight = models.FloatField(max_length=30)
    diler = models.ForeignKey(to='Diler', on_delete=models.CASCADE)


class Furniture(BaseModel):
    class Meta:
        db_table = 'furniture'

    length = models.FloatField(max_length=20, null=False, blank=False)
    height = models.FloatField(max_length=20, null=False, blank=False)
    depth = models.FloatField(max_length=20, null=False, blank=False)
    ship = models.ForeignKey(to='Shipment', on_delete=models.CASCADE)
    colour = models.ForeignKey(to='Colours', on_delete=models.CASCADE)


class Sofa(BaseModel):
    class Meta:
        db_table = 'sofa'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    num_seats = models.IntegerField(null=False, blank=False)
    expand = models.BooleanField(null=False)
    corner = models.BooleanField(null=False)

    def __str__(self):
        if self.expand:
            return f"Диван угловой {self.self_id}"
        else:
            return f"Диван {self.self_id}"


class Wardrobe(BaseModel):
    class Meta:
        db_table = 'wardrobe'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    num_shelfs = models.IntegerField(null=False, blank=False)


class Stol(BaseModel):
    class Meta:
        db_table = 'stol'

    self_id = models.AutoField(primary_key=True)
    fur = models.ForeignKey(to='Furniture', on_delete=models.PROTECT)
    expand = models.BooleanField(null=False)


class Orders(BaseModel):
    class Meta:
        db_table = 'orders'

    user = models.ForeignKey(to='Users', on_delete=models.PROTECT)
    order_date = models.DateField(null=False)
    order_cost = models.FloatField(max_length=15, null=False)
