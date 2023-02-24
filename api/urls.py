from django.urls import path
from .views import *
urlpatterns = [
 path('' ,homepage, name='home' ),
 path('allItems/' ,allItems, name='allItems' ),
 path('user/<str:cat>/' ,Adduser, name='user' ),
 path('itemids/' ,itemids, name='ids' ),
 path('bid/' ,getBids, name='bids' ),
 path('onsale/' ,allItemsbyaddress, name='onsale' ),
 path('auctions/' ,allItemsauction, name='onsale' ),
 path('delete/' ,DeleteItems, name='onsales' ),
 path('license/' ,allItemslicense, name='onsale' ),
 path('create_get_collection/' ,collections, name='onsale1' ),
 path('all_collections/' ,Allcollections, name='onsale2' ),
 path('all_collections_by_user/<str:user>/' ,collections_by_user, name='onsale4' ),
 path('all_collection_by_user/<str:user>/' ,collection_by_user, name='onsale5' ),
 path('all_routes/' , Preview, name='onsale2' ),
 path("all_users/",All_users),
 path("share/",user),
#  singlecollection
 path('collection/<str:token>/' , singlecollection, name='single_collection' ),
 path('singleuser/<str:user>/',singleuser),
 path('onsale/<str:contract>/<int:ItemId>' ,Onsale, name='onsale3' ),
#  allItQuestions allILicense
 path('questions/' ,allItQuestions, name='allItQuestions' ),
 path('licenses/' ,allILicense ),
 path('sell/<str:toke>/<int:itemid>/' ,SolidItem ),
 path('question/<int:pk>/' ,Question1, name='Question' ),
]