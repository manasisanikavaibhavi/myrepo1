# """
# URL configuration for project1 project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from testapp import views

# urlpatterns =[
#     path('admin/', admin.site.urls),
#     path('test1/test', views.display),
#     path('lgn/', views.receive,name='lgn'),
#     path('test1/test1',views.start),
#     path('test1/exb/test1',views.start),
#     path('test1/',views.start),
#     path('coll/', views.receive,name='coll'),
#     path('test1/clt/test1',views.start),
#     path('test1/clt/abo',views.about),
#     path('test1/clt/cntc',views.present),
#     path('test1/clt/exb',views.exhibit),
#     path('test1/clt/clt',views.collect),
#     path('test1/abo/clt',views.collect),

    

    
    
#     path('test1/welcome/',views.show),
#     path('rg/',views.doreg,name='register'),
#     path('test1/welcome/clt',views.collect),
#     path('test1/welcome/ofr',views.myoffer),
#     path('test1/welcome/abo',views.about),
#     path('test1/welcome/cntc',views.present),
#     path('test1/welcome/exb',views.exhibit),
    


#     path('test1/fdbk/',views.clear),
#     path('rcv/',views.feed,name='feedback'),
#     path('abc/',views.feed,name='abc'),

#     path('test1/cntc/',views.present),
#     path('c/',views.com,name='c'),

#     path('test1/clt/cntc/',views.present), 

#     path('test1/ofr/',views.myoffer),
#     path('test1/ofr/abo',views.about),
#     path('test1/ofr/clt/',views.collect),
#     path('test1/ofr/exb',views.exhibit),
#     path('test1/exb',views.exhibit),
#     # path('test1/ofr/abo',views.about),
#     # path('test1/ofr/cntc',views.present),
#     # path('test1/ofr/test1',views.start),
    
#     path('test1/sprot1/',views.sprodut), 
#     path('test1/ofr/sprot1',views.sprodut),
#     path('test1/ofr/cart',views.mycart),
#     path('test1/ofr/pymt',views.makepayment),
    
#     path('pmt',views.dopayment,name="pmt"),

#     path('test1/clt/',views.collect),

#     path('test1/abo/',views.about),
#     path('test1/abo/test1',views.start),
#     path('test1/abo/ofr',views.myoffer),
#     path('test1/abo/cit',views.collect),
#     path('test1/abo/exb',views.exhibit),
#     path('test1/abo/abo',views.about),
#     path('test1/abo/cntc',views.present),
    
    


    
#     path('test1/exb /exb',views.exhibit),
#     path('test1/exb/abo',views.about),
#     path('test1/exb/cntc',views.present),
#     path('test1/exb/ofr',views.myoffer),
#     path('test1/exb/test1',views.start),
#     path('test1/exb/clt',views.collect),


#     path('test1/reiv/',views. review),
    
#     path('test1/exb/hellow/',views.art),
#     path('a/', views.artist,name='a'),
#     path('test1/hellow/abo',views.about),
#     path('test1/hellow/cntc',views.present),
#     path('test1/hellow/ofr',views.myoffer),
#     path('test1/hellow/test1',views.start),
#     path('test1/hellow/clt',views.collect),
    
    


