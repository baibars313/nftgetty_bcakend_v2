import numbers
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from PIL import Image
import requests
from rest_framework import status
import threading
import time
from django.db.models import F
from web3 import Web3

# Create your views here.

import time

current_time = int(time.time())


def homepage(request):

    # print)
    return render(request, 'Emails.html')

def proxy(request):
    return render(request, 'proxies.html')

def user(request):

    return render(request, 'users.html')
# baibars313Rajput


@api_view(['GET','POST'])
def allItems(request):
    if request.method=="GET":
        if request.GET.get("category") == 'all':
            all_auctions = Items.objects.filter(sold=False, auction=True,expiring__gt=current_time)
            allob = Items.objects.filter(sold=False, auction=False)

            combined_list = list(allob) + list(all_auctions)  # Concatenate the object lists

            serialized = Itemserializer(combined_list, many=True)
            return Response(serialized.data)

        else:
            cat=request.GET.get("category")
            all_auctions = Items.objects.filter(sold=False, auction=True, expiring__gt=current_time,category=cat)
            allob = Items.objects.filter(sold=False, auction=False,category=cat)

            combined_list = list(allob) + list(all_auctions)  # Concatenate the object lists

            serialized = Itemserializer(combined_list, many=True)
            return Response(serialized.data)

    if request.method=='POST':
        serializer=Itemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Item":"updated"})


@api_view(['GET','POST'])
def Allsales(request):
    if request.method=="GET":
        allob = Items.objects.filter(sold=True)
        serialized = Itemserializer( allob, many=True)
        return Response(serialized.data)

@api_view(['GET','POST'])
def AllAuctions(request):
    if request.method=="GET":
        allob = Items.objects.filter(auction=True)
        serialized = Itemserializer( allob, many=True)
        return Response(serialized.data)

@api_view(['GET','POST'])
def BidsAuctions(request):
    if request.method=="GET":
        allob = Bids.objects.all()
        serialized = Itemserializer( allob, many=True)
        return Response(serialized.data)



@api_view(['GET'])
def allItemsbyaddress(request):
    if request.method=="GET":
        cat=request.GET.get("address")
        print(cat)
        allob=Items.objects.filter(owner=cat)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def allItemsauction(request):
    if request.method=="GET":
        allob=Items.objects.filter(auction=True,sold=False,expiring__gt=current_time)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def allItemslicense(request):
    if request.method=="GET":
        allob=Items.objects.filter(license=True)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def allNotifications(request,user):
    if request.method=="GET":
        allob=Notifications.objects.filter(viewed=False,userAddress=user)
        serialized=Notificationserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET'])
def viewNotification(request,pk):
    if request.method=="GET":
        allob=Notifications.objects.get(id=pk)
        allob.viewed=True
        allob.save()
        return Response(serialized.data)
    else:
        return Response({"status":"no address id provided"})
@api_view(['GET'])
def NotificationHistory(request,user):
    if request.method=="GET":
        allob=Notifications.objects.filter(userAddress=user)
        serialized=Notificationserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})


@api_view(['GET','POST'])
def Adduser(request,cat):
    if request.method=="GET":
        allob=Userr.objects.get(address=cat)
        serialized=Useserilizer(allob, many=False)
        return Response(serialized.data)
    if request.method=='POST':
        try:
            allob=Userr.objects.get(address=cat)
            serializer=Useserilizer(instance=allob, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"update":"ok"})
        except:
            serializer=Useserilizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"creaded":"ok"})
            else:
                return Response({"not ok":"500"})
    else:
        return Response({"not ok":"500"})


@api_view(['GET'])
def All_users(request):
    allob=Userr.objects.all()
    serialized=Useserilizer(allob, many=True)
    return Response(serialized.data)



@api_view(['GET'])
def itemids(request):
    if request.method=='GET':
        cat=cat=request.GET.get("address")
        ids=Items.objects.filter(owner=cat).values('tokenId','chain')

        ids=str(ids).split('t ')[1].removesuffix('>').strip().replace("'",'''"''').replace('\\','')
        jsonid=json.loads(ids)
        print(ids)
        return Response({"ids":jsonid})


