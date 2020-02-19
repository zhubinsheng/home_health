from django.shortcuts import render, redirect, HttpResponse
from backstage.models import UserInfo, mhealth, paymoneyin, lendmoneyin, borrowmoneyin
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
import json

msg = ''


def getBackstage(request):
    response = 0
    if request.method == 'GET':
        crruentUser = request.user.username
        if crruentUser:
            if UserInfo.objects.get(username=crruentUser).is_active:
                user_all_information = UserInfo.objects.all()
                name = crruentUser
                response = render(request, 'account.html',
                                  {'username': name, 'user_all_information': user_all_information})
            else:
                response = redirect('/')
        else:
            tips = "请先登录"
            response = redirect('/', locals())
    else:
        response = redirect('/')
    return response


def userLoginOut(request):
    crruentUser = request.user.username
    if crruentUser:
        if UserInfo.objects.get(username=crruentUser).is_active:
            logout(request)
            return redirect('/')
        else:
            return redirect('/', locals())
    else:
        return redirect('/')


def getUserInformation(request, name):
    if request.is_ajax():
        crruentUser = request.user.username
        if crruentUser:
            if UserInfo.objects.get(username=crruentUser).is_active:
                try:
                    if name == 'currentUser':
                        user_all_information = UserInfo.objects.get(username=crruentUser)
                    else:
                        user_all_information = UserInfo.objects.get(username=name)
                    information = {}
                    information['introduction'] = user_all_information.introduction
                    information['qq'] = user_all_information.qq
                    information['phone'] = user_all_information.phone
                    information['username'] = user_all_information.username
                    information['email'] = user_all_information.email
                    information['first_name'] = user_all_information.first_name
                    return HttpResponse(json.dumps(information))
                except Exception as e:
                    print(e)
                    return HttpResponse('bad request 500')
            else:
                return redirect('/', locals())
        else:
            return redirect('/')
    else:
        return HttpResponse('bad request 500')


def getUserInfo(request):
    global msg

    if request.method == 'GET':
        crruentUser = request.user.username
        if crruentUser:
            if UserInfo.objects.get(username=crruentUser).is_active:
                userinfo = UserInfo.objects.get(username=crruentUser)
                msg = ''
                return render(request, 'userinfo.html', {'userinfo': userinfo, 'msg': msg})
            else:
                return redirect('/', locals())
        else:
            return redirect('/')
    elif request.is_ajax() or request.method == 'POST':
        crruentUser = request.user.username
        if crruentUser:
            user = UserInfo.objects.get(username=crruentUser)
            change_info = request.POST
            for key, value in change_info.items():
                if key != "csrfmiddlewaretoken":
                    try:
                        if key == 'password':
                            exec('user.' + key + '="' + str(make_password(value)) + '"')
                        else:
                            exec('user.' + key + '="' + value + '"')
                    except Exception as e:
                        print(e)
                        msg = "修改失败"
            try:
                user.save()
                msg = '修改成功'
            except Exception as e:
                print(e)
                msg = "修改失败 " + str(e)
            return render(request, 'userinfo.html', locals())
        else:
            return redirect('/')
    else:
        return HttpResponse('bad request 500')


def addmoney(request):
    if request.method == 'GET':
        moneyInfo_List = mhealth.objects.all()
        return render(request, 'addmoney.html', {'moneyInfo_List': moneyInfo_List})
    if request.method == 'POST':


    # mhealth.objects.create(weight=weight, blood_pressure=blood_pressure, routine_blood_test=routine_blood_test)

        edit_publisher = mhealth.objects.get(id=1)
        edit_publisher.weight = request.POST.get('weight')
        edit_publisher.blood_pressure = request.POST.get('blood_pressure')
        edit_publisher.routine_blood_test = request.POST.get('routine_blood_test')

        if len(edit_publisher.weight) == 0:
            moneyInfo_List = mhealth.objects.all()
            return render(request, 'addmoney.html', {'moneyInfo_List': moneyInfo_List})

        if len(edit_publisher.blood_pressure) == 0:
            moneyInfo_List = mhealth.objects.all()
            return render(request, 'addmoney.html', {'moneyInfo_List': moneyInfo_List})

        if len(edit_publisher.routine_blood_test) == 0:
            moneyInfo_List = mhealth.objects.all()
            return render(request, 'addmoney.html', {'moneyInfo_List': moneyInfo_List})

        edit_publisher.save()  # 把修改提交到数据库

        moneyInfo_List = mhealth.objects.all()
        return render(request, 'addmoney.html', {'moneyInfo_List': moneyInfo_List})
    else:
        return HttpResponse('bad request 500')


