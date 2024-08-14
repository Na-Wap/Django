from django.urls import path
from . import views
urlpatterns = [
   path('index' ,views.index,name='index'),
   path('about' ,views.about,name='about'),
   path('add/<int:a>/<int:b>' ,views.add,name='add'),
   path('intro/<str:name>/<int:age>' ,views.intro,name='introS'),
   path('' ,views.home,name='home'),
   path('second' ,views.second,name='second'),
   path('third' ,views.third,name='third'),
   path('image' ,views.image,name='image'),
   path('myform' ,views.myform,name='myform'),
]
