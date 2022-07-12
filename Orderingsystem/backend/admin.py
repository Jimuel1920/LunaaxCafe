from django.contrib import admin
from  .models import user , Comment , Product , Meat
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here
from main.models import Shippingaddress


admin.site.site_header = " BACK-END ADMINISTRATOR"
admin.site.site_title = "Adminstration Area"
admin.site.index_title = "Welcome to Adimistrator Area"

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

#------- admin
class Useradmin(admin.ModelAdmin):
    list_display = ['image_tag','user_uid','user_fname','user_lname','user_position','user_username','user_password','pub_date']
    search_fields = ['user_uid']
    inlines = [CommentInline]
    
admin.site.register(user,Useradmin)

class CommentAdmin(admin.ModelAdmin):
    list_display  =  ['name','body','user_com','created_on','active']
    list_filter   = ['active', 'created_on']
    search_fields = ['name','email','body']
    actions = ['approve_comment']
    def approve_comment(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['image_tag','pro_id','pro_name','pro_price','pro_price','pro_size','Catergoty']

admin.site.register(Product, Productadmin)

class Meatadmin(admin.ModelAdmin):
    list_display = ['image_tag','m_id','m_name','m_price','m_price','m_size','m_cat']

admin.site.register(Meat, Meatadmin)
