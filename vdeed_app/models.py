from django.db import models
from django.contrib.auth.models import User


class deeds1(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class deeds2(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class deeds3(models.Model):
    deed = models.CharField(max_length=500)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class globalLamrim2(models.Model):
    deed = models.CharField(max_length=600)
    name = models.CharField(max_length=80)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class plastic(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # plastic bag
    plastic_bag_counter = models.PositiveIntegerField(default=0)
    # plastic bottle
    plastic_bottle_counter = models.PositiveIntegerField(default=0)
    # plastic wrapper
    plastic_wrapper_counter = models.PositiveIntegerField(default=0)
    # plastic cup and straw
    plastic_cup_straw_counter = models.PositiveIntegerField(default=0)

    plastic_bag_target = models.PositiveIntegerField(default=0)
    plastic_bottle_target = models.PositiveIntegerField(default=0)
    plastic_wrapper_target = models.PositiveIntegerField(default=0)
    plastic_cup_straw_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class paper(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # paper tissue
    paper_tissue_counter = models.PositiveIntegerField(default=0)
    # paper
    paper_counter = models.PositiveIntegerField(default=0)
    paper_cup_counter = models.PositiveIntegerField(default=0)
    paper_cigarette_butt_counter = models.PositiveIntegerField(default=0)

    paper_tissue_target = models.PositiveIntegerField(default=0)
    paper_target = models.PositiveIntegerField(default=0)
    paper_cup_target = models.PositiveIntegerField(default=0)
    paper_cigarette_butt_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class misc(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    misc_glass_bottle_counter = models.PositiveIntegerField(default=0)
    misc_mask_counter = models.PositiveIntegerField(default=0)
    misc_others_counter = models.PositiveIntegerField(default=0)
    misc_can_counter = models.PositiveIntegerField(default=0)

    misc_glass_bottle_target = models.PositiveIntegerField(default=0)
    misc_mask_target = models.PositiveIntegerField(default=0)
    misc_others_target = models.PositiveIntegerField(default=0)
    misc_can_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class counter_target(models.Model):

    plastic_bag_target = models.PositiveIntegerField(default=0)
    plastic_bottle_target = models.PositiveIntegerField(default=0)
    plastic_wrapper_target = models.PositiveIntegerField(default=0)
    plastic_cup_straw_target = models.PositiveIntegerField(default=0)

    paper_tissue_target = models.PositiveIntegerField(default=0)
    paper_target = models.PositiveIntegerField(default=0)
    paper_cup_target = models.PositiveIntegerField(default=0)
    paper_cigarette_butt_target = models.PositiveIntegerField(default=0)

    misc_glass_bottle_target = models.PositiveIntegerField(default=0)
    misc_mask_target = models.PositiveIntegerField(default=0)
    misc_others_target = models.PositiveIntegerField(default=0)
    misc_can_target = models.PositiveIntegerField(default=0)

    date_time = models.DateTimeField(auto_now=True)
