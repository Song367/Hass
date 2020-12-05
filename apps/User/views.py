#coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from ..log.models import TemporaryLogin, FormalLogin
from django.contrib.auth.models import User
from ..User.models import Users
from ..User.forms import UserForm


@login_required
def info(request):
    if request.method == 'GET':
        # print(request.COOKIES['username'])
        # print(User.username)
        return render(request, 'test.html',{'name':request.COOKIES['username']})
    else:
        big_cat = request.POST.get('big_cats')
        mid_cat = request.POST.get('mid_cats')
        small_cat = request.POST.get('small_category')
        site = request.POST.get('sites')
        price = request.POST.get('prices')
        resident = request.POST.get('residents')
        department = request.POST.get('department')
        localpeople = request.POST.get('localpeople')
        align_item = request.POST.get('align_items')
        maintain_item = request.POST.get('maintain_items')
        image = request.FILES.get('image')
        datasheet = request.FILES.get('datasheet')
        drawings = request.FILES.get('drawings')
        operation_manaul = request.FILES.get('operation_manaul')

        ss = request.COOKIES['username']

        usr_obj = User.objects.get(username=ss)

        temporary = TemporaryLogin.objects.create(

            big_category=big_cat,
            mid_category=mid_cat,
            small_category=small_cat,
            site=site,
            price=price,
            Resident=resident,
            department=department,
            LocalPeople=localpeople,
            align=align_item,
            maintain=maintain_item,
            images=image,
            Specifications=datasheet,
            Drawing=drawings,
            operation=operation_manaul
        )
        temporary.user_id.add(usr_obj)
        # usr_obj.temporarylogin_set.add(temporary)
        temporary.save()
        # usr_obj.save()
        return render(request, 'test.html')


def Login(request):
    error_msg = ''
    if request.method == 'GET':

        return render(request, 'login_out/login.html')
    else:

        # userform = UserForm(request.POST)
        # #print(userform)
        # if userform.is_valid():
        #     username = userform.cleaned_data['name']
        #     password = userform.cleaned_data['password']
        #     print(username, password)
        #     user = authenticate(name=username,password=password)
        #     if user:
        #         login(request, user)
        #         response=redirect(request.GET.get("next", '/info/'))
        #         response.set_cookie('username',username,max_age=7*24*3600)
        #         return response  # 登录成功后就跳转
        #     else:
        #         print(user)
        #         error_msg = '用户名或者密码错误'
        #     return render(request, "login_out/login.html", {'error': error_msg})
        # return HttpResponse('error')

        username = request.POST.get('name')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            response = redirect(request.GET.get("next", '/info/'))
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
            return response  # 登录成功后就跳转
        else:
            print(user)
            error_msg = '用户名或者密码错误'
        return render(request, "login_out/login.html", {'error': error_msg})
        # return HttpResponse('error')


def Logout(request):
    logout(request)
    return redirect('/login/')


def trans_temporary(request):
    user = request.COOKIES['username']
    User_obj = User.objects.get(username=user)
    data = list(TemporaryLogin.objects.filter(user_id=User_obj).values())
    return JsonResponse({'data': data})


# 决裁通过
def Tem_decision(request):
    user = request.COOKIES['username']
    ids = request.POST.getlist('ids')
    print(ids)
    if user == '10000':
        user_obj = User.objects.get(username='10001')
        for i in ids:
            tem_obj = TemporaryLogin.objects.get(id=i)
            user_obj.temporarylogin_set.add(tem_obj)
        user_obj.save()
    elif user == '10001':
        user_obj = User.objects.get(username='10002')
        for i in ids:
            tem_obj = TemporaryLogin.objects.get(id=i)
            user_obj.temporarylogin_set.add(tem_obj)
        user_obj.save()
    elif user == '10002':
        user_obj = User.objects.get(username='10003')
        for i in ids:
            tem_obj = TemporaryLogin.objects.get(id=i)
            user_obj.temporarylogin_set.add(tem_obj)
        user_obj.save()
    elif user == '10003':
        # user_obj = User.objects.get(username='10003')
        for i in ids:
            tem_obj = TemporaryLogin.objects.get(id=i)
            tem_obj.state = 1
            tem_obj.status = 2
            tem_obj.save()

    return JsonResponse('ok', safe=False)


