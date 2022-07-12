from django.shortcuts import render, get_object_or_404 , reverse
from django.http import HttpResponseRedirect, Http404
from . models import user , Product  ,Meat
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from main.models import order, orderitem, Shippingaddress
from  django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
#---- view


def home2(request):
    return render(request,'admins_/Home.html')
def home3(request):
    return render(request, 'frontend/home2.html')


def isearch(request):
     term = request.GET.get('search','')
     user_list =user.objects.filter(Q (user_fname__icontains=term) | Q(user_lname__icontains=term)).order_by('-id')

     return render(request, 'admins_/index.html', {'user_list': user_list})

 #--- meat search

def search(request):
    term = request.GET.get('search','')
    m_list = Meat.objects.filter(Q(m_name__icontains=term)).order_by('-id')

    return render(request, 'admins_/products.html', {'m_list': m_list}  )

# pancit search

def psearch(request):
    term = request.GET.get('psearch','')
    pro_list = Product.objects.filter(Q(pro_name__icontains=term)).order_by('-id')

    return render(request, 'admins_/products.html', {'pro_list': pro_list}  )


def accounts(request):
    user_list = user.objects.order_by('pub_date')
    context = {'user_list': user_list}

    return render(request, 'admins_/index.html', context)


def ship(request):
    ships = Shippingaddress.objects.all()
    shipcounts =   ships.count()
    context = {'ships': ships, 'shipcounts':shipcounts}

    return render(request, 'admins_/Foodorders.html', context)




def show(request):
    user_list = user.objects.order_by('pub_date')
    context = {'user_list': user_list}

    return render(request, 'admins_/index.html', context)


# adding new user

def Processadd(request):

    
    uid = request.POST.get('uid')
    
    position = request.POST.get('position')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    uname = request.POST.get('uname')
    pword = request.POST.get('pword')
    start = request.POST.get('start')


    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile/image.jpg'
    try:                                                                                                        
        n = user.objects.get(user_username=uname)

        return render(request, 'admins_/account.html', { 'error_message': "This Username " + uname +  "already exist"})

    except ObjectDoesNotExist:
        users = user.objects.create(user_uid=uid, user_username=uname, user_position=position, user_fname=fname, user_lname=lname
                                    ,pub_date=start, user_password=pword,user_image=user_pic)
        users.save()

        return HttpResponseRedirect('/backend/accounts')



#delete details
def deletes(request, user_id):
    user.objects.filter(id=user_id).delete()
    return HttpResponseRedirect('/backend/accounts')

#edits

def edits(request, user_id):
    try:
        users = user.objects.get(pk=user_id)

    except user.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'admins_/edit.html', {'users': users})

def proccessedit(request, user_id):
    users = get_object_or_404(user, pk=user_id)
    profile_pic = request.FILES.get('image')
    try:

        position = request.POST.get('position')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')

    except (KeyError, user.DoesNotExist):
        return render(request,'admins_/detail.html', {
            'users':users,
            'error_message': "There is a problem on updating the record"
        })
    else:
        user_profile =user.objects.get(id=user_id)
        user_profile.user_position = position
        user_profile.user_fname = fname
        user_profile.user_lname = lname
        user_profile.user_uname = uname
        user_profile.user_password = pword
        if profile_pic:
            user_profile.user_image = profile_pic
        user_profile.save()
        return HttpResponseRedirect(reverse('backend:detail', args=(user_id, )))


def detail(request, user_id):
    try:
        users = user.objects.get(pk=user_id)

    except user.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'admins_/detail.html', {'users': users})


#----- add products

def productshow(request):
        pro_list = Product.objects.order_by('pro_id')
        m_list = Meat.objects.order_by('m_id')

        context = {'pro_list': pro_list, 'm_list': m_list}

        return render(request, 'admins_/products.html', context)



# THIS IS FOR THE MEAT PRODUCT ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Meatprocess(request):
    mid = request.POST.get('pid')
    mname = request.POST.get('proname')
    mprice = request.POST.get('price')
    mcategory = request.POST.get('cat')
    msize = request.POST.get('size')

    if request.FILES.get('image'):
        mpro_pic = request.FILES.get('image')
    else:
        mpro_pic = 'profile/image.jpg'
    try:
        n = Meat.objects.get(m_id=mid)

        return render(request, 'forms/addpancit.html', {'error_message': "This product " + mid +""+ mname + "already exist"})

    except ObjectDoesNotExist:
        users = Meat.objects.create(m_id=mid, m_name=mname, m_price=mprice, m_cat=mcategory, m_size=msize
                                       , m_image=mpro_pic)
        users.save()

        return HttpResponseRedirect(reverse('backend:products'))


# meat edits --------------------------------------------------------------------------->>>>>