#     path('rpt1/',views.repartist),
#     path('rpt2/',views.replogin),
#     path('rpt3/',views.repregister),
#     path('rpt4/',views.repcontact),
#     path('rpt5/',views.repfeedback),
#     path('test1/abo/paint',views.paintig),
#     path('test1/paint',views.paintig),
#     path('test1/clt/paint',views.paintig),
#     path('test1/radh',views.Radh),
#     path('test1/abo/radh',views.Radh),
#     path('test1/clt/radh',views.Radh),
#     path('test1/dool',views.paintig),
#     path('test1/clt/dool',views.dood),
#     path('test1/abo/dool',views.dood),
#     path('test1/ar',views.arch),
#     path('test1/clt/ar',views.arch),
#     path('test1/abo/ar',views.arch),
#     path('test1/scl',views.sculp),
#     path('test1/clt/scl',views.sculp),




    


    
# ]
# # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('test1/test', views.display),
    path('lgn/', views.receive,name='lgn'),
    path('test1/test1',views.start),
    path('test1/exb/test1',views.start),
    path('test1/',views.start),
    path('coll/', views.receive,name='coll'),
    path('test1/clt/test1',views.start),
    path('test1/clt/abo',views.about),
    path('test1/clt/cntc',views.present),
    path('test1/clt/exb',views.exhibit),
    path('test1/clt/clt',views.collect),
    path('test1/abo/clt',views.collect),

    

    
    
    path('test1/welcome/',views.show),
    path('rg/',views.doreg,name='register'),
    path('test1/welcome/clt',views.collect),
    path('test1/welcome/ofr',views.myoffer),
    path('test1/welcome/abo',views.about),
    path('test1/welcome/cntc',views.present),
    path('test1/welcome/exb',views.exhibit),
    


    path('test1/fdbk/',views.clear),
    path('rcv/',views.feed,name='feedback'),
    path('abc/',views.feed,name='abc'),

    path('test1/cntc/',views.present),
    path('c/',views.com,name='c'),

    path('test1/clt/cntc/',views.present), 

    path('test1/ofr/',views.myoffer),
    path('test1/ofr/abo',views.about),
    path('test1/ofr/clt/',views.collect),
    path('test1/ofr/exb',views.exhibit),
    path('test1/exb',views.exhibit),
    # path('test1/ofr/abo',views.about),
    # path('test1/ofr/cntc',views.present),
    path('test1/ofr/test1',views.start),
    
    path('test1/sprot1/',views.sprodut), 
    path('test1/ofr/sprot1',views.sprodut),
    path('test1/ofr/cart',views.mycart),
    path('test1/ofr/pymt',views.makepayment),
    path('test1/ofr/ofr',views.myoffer),
    path('test1/ofr/cntc',views.present),
    
    path('pmt',views.dopayment,name="pmt"),

    path('test1/clt/',views.collect),

    path('test1/abo/',views.about),
    path('test1/abo/test1',views.start),
    path('test1/abo/ofr',views.myoffer),
    path('test1/abo/cit',views.collect),
    path('test1/abo/exb',views.exhibit),
    path('test1/abo/abo',views.about),
    path('test1/abo/cntc',views.present),
    
    


    
    path('test1/exb/exb',views.exhibit),
    path('test1/exb/abo',views.about),
    path('test1/exb/cntc',views.present),
    path('test1/exb/ofr',views.myoffer),
    # path('test1/exb/test1',views.start),
    path('test1/exb/clt',views.collect),
    path('test1/exb/',views.exhibit),

    path('test1/reiv/',views. review),
    path('test1/hellow',views.art),
    path('test1/exb/hellow/',views.art),
    path('a/', views.artist,name='a'),
    path('test1/hellow/abo',views.about),
    path('test1/hellow/cntc',views.present),
    path('test1/hellow/ofr',views.myoffer),
    path('test1/hellow/test1',views.start),
    path('test1/hellow/clt',views.collect),
    path('test1/ofr/hellow/',views.art),
    path('test1/exb/paint',views.paintig),
    path('test1/exb/dool',views.dood),
    path('test1/exb/radh',views.Radh),
    path('test1/exb/ar',views.arch),
    path('test1/exb/scl',views.sculp),
    path('test1/exb/cart',views.mycart),
    path('test1/welcome',views.show),
    path('test1/welcome/test1',views.start),
    path('test1/welcome/welcome',views.show),
    path('test1/welcome/cart',views.mycart),
     
    path('test1/welcome/paint',views.paintig),
    path('test1/welcome/dool',views.dood),
    path('test1/welcome/radh',views.Radh),
    path('test1/welcome/ar',views.arch),
    path('test1/welcome/scl',views.sculp),
    path('test1/test',views.start),

    path('test/abo',views.about),
    path('test1/off',views.myoffer),
    path('test1/cart',views.mycart),
    

    path('rpt1/',views.repartist),
    path('rpt2/',views.replogin),
    path('rpt3/',views.repregister),
    path('rpt4/',views.repcontact),
    path('rpt5/',views.repfeedback),
    path('test1/abo/paint',views.paintig),
    path('test1/paint',views.paintig),
    path('test1/clt/paint',views.paintig),
    path('test1/radh',views.Radh),
    path('test1/abo/radh',views.Radh),
    path('test1/clt/radh',views.Radh),
    path('test1/dool',views.paintig),
    path('test1/clt/dool',views.dood),
    path('test1/abo/dool',views.dood),
    path('test1/ar',views.arch),
    path('test1/clt/ar',views.arch),
    path('test1/abo/ar',views.arch),
    path('test1/scl',views.sculp),
    path('test1/clt/scl',views.sculp),
    path('test1/ofr/fdbk',views.start),
    



    


    
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)