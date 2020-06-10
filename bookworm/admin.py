from django.contrib import admin
from .models import *
import qrcode
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def create_qr_code(modeladmin, request, queryset):

    for query in queryset:
        qr = qrcode.QRCode(
        	version=1,
        	box_size=15,
        	border=5
        )
        data = query.__class__.__name__
        if data == "Extra_user_info":
            data = "utente" + "_" + str(query.id)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save("C:/Users/copow/mybookworm/media/qr_code/user/" + data + '.jpg')
            data = ""
            #return HttpResponse(data)
        elif data == "Volume":
            data = "volume" + "_" + str(query.id)
            print(data)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save("C:/Users/copow/mybookworm/media/qr_code/volume/" + data + '.jpg')
            data = ""
            print(data)

@admin.register(Sezione)
class SezioneAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_release_date', 'language', 'sezione')
    ordering = ('book_name',)
    filter_horizontal = ('author', 'genres')
    search_fields = ('book_name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('type',)
    search_fields = ('type',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ('last_name',)
    search_fields = ('last_name','first_name')

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    ordering = ('book',)
    search_fields = ('book__book_name',)
    actions = [create_qr_code]

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'volume', 'return_date')
    ordering = ('user',)
    search_fields = ('volume',)
    change_list_template = 'admin/loan/create_loan.html'

@admin.register(Extra_user_info)
class Extra_user_infoAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone_number')
    ordering = ('user',)
    search_fields = ('user__username',)
    actions = [create_qr_code]