def mdetail(request, meat_id):
    try:
        meats = Meat.objects.get(pk=meat_id)

    except Meat.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'admins_/mdetail.html', {'meats': meats})


# delete details
def mdelete(request, meat_id):
    Meat.objects.filter(id=meat_id).delete()
    return HttpResponseRedirect(reverse('backend:products'))


# edits

def medit(request, meat_id):
    try:
        meats = Meat.objects.get(pk=meat_id)

    except Meat.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'forms/meatedit.html', {'meats': meats})


def mproccessedit(request, meat_id):
    meats = get_object_or_404(Meat, pk=meat_id)
    profile_pic = request.FILES.get('image')
    try:
        mid = request.POST.get('pid')
        mname = request.POST.get('proname')
        mprice = request.POST.get('price')
        mcategory = request.POST.get('cat')
        msize = request.POST.get('size')

    except (KeyError, user.DoesNotExist):
        return render(request, 'admins_/mdetail.html', {
            'meats': meats,
            'error_message': "There is a problem on updating the record"
        })
    else:
        meat_profile = Meat.objects.get(id=meat_id)
        meat_profile.m_id = mid
        meat_profile.m_name = mname
        meat_profile.m_price = mprice
        meat_profile.m_cat = mcategory
        meat_profile.m_size = msize
        if profile_pic:
            meat_profile.m_image = profile_pic
        meat_profile.save()
        return HttpResponseRedirect(reverse('backend:mdetail', args=(meat_id, )))


#------------------------------------------------ product pancit--------------
    
def Productprocess(request):
    id= request.POST.get('pid')
    name = request.POST.get('proname')
    price = request.POST.get('price')
    category = request.POST.get('cat')
    size = request.POST.get('size')


    if request.FILES.get('image'):
        pro_pic = request.FILES.get('image')
    else:
        pro_pic = 'profile/image.jpg'
    try:
        n =Product.objects.get(pro_id=id)

        return render(request, 'forms/addpancit.html',{ 'error_message': "This product " + id +  "already exist"})

    except ObjectDoesNotExist:
        users = Product.objects.create(pro_id=id, pro_name=name, pro_price=price,  Catergoty=category, pro_size=size
                                    ,pro_image=pro_pic)
        users.save()

        return HttpResponseRedirect(reverse('backend:products'))



#------------------- Pancit Editing ---------



def pdetails(request, pancit_id):
    try:
        pancit = Product.objects.get(pk=pancit_id)

    except Product.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'admins_/pdetail.html', {'pancit': pancit})


# delete details
def pdelete(request,pancit_id):
    Product.objects.filter(id=pancit_id).delete()
    return HttpResponseRedirect(reverse('backend:products'))


# edits

def pedit(request, pancit_id):
    try:
        pancit = Product.objects.get(pk=pancit_id)

    except Productprocess.DoesNotExist:
        raise Http404("This user does not exist!!")

    return render(request, 'forms/pancitedit.html', {'pancit': pancit})


def pproccessedit(request, pancit_id):
    pancit = get_object_or_404(Product, pk=pancit_id)
    profile_pic = request.FILES.get('image')
    try:
        id = request.POST.get('pid')
        name = request.POST.get('proname')
        price = request.POST.get('price')
        category = request.POST.get('cat')
        size = request.POST.get('size')

    except (KeyError, Productprocess.DoesNotExist):
        return render(request, 'admins_/pdetail.html', {
            'pancit': pancit,
            'error_message': "There is a problem on updating the record"
        })
    else:
        pancit_profile = Product.objects.get(id=pancit_id)
        pancit_profile.m_id = id
        pancit_profile.m_name = name
        pancit_profile.m_price = price
        pancit_profile.Catergoty = category
        pancit_profile.m_size = size
        if profile_pic:
            pancit_profile.pro_image = profile_pic
        pancit_profile.save()
        return HttpResponseRedirect(reverse('backend:pdetails', args=(pancit_id, )))


##----------- Login
def loginview(request):
    return render(request, 'forms/login.html')


def Loginprocess(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:

        login(request, user)
        return HttpResponseRedirect('/backend/home')
    else:

        return render(request, 'admins_/Home.html', {
            'error_message': "Incorrect password or Email please enter the correct information"
        })


def processlogout(request):
    logout(request)
    return HttpResponseRedirect('/backend/')


def home(request):
    ships = Shippingaddress.objects.all()
    shipcounts = ships.count()
    context = {'ships': ships, 'shipcounts': shipcounts}
    return render(request,'modal/confirmdelete.html', context)

def procesingorders(request):
    return render(request,'admins_/proccessing.html')
def food_orders(request):
    return render(request, 'admins_/Foodorders.html')
def add(request):
    return render(request, 'admins_/account.html')


def meatpage(request):
    return render(request, 'forms/addmeat.html')
def pancitpage(request):
    return render(request, 'forms/addpancit.html')




