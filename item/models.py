from django.db import models

class CraftCategory(models.Model):
    name = models.CharField('Категория крафта', max_length=255, blank=True, null=True)
    name_en = models.CharField('Категория крафта(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

class CraftSubCategory(models.Model):
    name = models.CharField('Подкатегория крафта', max_length=255, blank=True, null=True)
    name_en = models.CharField('Подкатегория крафта(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

#     ---------------------------------\
class ResourceCategory(models.Model):
    name = models.CharField('Категория ', max_length=255, blank=True, null=True)
    name_en = models.CharField('Категория (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

class ResourceType(models.Model):
    name = models.CharField('Название типа', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название типа(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)


class ResourceSlot(models.Model):
    name = models.CharField('Название слота', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название слота(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)


class Resource(models.Model):
    category = models.ForeignKey(ResourceCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип')
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип')
    slot = models.ForeignKey(ResourceSlot, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Слот')
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Изображение', upload_to='images/craft_items/', blank=True)
    tier = models.IntegerField(default=0)
#     ---------------------------------

class ItemCategory(models.Model):
    name = models.CharField('Категория', max_length=255, blank=True, null=True)
    name_en = models.CharField('Категория (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

class ItemSubCategory(models.Model):
    name = models.CharField('Подкатегория', max_length=255, blank=True, null=True)
    name_en = models.CharField('Подкатегория (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)


class ItemType(models.Model):
    name = models.CharField('Название типа', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название типа(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)


class ItemSlot(models.Model):
    name = models.CharField('Название слота', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название слота(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)


class Item(models.Model):
    name = models.CharField('Название предмета', max_length=255, blank=True, null=True)
    title = models.CharField('Название предмета', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название предмета(оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Изображение', upload_to='images/items/', blank=True)
    category = models.ForeignKey(ItemCategory,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Категория ')
    subcategory = models.ForeignKey(ItemSubCategory,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Подкатегория')
    crafted_by = models.ForeignKey(CraftCategory,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Категория крафта')
    type = models.ForeignKey(ItemType,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Тип')
    slot = models.ForeignKey(ItemSlot,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Слот')
    tier = models.IntegerField(default=0)
    rarity = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    level = models.IntegerField('Уровень', default=0)
    gear_score = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    bop = models.BooleanField(default=False)


class ItemIngredient(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
    ingredient = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)