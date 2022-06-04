from django.contrib import admin

from .models import Author, Book, Address, Country

# Register your models here.

# Create configuration class based on admin.modeladmin


class CountryAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "postal_code")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    # Shows fields and makes them read only
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    # Replaces the default model __str__ view and sets tuple as columns
    list_display = ("title", "author")


# register Book and the admin config object
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
