from django.contrib import admin

from .models import Listing, User, Bids, Comments, Category

admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Category)
# Register your models here.
