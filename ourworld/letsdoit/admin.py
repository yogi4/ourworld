# Register your models here.
from letsdoit.models import Poll, Choice, Category, ServiceProvider
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("servicename", "categoryImage")
    fieldsets = (
        (None, {
             "fields": ("servicename", "categoryImage")

        }),
    )

class ServicesProvAdmin(admin.ModelAdmin):
  #  list_display = ("Service", "Category")
    fieldsets = [
        (None, {
          "fields": ("fullName", "contactNum1","contactNum2","email","image",
          "providername","servicename","speciality","address1" ,"address2","city","state", "country" ,"zipcode"
          )
        }),
        ('Optional Fields',{
            'fields': ("description","serviceCharge")
        })
    ]
  #  inlines = [ChoiceInline]
admin.site.register(ServiceProvider,ServicesProvAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Category,CategoryAdmin)