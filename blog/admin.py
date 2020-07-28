from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Category, Order #Comment

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    list_display = (
            'author',
            'option',
            'quantity',
            'email',
            'phone',
            'message_store',
            'post',
            )
    search_fields = ('author','option', 'phone')
    pass

#class CommentAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(Comment, CommentAdmin)
# Register your models here.
