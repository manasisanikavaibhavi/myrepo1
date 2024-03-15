from django.contrib import admin
from .models import *



# Register your models here.
class LoginAdmin(admin.ModelAdmin):
 list_display=['email','password']


admin.site.register(Login,LoginAdmin)




class RegistrationAdmin(admin.ModelAdmin):
   list_display=['name','email','phone','address','country','city','region','code']


admin.site.register(Registration,RegistrationAdmin)




class feedbackAdmin(admin.ModelAdmin):
  list_display=['name','email','phone','satisfy','msg']


admin.site.register(feedback,feedbackAdmin)



class contactAdmin(admin.ModelAdmin):
  list_display=['name','email','message']

admin.site.register(contact,contactAdmin)

class artistfromAdmin(admin.ModelAdmin):
  list_display=['name','art','artname','age','Amount','Nationality','email','phone','image']

admin.site.register(artistfrom,artistfromAdmin)

class PaymentAdmin(admin.ModelAdmin):
  list_display=['name','cardname','email','address','city','pay_detail','cardno','cvc','phoneno','month','year','amount']

admin.site.register(Payment,PaymentAdmin)



