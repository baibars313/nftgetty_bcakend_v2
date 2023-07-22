from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Netuser, Deposit, Trade, Order, Withdrawl,Link
from .serializers import NetuserSerializer, DepositSerializer, TradeSerializer, OrderSerializer, WithdrawlSerializer,LinkSerializer
from rest_framework import status
from django.db.models import Sum,Value,DecimalField
from decimal import Decimal
from django.db.models.functions import Coalesce
from web3 import Web3
from rest_framework.views import APIView
from .web3_utils import web3
import time
@api_view(['GET', 'POST'])
def netuser_list(request):
    if request.method == 'GET':
        netusers = Netuser.objects.all()
        serializer = NetuserSerializer(netusers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        wa = request.POST.get('wallet')  # Fix the typo here, it should be request.POST
        serializer = NetuserSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.wallet = wa
            instance.save()
            return Response({'wallet': wa}, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def netuser_detail(request, pk):
    try:
        netuser = Netuser.objects.get(pk=pk)
    except Netuser.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = NetuserSerializer(netuser)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NetuserSerializer(netuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        netuser.delete()
        return Response(status=204)




@api_view(['POST'])
def create(request):
    refral = request.data.get('parent_refral', '')
    user_id = request.data.get('user_id', '')
    my_refral = request.data.get('my_refral', '')
    levels = my_refral.split('-')

    if len(levels) >= 4:
        level_1 = levels[3]
        level_2 = levels[2]
        level_3 = levels[1]
        level_4 = levels[0]
        wa = request.data.get('wallet', '')  # Use request.data instead of request.POST

        if wa:  # Check if wallet is provided and not empty
            netuser = Netuser(
                user_id=user_id,
                level_1=level_1,
                level_2=level_2,
                level_3=level_3,
                level_4=level_4,
                my_refral=my_refral,
                wallet=wa
            )
            netuser.save()

            serializer = NetuserSerializer(netuser)
            return Response(serializer.data, status=201)
        else:
            return Response({'error': 'Wallet is required'}, status=400)

    return Response({'error': 'Invalid format for referral'}, status=400)

@api_view(['GET', 'POST'])
def deposit_list(request):
    if request.method == 'GET':
        deposits = Deposit.objects.filter(confirmed=False)
        serializer = DepositSerializer(deposits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_id = request.data.get('user_id')
        pending_deposits = Deposit.objects.filter(user_id=user_id, confirmed=False)

        if not pending_deposits:
            serializer = DepositSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"error":"already have pending request"}, status=400)

# Deposit by user
@api_view(['GET'])
def deposit_by_user(request,user_id):
    if request.method == 'GET':
        deposits = Deposit.objects.filter(user_id=user_id,confirmed=False)
        serializer = DepositSerializer(deposits, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def deposit_detail(request, pk):
    try:
        deposit = Deposit.objects.get(pk=pk)
    except Deposit.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        deposit.confirmed=True
        deposit.save()
        return Response({"status":"200 ok"})
    elif request.method == 'PUT':
        serializer = DepositSerializer(deposit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        deposit = Deposit.objects.get(pk=pk)
        if not deposit.confirmed:
            deposit.delete()
            return Response(status=204)
        else:
            return Response(status=404)

# Trade views
@api_view(['GET', 'POST'])
def trade_list(request):
    if request.method == 'GET':
        trades = Trade.objects.filter(disable=False)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def trade_detail(request, pk):
    if request.method == 'POST':
        trade = Trade.objects.get(id=pk)
        trade.disable = True
        trade.save()
        return Response({"message": "Trade disabled."})




# Order views
@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def balance_util(user_id):
    current_time = int(time.time())  # Get current Unix timestamp

    # Filter Netuser by level_1
    netuser_objects_lv1 = Netuser.objects.filter(level_1=user_id)

    # Calculate the sum of 'level_1' field in Order for each Netuser instance
    total_sum_lv1 = netuser_objects_lv1.aggregate(total_amount=Coalesce(Sum('order__level_1', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_2
    netuser_objects_lv2 = Netuser.objects.filter(level_2=user_id)

    # Calculate the sum of 'level_2' field in Order for each Netuser instance
    total_sum_lv2 = netuser_objects_lv2.aggregate(total_amount=Coalesce(Sum('order__level_2', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_3
    netuser_objects_lv3 = Netuser.objects.filter(level_3=user_id)

    # Calculate the sum of 'level_3' field in Order for each Netuser instance
    total_sum_lv3 = netuser_objects_lv3.aggregate(total_amount=Coalesce(Sum('order__level_3', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_4
    netuser_objects_lv4 = Netuser.objects.filter(level_4=user_id)

    # Calculate the sum of 'level_4' field in Order for each Netuser instance
    total_sum_lv4 = netuser_objects_lv4.aggregate(total_amount=Coalesce(Sum('order__level_4', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Calculate the sum of all levels combined
    total_sum_all = total_sum_lv1 + total_sum_lv2 + total_sum_lv3 + total_sum_lv4

    # Calculate the sum of confirmed deposits for the user
    deposit_sum = Deposit.objects.filter(user_id=user_id, confirmed=True).aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)

    # Calculate the sum of withdrawals for the user
    withdrawal_sum = Withdrawl.objects.filter(user_id=user_id, confirmed=True).aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)

    # Filter Order by user_id and ending_time < current time
    current_time = int(time.time())
    orders = Order.objects.filter(user_id=user_id, ending_time__gt=current_time)
    order_sum = orders.aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)
    completed_order_sum=Order.objects.filter(user_id=user_id, ending_time__lt=current_time)
    # Calculate the sum of personal commissions from the filtered orders
    commission_sum = completed_order_sum.aggregate(total_amount=Sum('personal_commision'))['total_amount'] or Decimal(0)

    # Calculate the current balance by adding the deposits, commissions, and total sums, and subtracting the withdrawals
    current_balance = float(deposit_sum) + float(total_sum_all) + float(commission_sum) - float(withdrawal_sum) - float(order_sum)
    tota_commission=float(total_sum_all) + float(commission_sum)

    # Return the user's current balance
    return  current_balance


@api_view(['GET'])
def Getbalance(request,user_id):
    bal=balance_util(user_id)
    return Response({'bal':bal})

# order creation balance counting
@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        try:
            # Retrieve values from the request data
            user_id = request.data.get('user_id')
            user=Netuser.objects.get(pk=user_id)
            trade_id = request.data.get('trade_id')
            amount = request.data.get('amount')
            balance=balance_util(user_id)
            starting_time = request.data.get('starting_time')
            ending_time = request.data.get('ending_time')

            # Validate input values if necessary

            # Retrieve trade percentage and calculate commission amount
            trade = Trade.objects.get(id=trade_id)
            trade_percentage = trade.percentage
            commission_amount = (trade_percentage / 100) * float(amount)
            lv1=(10/ 100) * float(commission_amount)
            lv2=(6/ 100) * float(commission_amount)
            lv3=(2/ 100) * float(commission_amount)
            lv4=(2/ 100) * float(commission_amount)
            personal_commision=commission_amount-(lv1+lv2+lv3+lv4)
            market_commision=lv1+lv2+lv3+lv4
            # Create a new Order object
            if float(balance)>=float(amount):
                order = Order(
                user_id=user,
                trade_id=trade_id,
                amount=amount,
                commission=commission_amount,
                starting_time=starting_time,
                ending_time=ending_time,
                level_1=lv1,
                level_2=lv2,
                level_3=lv3,
                level_4=lv4,
                personal_commision=personal_commision,
                market_comission=market_commision

                    )

            # Save the order to the database
                order.save()

            # Serialize the order data for the response
                serializer = OrderSerializer(order)

            # Return a JSON response with the serialized order data
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Not enough balance'}, status=status.HTTP_400_BAD_REQUEST)



        except Trade.DoesNotExist:
            return Response({'error': 'Trade not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET'])
def balance(request, user_id):
    current_time = int(time.time())  # Get current Unix timestamp

    # Filter Netuser by level_1
    netuser_objects_lv1 = Netuser.objects.filter(level_1=user_id)

    # Calculate the sum of 'level_1' field in Order for each Netuser instance
    total_sum_lv1 = netuser_objects_lv1.aggregate(total_amount=Coalesce(Sum('order__level_1', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_2
    netuser_objects_lv2 = Netuser.objects.filter(level_2=user_id)

    # Calculate the sum of 'level_2' field in Order for each Netuser instance
    total_sum_lv2 = netuser_objects_lv2.aggregate(total_amount=Coalesce(Sum('order__level_2', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_3
    netuser_objects_lv3 = Netuser.objects.filter(level_3=user_id)

    # Calculate the sum of 'level_3' field in Order for each Netuser instance
    total_sum_lv3 = netuser_objects_lv3.aggregate(total_amount=Coalesce(Sum('order__level_3', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Filter Netuser by level_4
    netuser_objects_lv4 = Netuser.objects.filter(level_4=user_id)

    # Calculate the sum of 'level_4' field in Order for each Netuser instance
    total_sum_lv4 = netuser_objects_lv4.aggregate(total_amount=Coalesce(Sum('order__level_4', output_field=DecimalField()), Value(Decimal(0), output_field=DecimalField())))['total_amount']

    # Calculate the sum of all levels combined
    total_sum_all = total_sum_lv1 + total_sum_lv2 + total_sum_lv3 + total_sum_lv4

    # Calculate the sum of confirmed deposits for the user
    deposit_sum = Deposit.objects.filter(user_id=user_id, confirmed=True).aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)

    # Calculate the sum of withdrawals for the user
    withdrawal_sum = Withdrawl.objects.filter(user_id=user_id, confirmed=True).aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)

    # Filter Order by user_id and ending_time < current time
    current_time = int(time.time())
    orders = Order.objects.filter(user_id=user_id, ending_time__gt=current_time)
    order_sum = orders.aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal(0)
    completed_order_sum=Order.objects.filter(user_id=user_id, ending_time__lt=current_time)
    # Calculate the sum of personal commissions from the filtered orders
    commission_sum = completed_order_sum.aggregate(total_amount=Sum('personal_commision'))['total_amount'] or Decimal(0)

    # Calculate the current balance by adding the deposits, commissions, and total sums, and subtracting the withdrawals
    current_balance = float(deposit_sum) + float(total_sum_all) + float(commission_sum) - float(withdrawal_sum) - float(order_sum)
    tota_commission=float(total_sum_all) + float(commission_sum)

    # Return the user's current balance
    return Response({"current_balance": current_balance,'withdrawl':float(withdrawal_sum),'desposits':float(deposit_sum),'total_revnue':tota_commission,"order_sum":order_sum,"my_order_commission":commission_sum})

# balanc util



# commission
@api_view(['GET'])
def get_commision(request, user_id):
    # Filter Netuser by level_1
    current_time = int(time.time())  # Get current Unix timestamp

    # Filter Netuser by level_1
    netuser_objects_lv1 = Netuser.objects.filter(level_1=user_id)

    # Calculate the sum of 'level_1' field in Order for each Netuser instance
    total_sum_lv1 = netuser_objects_lv1.aggregate(total_amount=Coalesce(Sum('order__level_1', output_field=DecimalField()), Value(0, output_field=DecimalField())))['total_amount']

    # Get all Order objects filtered by level_1 and ending_time < current_time
    orders_lv1 = Order.objects.filter(user_id__in=netuser_objects_lv1, ending_time__lt=current_time)

    # Serialize the Order objects
    serializer_lv1 = OrderSerializer(orders_lv1, many=True)

    # Filter Netuser by level_2
    netuser_objects_lv2 = Netuser.objects.filter(level_2=user_id)

    # Calculate the sum of 'level_2' field in Order for each Netuser instance
    total_sum_lv2 = netuser_objects_lv2.aggregate(total_amount=Coalesce(Sum('order__level_2', output_field=DecimalField()), Value(0, output_field=DecimalField())))['total_amount']

    # Get all Order objects filtered by level_2 and ending_time < current_time
    orders_lv2 = Order.objects.filter(user_id__in=netuser_objects_lv2, ending_time__lt=current_time)

    # Serialize the Order objects
    serializer_lv2 = OrderSerializer(orders_lv2, many=True)

    # Filter Netuser by level_3
    netuser_objects_lv3 = Netuser.objects.filter(level_3=user_id)

    # Calculate the sum of 'level_3' field in Order for each Netuser instance
    total_sum_lv3 = netuser_objects_lv3.aggregate(total_amount=Coalesce(Sum('order__level_3', output_field=DecimalField()), Value(0, output_field=DecimalField())))['total_amount']

    # Get all Order objects filtered by level_3 and ending_time < current_time
    orders_lv3 = Order.objects.filter(user_id__in=netuser_objects_lv3, ending_time__lt=current_time)

    # Serialize the Order objects
    serializer_lv3 = OrderSerializer(orders_lv3, many=True)

    # Filter Netuser by level_4
    netuser_objects_lv4 = Netuser.objects.filter(level_4=user_id)

    # Calculate the sum of 'level_4' field in Order for each Netuser instance
    total_sum_lv4 = netuser_objects_lv4.aggregate(total_amount=Coalesce(Sum('order__level_4', output_field=DecimalField()), Value(0, output_field=DecimalField())))['total_amount']

    # Get all Order objects filtered by level_4 and ending_time < current_time
    orders_lv4 = Order.objects.filter(user_id__in=netuser_objects_lv4, ending_time__lt=current_time)

    # Serialize the Order objects
    serializer_lv4 = OrderSerializer(orders_lv4, many=True)

    # Calculate the sum of all levels combined
    total_sum_all = total_sum_lv1 + total_sum_lv2 + total_sum_lv3 + total_sum_lv4

    # Return the sums and serialized Order objects
    return Response({
        "sum_lv1": total_sum_lv1,
        "sum_lv2": total_sum_lv2,
        "sum_lv3": total_sum_lv3,
        "sum_lv4": total_sum_lv4,
        "sum_all_levels": total_sum_all,
        "orders_lv1": serializer_lv1.data,
        "orders_lv2": serializer_lv2.data,
        "orders_lv3": serializer_lv3.data,
        "orders_lv4": serializer_lv4.data,

    })




@api_view(['GET'])
def pending_order_list(request,user_id):
    if request.method == 'GET':
        current_time = int(time.time())  # Get current Unix timestamp

        # Retrieve orders where current time is less than end_time
        orders = Order.objects.filter(ending_time__gt=current_time,user_id=user_id)

        # Serialize the order data for the response
        serializer = OrderSerializer(orders, many=True)

        # Return a JSON response with the serialized order data
        return Response(serializer.data)


@api_view(['GET'])
def completed_order_list(request,user_id):
    if request.method == 'GET':
        current_time = int(time.time())  # Get current Unix timestamp

        # Retrieve orders where ending_time is less than current time
        orders = Order.objects.filter(ending_time__lt=current_time,user_id=user_id)

        # Serialize the order data for the response
        serializer = OrderSerializer(orders, many=True)

        # Return a JSON response with the serialized order data
        return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=204)


# Withdrawl views
@api_view(['GET', 'POST'])
def withdrawl_list(request):
    if request.method == 'GET':
        withdrawls = Withdrawl.objects.filter(confirmed=False)
        serializer = WithdrawlSerializer(withdrawls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WithdrawlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def withdrawl_detail(request, pk):
    try:
        withdrawl = Withdrawl.objects.get(pk=pk)
    except Withdrawl.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = WithdrawlSerializer(withdrawl)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WithdrawlSerializer(withdrawl, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        withdrawl = Withdrawl.objects.get(pk=pk)
        if not withdrawl.confirmed:
            withdrawl.delete()
            return Response(status=204)

@api_view(['POST'])
def create_withdrawl(request,user_id):
 # Assuming the user is authenticated
    amount = request.data.get('amount')
    balance=balance_util(user_id)
    if float(balance)>=float(amount):
        user=Netuser.objects.get(pk=user_id)
        if amount is None:
            return Response({'error': 'Amount is required.'}, status=400)

        withdrawl = Withdrawl.objects.create(user_id=user, amount=amount)
        serializer = WithdrawlSerializer(withdrawl)
        return Response(serializer.data, status=201)
    else:
        return Response({'error': 'not enough balance.'}, status=400)


@api_view(['POST'])
def confirm_withdrawl(request,pk):
    draw= Withdrawl.objects.get(id=pk)
    draw.confirmed=True
    draw.save()
    return Response({"go":"fuck your self"})




@api_view(['GET'])
def user_withdrawls(request,user_id):
    # Assuming the user is authenticated
    withdrawls = Withdrawl.objects.filter(user_id=user_id,confirmed=False)
    serializer = WithdrawlSerializer(withdrawls, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_deposits(request,user_id):
    # Assuming the user is authenticated'
    withdrawls = Deposit.objects.filter(user_id=user_id)
    serializer = DepositSerializer(withdrawls, many=True)
    return Response(serializer.data)
# soicl media links

@api_view(['GET', 'POST'])
def link_list(request):
    if request.method == 'GET':
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def edit_link(request, pk):
    link = get_object_or_404(Link, pk=pk)

    if request.method == 'GET':
        serializer = LinkSerializer(link)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LinkSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)





# Define the ABI of the smart contract
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "userDetails",
        "outputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "total_withdraw",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "total_deposit",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
@api_view(['GET'])
def UserDetailsView(request,user_id):
        # Contract address
    contract_address = '0xe43f418F51E9245a320ce3F0d4dC7Ede1C91D476'

        # Create the contract instance
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

        # Call the smart contract function to read user details
    result = contract.functions.userDetails(user_id).call()


        # Format the data for the API response
    user_details = {
            'userAddress': result[0],
            'total_withdraw': float(result[1]),
            'total_deposit': float(result[2])
        }

    return Response(user_details)

