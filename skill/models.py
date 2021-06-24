from django.db import models
from pytils.translit import slugify



class Weapon(models.Model):
    order = models.IntegerField(default=50)
    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    main_char = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='images/weapon/', blank=True)
    description = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.order} | {self.name}'

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Weapon, self).save(*args, **kwargs)

    class Meta:
        ordering = ['order']


class SkillTree(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Оружие', related_name='trees')
    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    description = models.TextField(blank=True, null=True)
    spent_points = models.IntegerField(default=0)
    checked_skills = models.JSONField(blank=True,null=True)

    def __str__(self):
        return f'{self.name} | {self.name_en}'


class Skill(models.Model):
    tree = models.ForeignKey(SkillTree, on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Ветка', related_name='skills')
    parent_skill = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name='Родитель')
    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    name_en = models.CharField('Название (оригинал)', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Иконка', upload_to='images/skill/', blank=True)
    description = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    is_parent = models.BooleanField(default=False)
    is_has_parent = models.BooleanField(default=False)
    is_active_skill = models.BooleanField(default=False)
    is_ultimate = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    is_can_check = models.BooleanField(default=False)
    is_empty = models.BooleanField(default=False)
    is_has_left_parent = models.BooleanField(default=False)
    row = models.IntegerField('Ряд', default=1)
    col = models.IntegerField('Колонка', default=1)

    def __str__(self):
        return f'{self.name_en} | {self.name} | R: {self.row} C:{self.col}'

    class Meta:
        ordering = ['name_en']


class Build(models.Model):
    weapon1 = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Оружие',related_name='weapon1')
    weapon2 = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='Оружие',related_name='weapon2')
    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    checked_skills_left_w1 = models.JSONField(blank=True,null=True)
    checked_skills_right_w1 = models.JSONField(blank=True,null=True)
    checked_skills_left_w2 = models.JSONField(blank=True, null=True)
    checked_skills_right_w2 = models.JSONField(blank=True, null=True)
    total_rating = models.IntegerField('Рейтинг', default=1)
    votes = models.IntegerField('Голосов', default=1)
    is_active = models.BooleanField(default=False)



    class Meta:
        ordering = ['-id']