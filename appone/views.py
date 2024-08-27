from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
import datetime
# import razorpay




# Create your views here.
def index(re):
   return render(re, 'index.html')
def details(re):
   return  render(re,'contact.html')
# def cusreg(re):
#    return  render(re,'customer_register.html')

 # def log(re):
#    return render(re,'login.html')
def registration(request):
   if request.method == 'POST':
      a = request.POST['name']
      b = request.POST['add']
      c = request.POST['phoneno']
      d = request.POST['email']
      e = request.POST['uname']
      f = request.POST['password']
      try:
         data = custreg.objects.create(name=a, address=b, phoneno=c, email=d, username=e, password=f)
         print(data)
         data.save()
         messages.success(request, "Registration success")
      except:
         messages.success(request, "Username already exists")
         return redirect(registration)

      return redirect(login)
   else:
      return render(request, 'customer_register.html')


def vendor_reg(request):
   if request.method == 'POST':
      a = request.POST['name']
      b = request.POST['compid']
      c = request.POST['address']
      d = request.POST['email']
      e = request.POST['lisence']
      f = request.POST['phoneno']
      g = request.POST['location']
      h = request.POST['uname']
      i = request.POST['password']


      print("success")
      try:

         data = venreg.objects.create(Company_Name=a,Company_id=b, Company_address=c, email=d, lisence=e, phoneno=f, location=g,uname=h,password=i,status='pending')
         print(data)
         data.save()
         messages.success(request,"Registration success")
      except:
         messages.success(request,"Username already exists")
         return redirect(vendor_reg)

      return redirect(login)
   else:
      return render(request,'Vendor_registration.html')


def login(request):
   if request.method == 'POST':
      username = request.POST['name']
      password = request.POST['password']
      try:
         data = custreg.objects.get(username=username)
         if data.password == password:
            request.session['user'] = username
            messages.success(request, "login success")

            return redirect(custhome)
         else:
            messages.error(request, "password incorrect")
            return redirect(login)
            # return HttpResponse("password incorrect")
      except Exception:
         try:
            data = venreg.objects.get(uname=username)
            if data.password == password:
               if data.status == "active":

                  request.session['com'] = username
                  messages.success(request, "login success")

                  return redirect(venhome)
               else:
                  if data.status =="pending":
                     messages.error(request, "waiting for approval")
                     return redirect(login)
                  else:
                     if data.status =="reject":
                        messages.error(request, "waiting for approval")
                        return redirect(login)

            else:
               messages.error(request, "password incorrect")
               return redirect(login)
         except Exception:
               if username == 'admin' and password == 'Admin@123':
                  request.session['admin'] = username
                  messages.success(request, "login success")
                  return redirect(adminhome)
               else:
                  messages.info(request, "username incorrect")
                  return redirect(login)
   else:

      return render(request, "login.html")


def logout(re):
   if '' in re.session:
      re.session.flush()
   return redirect(login)


def adminhome(request):
   return render(request, "adminhome.html")


def admincustdet(request):
   data = custreg.objects.all()
   return render(request, "admincustdet.html", {'data': data})


def adminvendet(request):
   data = venreg.objects.all()
   return render(request, "adminvendet.html", {'data': data})

def vendorpend(re):
   data = venreg.objects.filter(status="pending")
   return render(re, "vendor pend.html", {'data': data})
def venhome(re):
   return render(re, 'venhome.html')
def custhome(re):
   return render(re, 'custhome.html')


def pending1(re, id1):
   venreg.objects.filter(pk=id1).update(status='active')
   return redirect(vendorpend)
def rejecting(re, id1):
   venreg.objects.filter(id=id).update(status='reject')
   return redirect(vendorpend)

def products(request):
    return render(request,'venadd_procustview.html')

def custcontact(request):
   return render(request,'custcontact.html')

def venadd_product(request):
   return render(request,'venadd_product.html')

# def product(request):
#    if request.method =='POST':
#       a=request.POST['name']
#       b=request.POST['price']
#       c=request.POST['brand']
#       d=request.POST['description']
#       e=request.POST['image']
#       product=product.object.all()
#       return render(request,'venadd_procustview.html',{product:product})
   
def add_product(request):
   if request.method =='POST':
      A=request.POST['name']
      B=request.POST['price']
      C=request.POST['brand']
      E=request.FILES['image']
      D=request.POST['description']

      print("success")
      try:

         data=vendor.objects.create(vendorname=A,price=B,brand=C,image=E,description=D)
         print(data)
         data.save()
         messages.success(request,"product adding done")
      except:
         messages.success(request,"please fill all details")
         return redirect(add_product)

      # messages.success(request, "Product Add Successfully")
      return redirect(venhome)
   else:
      return render(request, 'venadd_product.html')

# def venadd_procustview(request):
#       return render(request, 'venadd_procustview.html')

def venadd_procustview(request):
   data = vendor.objects.all()
   return render(request, "venadd_procustview.html", {'data': data})

def booking(request):
   return render(request, "booking.html")

def confirm_booking(request):
   if request.method=='POST':
      p=request.POST['Location']
      q=request.POST['name']
      r=int(request.POST['phone'])
      s=int(request.POST['pin'])
      t=request.POST['Place']
      u=request.POST['State']
      v=int(request.POST['room'])
      w=request.POST['rname']
      x=int(request.POST['aphone'])
      y=request.POST['land']

      print("success")
      try:

         data=bookings.objects.create(location=p,name=q,phone_num=r,pin=s,city=t,state=u,BR_no=v,Road_name=w,Alt_phno=x,Landmark=y)
         data.save()
         messages.success(request,"Order Placed")
      except:
         messages.success(request,"please fill all details")
         return redirect(confirm_booking)
      return redirect(custhome)
   else:
      return render(request,'booking.html')


def addreviews(re):
   if 'user' in re.session:
      if re.method == 'POST':
         review = re.POST['feedback']
         brand_name = re.POST.get('Brand')
         user = custreg.objects.get(username=re.session['user'])
         d = Review.objects.create(user=user, review=review, Brand=brand_name)
         d.save()
         return render(re, 'index.html')
      else:
         return render(index)
   else:
      return render(login)


def uprofile(request):
   if 'user' in request.session:
      user = custreg.objects.get(username=request.session['user'])
      return render(request, "uprofile.html", {'user': user})


def edituser(req, id2):
   if req.method == 'POST':
      username = req.POST['username']
      user_email = req.POST['email']
      password = req.POST['password']
      mobile = req.POST['mobile']

      try:
         profimg = req.FILES['profile']
         custreg.objects.filter(pk=id2).update(username=username, email=user_email, password=password,
                                              phoneno=mobile, profile=profimg)
      except:
         custreg.objects.filter(pk=id2).update(username=username, email=user_email, password=password,
                                              phoneno=mobile)

      messages.success(req, "successfully updated")
      return redirect(uprofile)
   else:
      data = custreg.objects.get(pk=id2)
      return render(req, 'edituser.html', {'data': data})