def paymoney(request):
    if request.method == 'GET':
        moneyInfo_List = paymoneyin.objects.all()
        return render(request, 'paymoney.html', {'moneyInfo_List': moneyInfo_List})
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        paymoneyin.objects.create(amount=name, article=password, creatUser=email, datetime=repassword)
        moneyInfo_List = paymoneyin.objects.all()
        return render(request, 'paymoney.html', {'moneyInfo_List': moneyInfo_List})
    else:
        return HttpResponse('bad request 500')


def borrowmoney(request):
    if request.method == 'GET':
        moneyInfo_List = borrowmoneyin.objects.all()
        return render(request, 'borrowmoney.html', {'moneyInfo_List': moneyInfo_List})
    if request.method == 'POST':
        weight = request.POST.get('weight')
        blood_pressure = request.POST.get('blood_pressure')
        routine_blood_test = request.POST.get('routine_blood_test')
        name = request.user.username
        data = request.POST.get('data')

        if len(weight) == 0:
            moneyInfo_List = borrowmoneyin.objects.all()
            return render(request, 'borrowmoney.html', {'moneyInfo_List': moneyInfo_List})
        if len(routine_blood_test) == 0:
            moneyInfo_List = borrowmoneyin.objects.all()
            return render(request, 'borrowmoney.html', {'moneyInfo_List': moneyInfo_List})
        if len(blood_pressure) == 0:
            moneyInfo_List = borrowmoneyin.objects.all()
            return render(request, 'borrowmoney.html', {'moneyInfo_List': moneyInfo_List})

        rel_edit_publisher = mhealth.objects.get(id=1)
        rel_weight = rel_edit_publisher.weight
        rel_blood_pressure = rel_edit_publisher.blood_pressure
        rel_routine_blood_test = rel_edit_publisher.routine_blood_test

        strlist = rel_weight.split('-')
        if int(weight) < int(strlist[0]):
            weight = weight + '  偏低'
        elif int(weight) > int(strlist[1]):
            weight = weight + '  偏高'

        strlist2 = rel_blood_pressure.split('-')
        if int(blood_pressure) < int(strlist2[0]):
            blood_pressure = blood_pressure + '  偏低'
        elif int(blood_pressure) > int(strlist2[1]):
            blood_pressure = blood_pressure + '  偏高'

        strlist3 = rel_routine_blood_test.split('-')
        if float(routine_blood_test) < float(strlist3[0]):
            routine_blood_test = routine_blood_test + '  偏低'
        elif float(routine_blood_test) > float(strlist3[1]):
            routine_blood_test = routine_blood_test + '  偏高'



        borrowmoneyin.objects.create(amount=weight, article=blood_pressure, creatUser=routine_blood_test, datetime=data, name=name)
        moneyInfo_List = borrowmoneyin.objects.all()
        return render(request, 'borrowmoney.html', {'moneyInfo_List': moneyInfo_List})
    else:
        return HttpResponse('bad request 500')


def lendmoney(request):
    if request.method == 'GET':
        moneyInfo_List = lendmoneyin.objects.all()
        return render(request, 'lendmoney.html', {'moneyInfo_List': moneyInfo_List})
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        lendmoneyin.objects.create(amount=name, article=password, creatUser=email, datetime=repassword)
        moneyInfo_List = lendmoneyin.objects.all()
        return render(request, 'lendmoney.html', {'moneyInfo_List': moneyInfo_List})
    else:
        return HttpResponse('bad request 500')


def getMessage(request):
    global msg

    if request.is_ajax():
        crruentUser = request.user.username
        if crruentUser:
            return HttpResponse(msg)
        else:
            return HttpResponse('bad request 500')
    else:
        return HttpResponse('bad request 500')


def delUser(request, name):
    if request.is_ajax():
        crruentUser = request.user.username
        if crruentUser:
            if name.upper() != crruentUser.upper():
                if UserInfo.objects.get(username=crruentUser).is_superuser:
                    try:
                        UserInfo.objects.get(username=name).delete()
                        msg = '删除成功'
                        return HttpResponse(msg)
                    except Exception as e:
                        msg = '删除失败' + str(e)
                        return HttpResponse(msg)
                else:
                    msg = '你没有权限'
                    return HttpResponse(msg)
            else:
                msg = '不能删除自己'
                return HttpResponse(msg)
        else:
            return HttpResponse('bad request 500')
    else:
        return HttpResponse('bad request 500')