# 决裁驳回

def Refused(request):
    ids = request.POST.getlist('ids')
    for i in ids:
        tem = TemporaryLogin.objects.get(id=i)
        tem.state = 2
        tem.status = 4
        tem.save()

    return JsonResponse('ok', safe=False)


# 确定进入正式登录
def Decision_Formal(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    if request.method=='POST':
        id = request.POST.get('idd')
        print(id)
        Asset_number = request.POST.get('asset_number')
        A_S = request.POST.get('a_s')
        supplier = request.POST.get('supplier')
        Manufacturer = request.POST.get('manufacturer')
        S_N = request.POST.get('s_n')
        p_o = request.POST.get('place_origin')
        confirmation = request.FILES.get('confirmation')
        special = request.POST.get('special')
        print(Asset_number, A_S, supplier, Manufacturer, S_N, p_o, confirmation)
        print(special)

        user_obj = User.objects.get(username='10000')

        Formal_obj = FormalLogin.objects.create(asset_number=Asset_number,
                                                A_S=A_S,
                                                supplier=supplier,
                                                manufacturer=Manufacturer,
                                                S_N_Code=S_N,
                                                place_origin=p_o,
                                                special=special,
                                                confirmation=confirmation)
        tem_obj = TemporaryLogin.objects.get(id=id)
        Formal_obj.temporarylogin_set.add(tem_obj)
        Formal_obj.save()
        Formal_obj.user_id.add(user_obj)
        Formal_obj.save()

        return render(request, 'test.html')


def tran_Formal(request):
    user_obj=User.objects.get(username=request.COOKIES['username'])
    FormalData=[]
    for j in FormalLogin.objects.filter(user_id=user_obj):

        FormalData.append(list(j.temporarylogin_set.values()))
    state={}
    status_sc={}
    for i in FormalLogin.objects.filter(user_id=user_obj):
        state[i.id]=i.state
        status_sc[i.id]=i.status_sc

    return JsonResponse({'FormalData':FormalData,'state':state,'status_sc':status_sc})


def For_decision(request):
    user = request.COOKIES['username']
    ids = request.POST.getlist('ids')
    print(ids)
    if user == '10000':
        user_obj = User.objects.get(username='10001')
        for i in ids:
            for_obj = FormalLogin.objects.get(id=i)
            for_obj.examine_stage=2
            for_obj.save()
            user_obj.formallogin_set.add(for_obj)
        user_obj.save()
    elif user == '10001':
        user_obj = User.objects.get(username='10002')
        for i in ids:
            for_obj = FormalLogin.objects.get(id=i)
            for_obj.examine_stage = 3
            for_obj.save()
            user_obj.formallogin_set.add(for_obj)
        user_obj.save()
    elif user == '10002':
        user_obj = User.objects.get(username='10003')
        for i in ids:
            for_obj = FormalLogin.objects.get(id=i)
            for_obj.examine_stage = 4
            for_obj.save()
            user_obj.formallogin_set.add(for_obj)
        user_obj.save()
    elif user == '10003':
        # user_obj = User.objects.get(username='10003')
        for i in ids:
            for_obj = FormalLogin.objects.get(id=i)
            for_obj.state = 1
            for_obj.status_sc = 3
            for_obj.save()
        return JsonResponse({'status':1})
    return JsonResponse('ok',safe=False)


def For_refuse(request):
    ids = request.POST.getlist('ids')
    for i in ids:
        For = FormalLogin.objects.get(id=i)
        For.state = 2
        For.status_sc = 4
        For.save()
    return JsonResponse('ok',safe=False)



import logging
logger=logging.getLogger('django')
logging.info('请求成功')
logging.error('请求错误')