@api_view(['GET','POST'])
def getBids(request):
    if request.method=='GET':
        itemid=request.GET.get("itemid")
        chainid=request.GET.get("chainId")
        all_bids=Bids.objects.filter(itemId=itemid,chainId=chainid).order_by('-id')
        serialized=Bidserializer(all_bids, many=True)
        return Response(serialized.data)
    if request.method=='POST':
        serializer=Bidserializer(data=request.data)
        if serializer.is_valid():
            bid_object=serializer.save()
            notification = Notifications.objects.create(
                name=bid_object.name,
                description="Bid Recieved On an Auction with name " +bid_object.name,
                link=bid_object.link,
                userAddress=bid_object.userAddress,
                image=bid_object.image,
                amount=bid_object.amount,
                viewed=False
            )

            return Response({"update": "ok"})



@api_view(['GET','POST'])
def collections(request):
    if request.method=='POST':
        try:
            serializer=collectionserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"update":"ok"})
            else:
                return Response({"update":"failed"})
        except error as e:
            return Response({"error":f"{e}"})
        except:
            print("error")
    if request.method=='GET':
        contract=cat=request.GET.get("address")
        all_collections=collection.objects.get(contract=contract)
        serialized=collectionserializer(all_collections)
        return Response(serialized.data)
# biding start
@api_view(['POST','GET'])
def MakeBid(request):
    if request.method == 'POST':
        serializer = BidUnlistserializer(data=request.data)
        if serializer.is_valid():
            bid_object = serializer.save()
            try:
                notification = Notifications.objects.create(
                    name=f"A bid received on NFT ID #{bid_object.tokenId}",
                    description="Bid received on an on ulisted NFT click to check",
                    link=bid_object.link,
                    userAddress=bid_object.userAddress,
                    image=bid_object.image,
                    amount=bid_object.amount,
                    viewed=False
                )
                return Response({"update": "ok"})
            except Exception as e:
                return Response({"update": "error", "message": str(e)})
        else:
            return Response({"update": "error", "message": serializer.errors})

    else:
        return Response({"update": "error", "message": "Invalid request method."})





@api_view(['GET'])
def GetBids(request,contract,tokenid):
    all_collections=BidUnlist.objects.filter(contract=contract,tokenId=tokenid,closed=False)
    serialized=BidUnlistserializer(all_collections,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def GetFeaturedCollection(request):
    all_collections=FeaturedCollection.objects.all()
    serialized=FeaturedCollectionserializer(all_collections,many=True)
    return Response(serialized.data)


@api_view(['GET'])
def CloseBid(request,pk):
    bid=BidUnlist.objects.get(id=pk)
    bid.closed=True
    bid.save()
    return Response({"status":"ok"})
# biddin end

@api_view(['GET','POST'])
def Allcollections(request):
    if request.method=='GET':
        all_collections=collection.objects.all()
        serialized=collectionserializer(all_collections,many=True)
        return Response(serialized.data)

@api_view(['GET','POST'])
def collections_by_user(request,user):
    if request.method=='GET':
        all_collections=collection.objects.filter(owner=user)
        serialized=collectionserializer(all_collections,many=True)
        return Response(serialized.data)


@api_view(['GET','POST'])
def collection_by_user(request,user):
    if request.method=='GET':
        all_collections=collection.objects.get(owner=user)
        serialized=collectionserializer(all_collections)
        return Response(serialized.data)


@api_view(['GET','POST'])
def singlecollection(request,pk):
    if request.method=='POST':
        all_collections=collection.objects.get(id=pk)
        serializer=collectionserializer(instance=all_collections, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"ok 200"})
    else:
        all_collections=collection.objects.get(id=pk)
        serialized=collectionserializer(all_collections)
        return Response(serialized.data)


@api_view(['GET'])
def collectionLink(request,pk):
    all_collections=collection.objects.filter(contract=pk)
    collections=all_collections[0]
    serialized=collectionserializer(collections)
    return Response(serialized.data)


@api_view(['GET'])
def Blog(request,pk):
        all_collections=collection.objects.get(id=pk)
        collection=all_collections
        serialized=collectionserializer(collection)
        return Response(serialized.data)

@api_view(['GET'])
def Blogs(request):
        all_collections=collection.objects.all()
        collection=all_collections
        serialized=collectionserializer(collection,many=True)
        return Response(serialized.data)

