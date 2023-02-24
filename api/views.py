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
import threading
import time
# Create your views here.

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
        if request.GET.get("category")=='all':
            allob=Items.objects.filter(sold=False)
            serialized=Itemserializer(allob, many=True)
            return Response(serialized.data)
        else:
            cat=request.GET.get("category")
            print(cat)
            allob=Items.objects.filter(category=cat,sold=False)
            serialized=Itemserializer(allob, many=True)
            return Response(serialized.data)


    if request.method=="POST":
        serializer = Itemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"200"})



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
        allob=Items.objects.filter(auction=True)
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
            serializer.save()
            return Response({"update":"ok"})



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
def singlecollection(request,token):
    if request.method=='POST':
        all_collections=collection.objects.get(contract=token)
        serializer=collectionserializer(instance=all_collections, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"ok 200"})
    else:
        all_collections=collection.objects.get(contract=token)
        serialized=collectionserializer(all_collections)
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












