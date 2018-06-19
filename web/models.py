from django.db import models
# from django.db.models.signals import pre_save
# from django.urls import reverse
# from django.utils.text import slugify


class Site(models.Model):
    details = models.CharField(default="Starts", max_length=20)
#
#
# def upload_location(instance, filename):
#     return "%s/%s" % (instance.id, filename)
#
#
# class Vehicle(models.Model):
#     name = models.CharField(max_length=50)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to=upload_location,
#                               null=True, blank=True,
#                               height_field="height_field",
#                               width_field="width_field")
#     height_field = models.IntegerField(default=0)
#     width_field = models.IntegerField(default=0)
#     description = models.TextField()
#     price = models.IntegerField(default=0)
#     updated = models.TimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.TimeField(auto_now=False, auto_now_add=True)
#     # auto_now updates every time it is saved
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse("detail", kwargs={"pk": self.id})
#         # return "/vehicles/%s/" % self.id
#
#     class Meta:
#         ordering = ["-id", "-timestamp", "-updated"]
#
#
# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Vehicle.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def pre_save_vehicle_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_vehicle_receiver, sender=Vehicle)