@api_view(['GET','POST'])
def singleuser(request,user):
    if request.method=='GET':
        all_collections=Userr.objects.get(address=user)
        serialized=Useserilizer(all_collections)
        return Response(serialized.data)

@api_view(['GET','POST'])
def Onsale(request,contract,ItemId):
    if request.method=="GET":
        allob=Items.objects.get(contract_address=contract,tokenId=ItemId)
        serialized=Itemserializer(allob)
        return Response({"data":serialized.data})
    else:
        return Response({"status":"no address proverder"})

@api_view(['GET','POST'])
def Preview(request):
    return Response({"urls":'''
path('' ,homepage, name='home' ),
 path('allItems/' ,allItems, name='allItems' ),
 path('user/' ,Adduser, name='user' ),
 path('itemids/' ,itemids, name='ids' ),
 path('bid/' ,getBids, name='bids' ),
 path('onsale/' ,allItemsbyaddress, name='onsale' ),
 path('auctions/' ,allItemsauction, name='onsale' ),
 path('delete/' ,DeleteItems, name='onsales' ),
 path('license/' ,allItemslicense, name='onsale' ),
 path('create_get_collection/' ,collections, name='onsale1' ),
 path('all_collections/' ,Allcollections, name='onsale2' ),
 path('all_routes/' , Preview, name='onsale2' ),
  path('onsale/<str:contract>/<int:ItemId>' ,Onsale, name='onsale3' ),
    '''})

@api_view(['GET'])
def detail(request,pk):
    if request.method=="GET":
        allob=Items.objects.get(itemId=pk)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)

@api_view(['GET'])
def DeleteItems(request,pk):
    if request.method=="GET":
        obj=Items.objects.get(id=pk)
        obj.delete()
        return Response({"status":"deleted successfully"})

@api_view(['GET'])
def allItQuestions(request):
    if request.method=="GET":
        allob=Question.objects.all()
        serialized=Questionserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})


@api_view(['GET'])
def Question1(request,pk):
    if request.method=="GET":
        allob=Question.objects.get(id=pk)
        serialized=Questionserializer(allob)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})
@api_view(['GET','POST'])
def SolidItem(request,toke,itemid):
    if request.method=='POST':
        allob=Items.objects.filter(contract_address=toke,itemId=itemid)
        serializer=Itemserializer(instance=allob[0], data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"done"})
    else:
        allob=Items.objects.filter(contract_address=toke,itemId=itemid)
        serialized=Itemserializer(allob,many=True)
        return Response(serialized.data)

@api_view(['GET','POST'])
def allILicense(request):
    if request.method=="GET":
        allob=Items.objects.filter(license=True)
        serialized=Itemserializer(allob, many=True)
        return Response(serialized.data)
    else:
        return Response({"status":"no address proverder"})


@api_view(['GET','POST'])
def BaseFees(request):
    if request.method=="GET":
        allob=BaseFee.objects.get(id=1)
        serialized=BaseFeeserializer(allob)
        return Response(serialized.data)
    elif request.method=="POST":
        value=request.data.get('value')
        allob=BaseFee.objects.get(id=1)
        allob.amount=value
        allob.save()
        return Response({"status":"successFully updated"})
    else:
        return Response({"status":"no address proverder"})



@api_view(['GET','POST'])
def RewardView(request,pk):
    if reques.method=='POST':
        serializer=Rewardserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"creaded":"ok"})
    else:
        reward=Reawrd.objects.get(rewardId=pk)
        data=Rewardserializer(data)
        return Response(data)


@api_view(['GET','POST'])
def Ban(request,pk,objType):
    if request.method=="POST":
        if objType =='user':
            value=request.data.get('status')
            allob=Userr.objects.get(id=pk)
            allob.banned=value
            allob.save()
            return Response({"status":"successFully updated user"})
        else:
            value=request.data.get('status')
            allob=collection.objects.get(id=pk)
            allob.banned=value
            allob.save()
            return Response({"status":"successFully updated collection"})
    else:
        return Response({"status":"no address provirder","id":pk})




@api_view(['GET','POST'])
def Locations(request):
    if request.method=='POST':
        serializer=Locationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"creaded":"ok"})
    else:
        return Response({"creaded":"ok"})






