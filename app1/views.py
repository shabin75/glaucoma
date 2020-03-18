from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import DataForms
from .models import Data, Poster, Doctor, Patient, DoctorDetails
from .ai import testing
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.core.mail import send_mail
from glucoma.settings import EMAIL_HOST_USER
import numpy as np
import random
import string
import cv2
import os
import sys
from django.utils import timezone

now = timezone.now()

sys.path.insert(0, '/Users/shabin75/Desktop/btech/glucoma/keras-yolo3-glaucoma')
from yolo_video import detect_img
from yolo import YOLO


def home(request):
    if request.user.is_authenticated:
        if Doctor.objects.filter(user_id=request.user.id).exists():
            ob = Doctor.objects.get(user_id=request.user.id)
            return render(request, 'index.html', {'ob': ob})
        else:
            return render(request, 'index.html', {})
    else:
        return render(request, 'index.html', {})


def prediction(out):
    if out == 1:
        return "Healthy Eye"
    else:
        return "Glaucoma"


def test(request):
    if request.user.is_authenticated:
        out = ''
        test_img = ''
        form = DataForms(request.POST or None, request.FILES or None)
        post = Poster.objects.get(id=1)
        ## Data.objects.all().delete()
        if form.is_valid():
            im = form.cleaned_data['img']
            im = str(im)
            dir = 'media/pics'
            path = os.path.join(dir, im)
            form.save()
            i = cv2.imread(path)
            try:
                box = detect_img(YOLO(), path)
            except:
                box = None
            print(box)
            test_img = form.instance.img
            out = 'Sorry Try Another Image'
            if box is not None:
                test_im = cv2.rectangle(i, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
                cv2.imwrite('static/test_result.png', test_im)

                try:
                    out = testing(i)
                    out = prediction(out)
                    print(out)
                except Exception as e:
                    print(e)

            return render(request, 'test.html', {'out': out, 'post': post, 'test_img': test_img})
        return render(request, 'test.html', {'form': form,
                                             'out': out, 'post': post})
    else:
        messages.info(request, 'Login For Test your Eye')
        return redirect('app1:login')


def test1(request):
    if request.user.is_authenticated:
        form = DataForms(request.POST or None, request.FILES or None)
        out = ''
        test_img = ''
        post = Poster.objects.get(id=1)
        if request.method == 'POST':
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            age = request.POST.get('age')
            op = request.POST.get('op')
            blood = request.POST.get('blood')
            mob = request.POST.get('mob')
            description = request.POST.get('description')
            print(name, sex, op, blood, mob, description)
            ## Data.objects.all().delete()
            if form.is_valid():
                im = form.cleaned_data['img']
                im = str(im)
                dir = 'media/pics'
                path = os.path.join(dir, im)
                form.save()
                i = cv2.imread(path)
                try:
                    box = detect_img(YOLO(), path)
                except:
                    box = None
                print(box)
                test_img = form.instance.img
                out = 'Sorry Try Another Image'
                if box is not None:
                    test_im = cv2.rectangle(i, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
                    cv2.imwrite('static/test_result.png', test_im)

                    try:
                        out = testing(i)
                        out = prediction(out)
                        DoctorDetails.objects.create(name=name, sex=sex, op=op, blood=blood, mob=mob,
                                                     description=description, img=test_img, result=out,
                                                     doctorname=request.user, age=age, date=now)
                        print(out)
                    except Exception as e:
                        print(e)

                return render(request, 'test1.html', {'out': out, 'post': post, 'test_img': test_img})
        return render(request, 'test1.html', {'form': form,
                                              'out': out, 'post': post})
    else:
        messages.info(request, 'Login For Test your Eye')
        return redirect('app1:login')


def signup(request):
    return render(request, 'signupuser.html')


def doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        bday = request.POST['bday']
        gender = request.POST['gender']
        hospital = request.POST['hospital']
        email = request.POST['email']
        contact = request.POST['mob']
        username = request.POST['username']
        pword1 = request.POST['password1']
        pword2 = request.POST['password2']
        if pword1 == pword2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username is already taken')
                return redirect('app1:doctor')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'already register with this email')
                return redirect('app1:doctor')
            else:
                U = User.objects.create_user(username=username, password=pword1, email=email)
                Doctor.objects.create(user=U, name=name, doctor_Id=id, birth_day=bday, gender=gender, hospital=hospital,
                                      Contact=contact)
                auth.login(request, U)
                return redirect('app1:test1')


        else:
            messages.error(request, 'password and confirm password are incorrect')
            return redirect('app1:doctor')
    else:
        return render(request, 'signupdoctor.html')


def patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        bday = request.POST['bday']
        gender = request.POST['gender']
        email = request.POST['email']
        contact = request.POST['mob']
        username = request.POST['username']
        pword1 = request.POST['password1']
        pword2 = request.POST['password2']
        if pword1 == pword2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username is already taken')
                return redirect('app1:patient')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'already register with this email')
                return redirect('app1:patient')
            else:
                U = User.objects.create_user(username=username, password=pword1, email=email)
                Patient.objects.create(user=U, name=name, birth_day=bday, gender=gender,
                                       Contact=contact)
                auth.login(request, U)
                return redirect('app1:test')

        else:
            messages.error(request, 'password and confirm password are incorrect')
            return redirect('app1:patient')

    return render(request, 'signuppatient.html')


def log(request):
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['password']
        try:
            u = User.objects.get(email=e)
        except:
            u = None
        if u:
            uname = u.username
            user = auth.authenticate(username=uname, password=p)
            if user:
                auth.login(request, user)
                return redirect('app1:home')
            else:
                messages.info(request, 'Email or password incorrect')
                return redirect('app1:login')

        else:
            messages.info(request, 'Email or password incorrect')
            return redirect('app1:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('app1:home')


def forgot_password(request):
    if request.method == 'POST':
        subject = 'Mediplus'
        recipient = str(request.POST.get('email'))
        temp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        if User.objects.filter(email=recipient).exists():
            u = User.objects.get(email=recipient)
            u.set_password(temp)
            u.save()
            message = 'Hi..' + u.username + '\n' + 'Your password has been reset' + '\n' + 'And your new password is:' + temp + '\n' + 'Please login with this Password...' + '\n' + 'Thank you........'
            print(message)
            send_mail(subject,
                      message, EMAIL_HOST_USER, [recipient], fail_silently=False)

            messages.info(request, 'Message sent successfully')

            return redirect('app1:forgot')
        else:
            messages.info(request, 'No user is Register with this email')
            return redirect('app1:forgot')
    return render(request, 'forgot.html')


def detail(request):
    obj = DoctorDetails.objects.filter(doctorname_id=request.user.id)
    print(obj)
    return render(request, 'detail.html', {'obj': obj})


def delete(request, id):
    obj = get_object_or_404(DoctorDetails, id=id)
    obj.delete()
    return redirect('app1:detail')


def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            print(pass1,pass2)
            if pass1==pass2:
                u=User.objects.get(email=request.user.email)
                u.set_password(pass1)
                u.save()
                messages.info(request, 'password change successfully ')
                return redirect('app1:login')
            else:
                messages.error(request,'password incorrect')
        return render(request,'change_password.html')
    return redirect('app1:login')