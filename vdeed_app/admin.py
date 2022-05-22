from django.contrib import admin
from .models import deeds1, deeds2, deeds3, globalLamrim2, plastic, paper, misc, counter_target
from django.http import HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import csv

# Register your models here.

# admin.site.register(deeds1)
# admin.site.register(deeds2)
# admin.site.register(deeds3)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class deeds1Resource(resources.ModelResource):
    class Meta:
        model = deeds1


class deeds1Admin(ImportExportModelAdmin, ExportCsvMixin):
    resource_class = deeds1Resource
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


#admin.site.register(deeds1, deeds1Admin)


class deeds2Resource(resources.ModelResource):
    class Meta:
        model = deeds2


class deeds2Admin(ImportExportModelAdmin, ExportCsvMixin):
    resource_class = deeds2Resource
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    #actions = ["export_as_csv"]


#admin.site.register(deeds2, deeds2Admin)


# @admin.register(deeds3)
class deeds3Admin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    actions = ["export_as_csv"]


# @admin.register(globalLamrim2)
class globalLamrim2Admin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "name",  "date_time")
    list_filter = ("name", "date_time")
    actions = ["export_as_csv"]


@admin.register(plastic)
class plasticAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "user",  "date_time", "plastic_bag_counter",
                    "plastic_bottle_counter", "plastic_wrapper_counter", "plastic_cup_straw_counter")
    list_filter = ("user", "date_time", "plastic_bag_counter",
                   "plastic_bottle_counter", "plastic_wrapper_counter", "plastic_cup_straw_counter")
    actions = ["export_as_csv"]


@admin.register(paper)
class sutraRecitationAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "user",  "date_time", "paper_tissue_counter",
                    "paper_counter", "paper_cup_counter", "paper_cigarette_butt_counter")
    list_filter = ("user", "date_time", "paper_tissue_counter",
                   "paper_counter", "paper_cup_counter", "paper_cigarette_butt_counter")
    actions = ["export_as_csv"]


@admin.register(misc)
class mantraRecitationAdmin(ImportExportModelAdmin, ExportCsvMixin):

    list_display = ("id", "user",  "date_time", "misc_glass_bottle_counter",
                    "misc_mask_counter", "misc_others_counter", "misc_can_counter")
    list_filter = ("user", "date_time", "misc_glass_bottle_counter",
                   "misc_mask_counter", "misc_others_counter", "misc_can_counter")
    actions = ["export_as_csv"]


@admin.register(counter_target)
class counterTargetAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ("id", "misc_can_target", "date_time")
    list_filter = ("id", "misc_can_target", "date_time")

    # list_display = ("id", "misc_glass_bottle_target", "misc_mask_target", "misc_others_target", "misc_can_target",
    #               "paper_tissue_target", "paper_target", "paper_cup_target", "paper_cigarette_butt_target",
    #              "plastic_bag_target", "plastic_bottle_target", "plastic_wrapper_target", "plastic_cup_straw_target")

    # list_filter = ("misc_glass_bottle_target", "misc_mask_target", "misc_others_target", "misc_can_target",
    #              "paper_tissue_target", "paper_target", "paper_cup_target", "paper_cigarette_butt_target",
    #             "plastic_bag_target", "plastic_bottle_target", "plastic_wrapper_target", "plastic_cup_straw_target")
