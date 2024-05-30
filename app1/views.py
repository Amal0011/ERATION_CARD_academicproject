import ctypes
from dis import dis
from http.client import HTTPResponse


from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie
# from matplotlib.pyplot import xlim
# from matplotlib.style import use
# from numpy import append
from .models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import random







def LoginPage(request):
    return render(request,'indexpage.html',{})

def Newindex(request):
    return render(request,'regindex.html',{})
def AdminHome(request):
    return render(request,'admin/adminhome.html',{})
def Regshop(request):
    return render(request,'Shop_reg.html',{})
def SaveStore(request):
    sname=request.GET.get("fname")
    pan=request.GET.get("pan")
    phone=request.GET.get("phone")
    dist=request.GET.get("dist")
    ardno=request.GET.get("ardno")
    ccnt=request.GET.get("ccnt")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    
    print(sname,"\n",pan,"\n",phone,"\n",dist,"\n",ardno,"\n",ccnt,"\n",uname,"\n",pswrd)
    try:
        ob=Shop_reg(Sname=sname,Panchayth=pan,Phone=phone,Ardno=ardno,District=dist,Cardcount=ccnt,Username=uname,Password=pswrd)
        ob.save()
        data={"status":1}
  
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)

def Regauto(request):
    lang=request.session["lang"]
    return render(request,'Auto_reg.html',{"lang":lang})


def Saveauto(request):
    sname=request.GET.get("fname")
    vnum=request.GET.get("vnum")
    phone=request.GET.get("phone")
    addr=request.GET.get("addr")
    lat=request.GET.get("lat")
    longg=request.GET.get("longg")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    print(sname,"\n",vnum,"\n",phone,"\n",addr,"\n",lat,"\n",longg,"\n",uname,"\n",pswrd)
    try:
        ob=Auto_reg(Name=sname,Vnumber=vnum,Phone=phone,Address=addr,Latitude=lat,Longitude=longg,Username=uname,Password=pswrd)
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)


def Regcustomer(request):
    return render(request,'Customer_reg.html',{})
def Savecustomer(request):
    sname=request.GET.get("fname")
    utyp=request.GET.get("utyp")
    phone=request.GET.get("phone")
    addr=request.GET.get("addr")
    rnum=request.GET.get("rnum")
    nfm=request.GET.get("nfm")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")


    print(sname,"\n",utyp,"\n",phone,"\n",addr,nfm,"\n",rnum,"\n","\n",uname,"\n",pswrd)
    try:
        ob=Customer_reg(Name=sname,Cardno=rnum,Phone=phone,Address=addr,Cardtype=utyp,No_fm=nfm,Username=uname,Password=pswrd)
        ob.save()
        data={"status":1}
   
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)

def UpdateShopuser(request):
    uid=request.GET.get("uid")
    sname=request.GET.get("fname")
    ardno=request.GET.get("ardno")
    phone=request.GET.get("phone")
    pan=request.GET.get("pan")
    dist=request.GET.get("dist")
    ccnt=request.GET.get("ccnt")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")


    print(sname,"\n",ardno,"\n",phone,"\n",pan,"\n",dist,"\n",ccnt,"\n",uname,"\n",pswrd)
    
    try:
        ob=Shop_reg.objects.get(id=uid)
        ob.Sname=sname
        ob.Ardno=ardno
        ob.Phone=phone
        ob.Panchayth=pan
        ob.District=dist
        ob.Cardcount=ccnt
        ob.Username=uname
        ob.Password=pswrd

 
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        print(uid)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)
def DeleteShopuser(request):
    uid=request.GET.get("qid")
    print(uid)
    try:
        ob=Shop_reg.objects.get(id=uid)
        ob.delete()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except:
        data={"status":0}
        return JsonResponse(data,safe=False)

def CheckLogin(request):
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    utype=request.GET.get("utype")
    print(uname,pswrd,utype)
    print(uname,pswrd,utype)
    if(utype=='admin' and uname=="admin@admin.com" and pswrd=="admin"):
        data={"status":3}
        return JsonResponse(data,safe=False)
    elif(utype=='shop'):
        try:
            ob=Shop_reg.objects.get(Username=uname,Password=pswrd)
            
            request.session["usernm"]=uname
            data={"status":11}
            return JsonResponse(data,safe=False)
        except:
            data={"status":0}
            return JsonResponse(data,safe=False)
    
    elif(utype=='customer'):
        try:
            ob=Customer_reg.objects.get(Username=uname,Password=pswrd)
            request.session["usernm"]=uname
            data={"status":31}
            return JsonResponse(data,safe=False)
        except:
            data={"status":0}
            return JsonResponse(data,safe=False)
    else:
        data={"status":0}
        return JsonResponse(data,safe=False)




def Adminviewstore(request):
    ob1=Shop_reg.objects.all()
    return render(request,'admin/Admin_view_store.html',{"data2":ob1})

def Add_to_stock(request):
    return render(request,'admin/add_to_stock.html',{})


def Addstock(request):
    utype=request.GET.get("utype")
    riceqt=request.GET.get("riceqt")
    ricepc=request.GET.get("ricepc")
    ricestk=request.GET.get("ricestk")
    
    whtqt=request.GET.get("whtqt")
    whtpc=request.GET.get("whtpc")

    whtstk=request.GET.get("whtstk")
    keroqt=request.GET.get("keroqt")
    keropc=request.GET.get("keropc")
    kerostk=request.GET.get("kerostk")
    
    ataqt=request.GET.get("ataqt")
    atapc=request.GET.get("atapc")
    atastk=request.GET.get("atastk")
    dte=request.GET.get("dte")
    dtelist=dte.split("/")
    mnth=dtelist[1]
    if(len(mnth)==1):
        mnth="0"+mnth
    year=dtelist[2]
    print("month and year",mnth,year)
    print(utype,"\n",riceqt,"\n",ricepc,"\n",ricestk,"\n",whtqt,"\n",whtpc,"\n",whtstk,keroqt,"\n",keropc,
    "\n",kerostk,"\n",ataqt,"\n",atapc,atastk,"\n",dte)
    try:
        ob=Stock_table.objects.get(Card_type=utype,Month=mnth,Year=year)
        
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        ob=Stock_table(Card_type=utype,Riceqt=riceqt,Riceprc=ricepc,Ricestck=ricestk,Whtqt=whtqt,Whtprc=whtpc,
        Whtstck=whtstk,Keroqt=keroqt,Keroprc=keropc,Kerostck=kerostk,Ataqt=ataqt,Ataprc=atapc,Atastck=atastk,Month=mnth,Year=year
        )
        ob.save()
        data={"status":0}
        return JsonResponse(data,safe=False)

def View_stock(request):
    return render(request,'admin/View_stock.html',{})


def Get_stock(request):
    utype=request.GET.get("utype")
    mnth=request.GET.get("mnth")
    
    dtelist=mnth.split("-")
    mnth=dtelist[1]
    if(len(mnth)==1):
        mnth="0"+mnth
    year=dtelist[0]
    print("month and year",mnth,year)
    print(utype)
    try:
        ob=Stock_table.objects.get(Card_type=utype,Month=mnth,Year=year)
        datalist=[]
        
        datalist.append(ob.id)
        datalist.append(ob.Riceqt)
        datalist.append(ob.Riceprc)
        datalist.append(ob.Ricestck)
        datalist.append(ob.Whtqt)
        datalist.append(ob.Whtprc)
        datalist.append(ob.Whtstck)
        datalist.append(ob.Keroqt)
        datalist.append(ob.Keroprc)
        datalist.append(ob.Kerostck)
        datalist.append(ob.Ataqt)
        datalist.append(ob.Ataprc)
        datalist.append(ob.Atastck)
    
        print(datalist)
        data={"status":datalist}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        
        data={"status":0}
        return JsonResponse(data,safe=False)




def Update_stock(request):
    pid=request.GET.get("pid")
    riceqt=request.GET.get("riceqt")
    ricepc=request.GET.get("ricepc")
    ricestk=request.GET.get("ricestk")
    
    whtqt=request.GET.get("whtqt")
    whtpc=request.GET.get("whtpc")

    whtstk=request.GET.get("whtstk")
    keroqt=request.GET.get("keroqt")
    keropc=request.GET.get("keropc")
    kerostk=request.GET.get("kerostk")
    
    ataqt=request.GET.get("ataqt")
    atapc=request.GET.get("atapc")
    atastk=request.GET.get("atastk")
    
   
  
    print(pid,"\n",riceqt,"\n",ricepc,"\n",ricestk,"\n",whtqt,"\n",whtpc,"\n",whtstk,keroqt,"\n",keropc,
    "\n",kerostk,"\n",ataqt,"\n",atapc,atastk,"\n")
    try:
        ob=Stock_table.objects.get(id=int(pid))
        ob.Riceqt=riceqt
        ob.Riceprc=ricepc
        ob.Ricestck=ricestk
        ob.Whtqt=whtqt
        ob.Whtprc=whtpc
        ob.Whtstck=whtstk
        ob.Keroqt=keroqt
        ob.Keroprc=keropc
        ob.Kerostck=kerostk
        ob.Ataqt=ataqt
        ob.Ataprc=atapc
        ob.Atastck=atastk
        ob.save()
                
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        
        data={"status":0}
        return JsonResponse(data,safe=False)









def Get_products(request):
    ob=Stock_table.objects.all()
    datalist=[]
    for i in ob:
        data={}
        data["pid"]=i.id
        data["ctyp"]=i.Card_type
        data["riceqt"]=i.Riceqt
        data["riceprc"]=i.Riceprc
        data["ricestck"]=i.Ricestck
        data["whtqt"]=i.Whtqt
        data["whtprc"]=i.Whtprc

        data["whtstck"]=i.Whtstck
        data["cat"]=i.Keroqt
        data["subcat"]=i.Keroprc
        data["price"]=i.Kerostck
        data["info"]=i.Ataqt
        data["stock"]=i.Ataprc
        data["price"]=i.Atastck
        data["info"]=i.Month
        data["stock"]=i.Year
        datalist.append(data)
    print("data")
    return JsonResponse(datalist,safe=False)




def Admin_view_history(request):
    ob=Purchase_table.objects.all()
    return render(request,'admin/admin_history.html',{"data":ob})


def Shophome(request):
    uname=request.session["usernm"]
    print(uname)
    ob=Shop_reg.objects.get(Username=uname)
    rtng=ob.Rating
    Name=ob.Sname
    return render(request,'shop/Shop_home.html',{"name":Name,"rating":rtng})


def Shop_stock(request):
    uname=request.session["usernm"]
    print(uname)
    ob=Shop_reg.objects.get(Username=uname)
    Name=ob.Sname
    rtng=ob.Rating
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    ob2=Stock_table.objects.filter(Month=month,Year=year)
    return render(request,'shop/stock_table.html',{"name":Name,"data":ob2,"rating":rtng})

def Customerhome(request):
    return render(request,'customer/Customerhome.html',{})
def View_stores(request):
    return render(request,'customer/CustomerShop.html',{})


def Get_my_shops(request):
    dist=request.GET.get("dist")
    
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    datalist=[]
    resp={}
    
    print(dist)
    print(resp)
    ob=Shop_reg.objects.filter(District=dist)
    for i in ob:
        data=[]
        data.append(i.id)
        data.append(i.Sname)
        data.append(i.Panchayth)
        data.append(i.Rating)
        datalist.append(data)
    resp["datalist"]=datalist
    print(datalist)
    return JsonResponse(resp,safe=False)

def Selected_shop(request):
    # shid=request.POST.get("idno")
    return render(request,'customer/CustomerShop.html',{})


def Get_shop_id(request):
    sid=request.GET.get("qid")
    request.session["shid"]=sid
    uname=request.session["usernm"]
    print(sid)
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    resp={}
    if(len(month)==1):
        month="0"+month
    print(uname)
    print(year)
    print(month)
    try:
        ob=Purchase_table.objects.get(usid=uname,month=month,year=year)
        resp["msg"]="yes"
    except:
        resp["msg"]=0
    print(resp)
    
    return JsonResponse(resp,safe=False)

def Buy_ration(request):
    uname=request.session["usernm"]
    print(uname)
    ob=Customer_reg.objects.get(Username=uname)
    Ctyp=ob.Cardtype
    Nofm=ob.No_fm
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    ob2=Stock_table.objects.filter(Card_type=Ctyp,Month=month,Year=year)
    obcnt=ob2.count()
    relist=[]
    if(obcnt!=0):
        for i in ob2:
            rqt=int(i.Riceqt)*int(Nofm)
            wqt=int(i.Whtqt)*int(Nofm)
            relist.append(str(rqt)+" kg") 
            relist.append(i.Riceprc)
            relist.append(str(wqt)+" kg") 
            relist.append(i.Whtprc)
            relist.append(i.Keroqt+" Litre") 
            relist.append(i.Keroprc)
            relist.append(i.Ataqt+" kg") 
            relist.append(i.Ataprc)
    else:
        relist.append("Nil") 
        relist.append("Nil")
        relist.append("Nil") 
        relist.append("Nil")
        relist.append("Nil") 
        relist.append("Nil")
        relist.append("Nil") 
        relist.append("Nil")

    # shid=request.POST.get("idno")
    return render(request,'customer/Buy_ration.html',{"data":relist})

def Save_my_ration(request):
    riceqt=request.GET.get("riceqt")
    whtqt=request.GET.get("whtqt")
    keroqt=request.GET.get("keroqt")
    ataqt=request.GET.get("ataqt")
   
    print(riceqt)
    print(whtqt)
    print(keroqt)
    print(ataqt)
    li1=[]
    li1.append(riceqt)
    li1.append(whtqt)
    li1.append(keroqt)
    li1.append(ataqt)
    request.session["rationlist"]=li1
    
    try:
       
        data={"status":1}
        return JsonResponse(data,safe=False)

    except:
        data={"status":0}
        return JsonResponse(data,safe=False)


def Bill_page(request):
    li1=request.session["rationlist"]
    uname=request.session["usernm"]
    print("li1",li1)
    print(uname)
    ob=Customer_reg.objects.get(Username=uname)
    Ctyp=ob.Cardtype
    Nofm=ob.No_fm
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    ob2=Stock_table.objects.filter(Card_type=Ctyp,Month=month,Year=year)

    relist=[]
    for i in ob2:
        rqty=li1[0]
        rprc=i.Riceprc
        rtot=int(rqty)*int(i.Riceprc)
        relist.append(rprc)
        relist.append(rqty) 
        
        relist.append(rtot) 

        wqty=li1[1]
        wprc=i.Whtprc
        wtot=int(wqty)*int(wprc)
        relist.append(wprc)
        relist.append(wqty) 
        
        relist.append(wtot) 

        kqty=li1[2]
        kprc=i.Keroprc
        ktot=int(kqty)*int(kprc)
        relist.append(kprc)
        relist.append(kqty) 
        
        relist.append(ktot) 

        aqty=li1[2]
        aprc=i.Ataprc
        atot=int(aqty)*int(aprc)
        relist.append(aprc)
        relist.append(aqty) 
        
        relist.append(atot) 

        gtot=rtot+ktot+wtot+atot
        relist.append(gtot) 
    request.session["cartlist"]=relist
    print("relist",relist)
    return render(request,'customer/Bill_page.html',{"data":relist})





def buy_product(request):
    shid=request.session["shid"]
    obs=Shop_reg.objects.get(id=int(shid))
    shname=obs.Sname
    uname=request.session["usernm"]
    relist=request.session["cartlist"]
    print(shid)
    print(shname)
    print(uname)
    print(relist)
    pnumber = random.randint(1000,9999)
    print(pnumber)
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    request.session["pcode"]=pnumber
    try:

        ob1=Purchase_table(shopid=shid,shopname=shname,
        usid=uname,Riceqt=relist[0],Riceprc=relist[2],Whtqt=relist[3],Whtprc=relist[5],Keroqt=relist[6],Keroprc=relist[8],
        Ataqt=relist[9],Ataprc=relist[11],total=relist[12],month=month,year=year,purchasecode=pnumber)
        ob1.save()
        resp={"msg":1}
    except:

        resp={"msg":0}
    return JsonResponse(resp,safe=False)



def Pcode(request):
    pcode=request.session["pcode"]
    
    return render(request,'customer/pcode.html',{"data":pcode})

def Customer_history(request):
    uname=request.session["usernm"]
    ob=Purchase_table.objects.filter(usid=uname)
    return render(request,'customer/myorders.html',{"data":ob})



def Shop_receive_orders(request):
    uname=request.session["usernm"]
    ob=Shop_reg.objects.get(Username=uname)
    shid=ob.id
    Name=ob.Sname
    rtng=ob.Rating
    ob=Purchase_table.objects.filter(shopid=str(shid),status="ordered")
    return render(request,'shop/shoporders.html',{"data":ob,"name":Name,"rating":rtng})

def Accept_order(request):
    orid=request.GET.get("qid")
    print(orid)
    try:
        ob=Purchase_table.objects.get(id=int(orid))
        username=ob.usid
        month=ob.month
        year=ob.year
        print(month)
        print(year)
        obc=Customer_reg.objects.get(Username=username)
        ctpye=obc.Cardtype
        print(ctpye)
        obs=Stock_table.objects.get(Month=month,Year=year,Card_type=ctpye)

        ricestck=int(obs.Ricestck)
        riceuser=int(ob.Riceqt)
        riceleft=ricestck-riceuser
        obs.Ricestck=str(riceleft)

        whtstck=int(obs.Whtstck)
        whtuser=int(ob.Whtqt)
        whtleft=whtstck-whtuser
        obs.Whtstck=str(whtleft)

        kerostck=int(obs.Kerostck)
        kerouser=int(ob.Keroqt)
        keroleft=kerostck-kerouser
        obs.Kerostck=str(keroleft)

        atastck=int(obs.Atastck)
        atauser=int(ob.Ataqt)
        ataleft=atastck-atauser
        obs.Atastck=str(ataleft)

        obs.save()
        ob.status="deliverd"
        ob.save()
        data={"status":0}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        data={"status":1}
        return JsonResponse(data,safe=False)
    # print(sid)
    # ob=Purchase_table.objects.get(id=int(sid))
    # ob.status="completed"
    # ob.save()
    # datalist=[]
    # resp={"msg":0}
    
    # return JsonResponse(resp,safe=False)



def Shop_all_orders(request):
    uname=request.session["usernm"]
    ob=Shop_reg.objects.get(Username=uname)
    shid=ob.id
    Name=ob.Sname
    rtng=ob.Rating
    ob=Purchase_table.objects.filter(shopid=str(shid))
    return render(request,'shop/shophistory.html',{"data":ob,"name":Name,"rating":rtng})


def Add_rating(request):
    rating=request.GET.get("rating")
    sid=request.session["shid"]
    print(rating)
    print(sid)
    ob=Shop_reg.objects.get(id=int(sid))
    rval=int(ob.Rating)
    rateval=(int(rating)+rval)/2
    ob.Rating=int(rateval)
    ob.save()
    resp={"msg":0}
    
    return JsonResponse(resp,safe=False)

########====================================android====================================

@csrf_exempt
def Andro_SaveStore(request):
    sname=request.POST.get("fname")
    pan=request.POST.get("pan")
    phone=request.POST.get("phone")
    dist=request.POST.get("dist")
    ardno=request.POST.get("ardno")
    ccnt=request.POST.get("ccnt")
    uname=request.POST.get("uname")
    pswrd=request.POST.get("pswrd")
    
    print(sname,"\n",pan,"\n",phone,"\n",dist,"\n",ardno,"\n",ccnt,"\n",uname,"\n",pswrd)
    try:
        ob=Shop_reg(Sname=sname,Panchayth=pan,Phone=phone,Ardno=ardno,District=dist,Cardcount=ccnt,Username=uname,Password=pswrd)
        ob.save()
        data={"msg":"yes"}
  
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"msg":"no"}
        return JsonResponse(data,safe=False)
@csrf_exempt
def Andro_Savecustomer(request):
    sname=request.POST.get("fname")
    utyp=request.POST.get("utyp")
    phone=request.POST.get("phone")
    addr=request.POST.get("addr")
    rnum=request.POST.get("rnum")
    nfm=request.POST.get("nfm")
    uname=request.POST.get("uname")
    pswrd=request.POST.get("pswrd")


    print(sname,"\n",utyp,"\n",phone,"\n",addr,nfm,"\n",rnum,"\n","\n",uname,"\n",pswrd)
    try:
        ob=Customer_reg(Name=sname,Cardno=rnum,Phone=phone,Address=addr,Cardtype=utyp,No_fm=nfm,Username=uname,Password=pswrd)
        ob.save()
        data={"msg":"yes"}
   
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"msg":"no"}
        return JsonResponse(data,safe=False)
@csrf_exempt
def Andro_CheckLogin(request):
    uname=request.POST.get("uname")
    pswrd=request.POST.get("pswrd")
    utype=request.POST.get("utype")
    print(uname,pswrd,utype)
    print(uname,pswrd,utype)
    if(utype=='Shop owner'):
        try:
            ob=Shop_reg.objects.get(Username=uname,Password=pswrd)
            
            data={"msg":"shop"}
            return JsonResponse(data,safe=False)
        except:
            data={"msg":0}
            return JsonResponse(data,safe=False)
    
    elif(utype=='Customer'):
        try:
            ob=Customer_reg.objects.get(Username=uname,Password=pswrd)
            data={"msg":"custom"}
            return JsonResponse(data,safe=False)
        except:
            data={"msg":0}
            return JsonResponse(data,safe=False)
    else:
        data={"msg":0}
        return JsonResponse(data,safe=False)
@csrf_exempt
def Andro_admin_view_store(request):
    ob=Shop_reg.objects.all()
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["shid"]=i.id
        data["shname"]=i.Sname
        data["panch"]=i.Panchayth
        data["phone"]=i.Phone
        data["ardno"]=i.Ardno
        data["dist"]=i.District
        data["ccount"]=i.Cardcount

        data["usnm"]=i.Username
        data["pswrd"]=i.Password
       
        resplist.append(data)
    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)



@csrf_exempt
def Andro_UpdateShopuser(request):
    uid=request.POST.get("uid")
    sname=request.POST.get("fname")
    ardno=request.POST.get("ardno")
    phone=request.POST.get("phone")
    pan=request.POST.get("pan")
    dist=request.POST.get("dist")
    ccnt=request.POST.get("ccnt")
    uname=request.POST.get("uname")
    pswrd=request.POST.get("pswrd")


    print(sname,"\n",ardno,"\n",phone,"\n",pan,"\n",dist,"\n",ccnt,"\n",uname,"\n",pswrd)
    
    try:
        ob=Shop_reg.objects.get(id=uid)
        ob.Sname=sname
        ob.Ardno=ardno
        ob.Phone=phone
        ob.Panchayth=pan
        ob.District=dist
        ob.Cardcount=ccnt
        ob.Username=uname
        ob.Password=pswrd

 
        ob.save()
        data={"msg":"yes"}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        print(uid)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"msg":"no"}
        return JsonResponse(data,safe=False)

@csrf_exempt
def Andro_DeleteShopuser(request):
    uid=request.POST.get("qid")
    print(uid)
    try:
        ob=Shop_reg.objects.get(id=uid)
        ob.delete()
        data={"status":"1"}
        return JsonResponse(data,safe=False)
    except:
        data={"status":"0"}
        return JsonResponse(data,safe=False)

@csrf_exempt
def Andro_Addstock(request):
    utype=request.POST.get("utype")
    riceqt=request.POST.get("riceqt")
    ricepc=request.POST.get("ricepc")
    ricestk=request.POST.get("ricestk")
    
    whtqt=request.POST.get("whtqt")
    whtpc=request.POST.get("whtpc")

    whtstk=request.POST.get("whtstk")
    keroqt=request.POST.get("keroqt")
    keropc=request.POST.get("keropc")
    kerostk=request.POST.get("kerostk")
    
    ataqt=request.POST.get("ataqt")
    atapc=request.POST.get("atapc")
    atastk=request.POST.get("atastk")
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    print("month and year",month,year)
    print(utype,"\n",riceqt,"\n",ricepc,"\n",ricestk,"\n",whtqt,"\n",whtpc,"\n",whtstk,keroqt,"\n",keropc,
    "\n",kerostk,"\n",ataqt,"\n",atapc,atastk,"\n")
    try:
        ob=Stock_table.objects.get(Card_type=utype,Month=month,Year=year)
        
        data={"status":"1"}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        ob=Stock_table(Card_type=utype,Riceqt=riceqt,Riceprc=ricepc,Ricestck=ricestk,Whtqt=whtqt,Whtprc=whtpc,
        Whtstck=whtstk,Keroqt=keroqt,Keroprc=keropc,Kerostck=kerostk,Ataqt=ataqt,Ataprc=atapc,Atastck=atastk,Month=month,Year=year
        )
        ob.save()
        data={"status":"0"}
        return JsonResponse(data,safe=False)


@csrf_exempt
def Andro_Get_stock(request):
    utype=request.POST.get("utype")
    mnth=request.POST.get("mnth")
    
    dtelist=mnth.split("/")
    mnth=dtelist[0]
    if(len(mnth)==1):
        mnth="0"+mnth
    year=dtelist[1]
    print("month and year",mnth,year)
    print(utype)
    data={}
    try:
        ob=Stock_table.objects.get(Card_type=utype,Month=mnth,Year=year)
        data["id"]=ob.id
        data["riceqt"]=ob.Riceqt
        data["riceprc"]=ob.Riceprc
        data["ricestck"]=ob.Ricestck
        data["whtqt"]=ob.Whtqt
        data["whtprc"]=ob.Whtprc
        data["whtstck"]=ob.Whtstck
        data["keroqt"]=ob.Keroqt
        data["keroprc"]=ob.Keroprc
        data["kerostck"]=ob.Kerostck
        data["ataqt"]=ob.Ataqt
        data["ataprc"]=ob.Ataprc
        data["atastck"]=ob.Atastck
    #     print(datalist)
        data["status"]="yes"
        print("return")
        print(data)
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        
        data={"status":0}
        return JsonResponse(data,safe=False)

@csrf_exempt
def Android_Update_stock(request):
    pid=request.POST.get("pid")
    riceqt=request.POST.get("riceqt")
    ricepc=request.POST.get("ricepc")
    ricestk=request.POST.get("ricestk")
    
    whtqt=request.POST.get("whtqt")
    whtpc=request.POST.get("whtpc")

    whtstk=request.POST.get("whtstk")
    keroqt=request.POST.get("keroqt")
    keropc=request.POST.get("keropc")
    kerostk=request.POST.get("kerostk")
    
    ataqt=request.POST.get("ataqt")
    atapc=request.POST.get("atapc")
    atastk=request.POST.get("atastk")
    
   
  
    print(pid,"\n",riceqt,"\n",ricepc,"\n",ricestk,"\n",whtqt,"\n",whtpc,"\n",whtstk,keroqt,"\n",keropc,
    "\n",kerostk,"\n",ataqt,"\n",atapc,atastk,"\n")
    try:
        ob=Stock_table.objects.get(id=int(pid))
        ob.Riceqt=riceqt
        ob.Riceprc=ricepc
        ob.Ricestck=ricestk
        ob.Whtqt=whtqt
        ob.Whtprc=whtpc
        ob.Whtstck=whtstk
        ob.Keroqt=keroqt
        ob.Keroprc=keropc
        ob.Kerostck=kerostk
        ob.Ataqt=ataqt
        ob.Ataprc=atapc
        ob.Atastck=atastk
        ob.save()
                
        data={"status":"0"}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        
        data={"status":"1"}
        return JsonResponse(data,safe=False)


@csrf_exempt
def Andro_admin_view_history(request):
    ob=Purchase_table.objects.all()
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["shopname"]=i.shopname
        data["usid"]=i.usid
        data["Riceqt"]=i.Riceqt
        data["Riceprc"]=i.Riceprc
        data["Whtqt"]=i.Whtqt
        data["Whtprc"]=i.Whtprc

        data["Keroqt"]=i.Keroqt
        data["Keroprc"]=i.Keroprc
        data["Ataqt"]=i.Ataqt
        data["Ataprc"]=i.Ataprc
        data["total"]=i.total

        data["month"]=i.month
        data["year"]=i.year
        data["status"]=i.status
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

@csrf_exempt
def Andro_shop_view_quota(request):
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    ob=Stock_table.objects.filter(Month=month,Year=year)
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["Card_type"]=i.Card_type
        data["Riceqt"]=i.Riceqt
        data["Riceprc"]=i.Riceprc
        data["Whtqt"]=i.Whtqt
        data["Whtprc"]=i.Whtprc

        data["Keroqt"]=i.Keroqt
        data["Keroprc"]=i.Keroprc
        data["Ataqt"]=i.Ataqt
        data["Ataprc"]=i.Ataprc
        
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

@csrf_exempt
def Andro_shop_sell_ration(request):
    uname=request.POST.get("usnm")
    print(uname)
    obs=Shop_reg.objects.get(Username=uname)
    shid=obs.id
    print(shid)
    ob=Purchase_table.objects.filter(shopid=str(shid),status="ordered")
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["orid"]=i.id
        data["usid"]=i.usid
        data["Riceqt"]=i.Riceqt
        data["Riceprc"]=i.Riceprc
        data["Whtqt"]=i.Whtqt
        data["Whtprc"]=i.Whtprc

        data["Keroqt"]=i.Keroqt
        data["Keroprc"]=i.Keroprc
        data["Ataqt"]=i.Ataqt
        data["Ataprc"]=i.Ataprc
        data["total"]=i.total

        data["month"]=i.month
        data["year"]=i.year
        data["purchasecode"]=i.purchasecode
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)

@csrf_exempt
def Andro_approve_ration(request):
    orid=request.POST.get("orid")
    print(orid)
    try:
        ob=Purchase_table.objects.get(id=int(orid))
        username=ob.usid
        obc=Customer_reg.objects.get(Username=username)
        ctpye=obc.Cardtype
        year = str(datetime.now().year)
        month = str(datetime.now().month)
        
        if(len(month)==1):
            month="0"+month
        print(year)
        print(month)
        obs=Stock_table.objects.get(Month=month,Year=year,Card_type=ctpye)

        ricestck=int(obs.Ricestck)
        riceuser=int(ob.Riceqt)
        riceleft=ricestck-riceuser
        obs.Ricestck=str(riceleft)

        whtstck=int(obs.Whtstck)
        whtuser=int(ob.Whtqt)
        whtleft=whtstck-whtuser
        obs.Whtstck=str(whtleft)

        kerostck=int(obs.Kerostck)
        kerouser=int(ob.Keroqt)
        keroleft=kerostck-kerouser
        obs.Kerostck=str(keroleft)

        atastck=int(obs.Atastck)
        atauser=int(ob.Ataqt)
        ataleft=atastck-atauser
        obs.Atastck=str(ataleft)

        obs.save()
        ob.status="deliverd"
        ob.save()
        data={"status":"1"}
        return JsonResponse(data,safe=False)
    except:
        data={"status":"0"}
        return JsonResponse(data,safe=False)



@csrf_exempt
def Andro_shop_view_history(request):
    uname=request.POST.get("usnm")
    print(uname)
    obs=Shop_reg.objects.get(Username=uname)
    shid=obs.id
    print(shid)
    ob=Purchase_table.objects.filter(shopid=str(shid),status="deliverd")
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["usid"]=i.usid
        data["Riceqt"]=i.Riceqt
        data["Riceprc"]=i.Riceprc
        data["Whtqt"]=i.Whtqt
        data["Whtprc"]=i.Whtprc

        data["Keroqt"]=i.Keroqt
        data["Keroprc"]=i.Keroprc
        data["Ataqt"]=i.Ataqt
        data["Ataprc"]=i.Ataprc
        data["total"]=i.total

        data["month"]=i.month
        data["year"]=i.year
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)





@csrf_exempt
def Andro_user_list_shop(request):
    dist=request.POST.get("dist")
    
   
    ob=Shop_reg.objects.filter(District=dist)
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["shid"]=i.id
        data["Shname"]=i.Sname
        data["Panchayth"]=i.Panchayth
        data["Rating"]=i.Rating
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)


@csrf_exempt
def Andro_get_user_ration(request):
    usname=request.POST.get("usname")
    print(usname)
    data={}
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    try:
        obp=Purchase_table.objects.get(usid=usname,month=month,year=year)
        data["status"]="no"
        
        print(data)
        return JsonResponse(data,safe=False)
    except:
        obc=Customer_reg.objects.get(Username=usname)
        ctpye=obc.Cardtype
        print(ctpye)
        
        
        obs=Stock_table.objects.get(Month=month,Year=year,Card_type=ctpye)


        data["Riceqt"]=obs.Riceqt
        data["Riceprc"]=obs.Riceprc
        data["Whtqt"]=obs.Whtqt
        data["Whtprc"]=obs.Whtprc
        data["Keroqt"]=obs.Keroqt
        data["Keroprc"]=obs.Keroprc
        data["Ataqt"]=obs.Ataqt
        data["Ataprc"]=obs.Ataprc
        data["status"]="yes"
        return JsonResponse(data,safe=False)


@csrf_exempt
def Andro_buy_product(request):
    usname=request.POST.get("usname")
    shopid=request.POST.get("shopid")

    riceqt=request.POST.get("riceqt")
    ricepc=request.POST.get("ricepc")
    
    whtqt=request.POST.get("whtqt")
    whtpc=request.POST.get("whtpc")

    keroqt=request.POST.get("keroqt")
    keropc=request.POST.get("keropc")
    
    ataqt=request.POST.get("ataqt")
    atapc=request.POST.get("atapc")
    total=request.POST.get("total")

    obs=Shop_reg.objects.get(id=int(shopid))
    shname=obs.Sname
    
    print(shopid)
    print(shname)
    print(usname)
    pnumber = random.randint(1000,9999)
    print(pnumber)
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    
    if(len(month)==1):
        month="0"+month
    print(year)
    print(month)
    request.session["pcode"]=pnumber
    try:

        ob1=Purchase_table(shopid=shopid,shopname=shname,
        usid=usname,Riceqt=riceqt,Riceprc=ricepc,Whtqt=whtqt,Whtprc=whtpc,Keroqt=keroqt,Keroprc=keropc,
        Ataqt=ataqt,Ataprc=atapc,total=total,month=month,year=year,purchasecode=pnumber)
        ob1.save()
        resp={"msg":str(pnumber)}
     
    except:

        resp={"msg":"0"}
    return JsonResponse(resp,safe=False)

@csrf_exempt
def Android_add_rating(request):
    rating=request.POST.get("rating")
    sid=request.POST.get("shopid")

    print(rating)
    print(sid)
    ob=Shop_reg.objects.get(id=int(sid))
    rval=int(ob.Rating)
    rateval=(int(rating)+rval)/2
    ob.Rating=int(rateval)
    ob.save()
    resp={"msg":"0"}
    
    return JsonResponse(resp,safe=False)

@csrf_exempt
def Andro_user_view_history(request):
    uname=request.POST.get("uname")
    print(uname)
    ob=Purchase_table.objects.filter(usid=uname)
    
    resplist=[]
    respdata={}
    for i in ob:
        data={}
        data["shopname"]=i.shopname
        
        data["Riceqt"]=i.Riceqt
        data["Riceprc"]=i.Riceprc
        data["Whtqt"]=i.Whtqt
        data["Whtprc"]=i.Whtprc

        data["Keroqt"]=i.Keroqt
        data["Keroprc"]=i.Keroprc
        data["Ataqt"]=i.Ataqt
        data["Ataprc"]=i.Ataprc
        data["total"]=i.total

        data["month"]=i.month
        data["year"]=i.year
        data["status"]=i.status
        resplist.append(data)

    respdata["data"]=resplist
    print(respdata)
    return JsonResponse(respdata,safe=False)





def Approvestore(request):
    uid=request.GET.get("qid")
    print(uid)
    
    try:
        ob=Shop_reg.objects.get(id=uid)
        print(ob.Active)
        ob.Active="1"
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)

    except:
        data={"status":0}
        return JsonResponse(data,safe=False)


def Adminviewauto(request):
    lang=request.session["lang"]
    ob=Auto_reg.objects.filter(Active="0")
    ob1=Auto_reg.objects.filter(Active="1")
    return render(request,'admin/Admin_view_auto.html',{"data":ob,"data2":ob1,"lang":lang})
def Approveauto(request):
    uid=request.GET.get("qid")
    print(uid)
    
    try:
        ob=Auto_reg.objects.get(id=uid)
        print(ob.Active)
        ob.Active="1"
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)

    except:
        data={"status":0}
        return JsonResponse(data,safe=False)

def Updateauto(request):
    uid=request.GET.get("uid")
    sname=request.GET.get("fname")
    vnum=request.GET.get("vnum")
    phone=request.GET.get("phone")
    addr=request.GET.get("addr")
    lat=request.GET.get("lat")
    longg=request.GET.get("longg")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    print(sname,"\n",vnum,"\n",phone,"\n",addr,"\n",lat,"\n",longg,"\n",uname,"\n",pswrd)
    
    try:
        ob=Auto_reg.objects.get(id=uid)
        ob.Name=sname
        ob.Vnumber=vnum
        ob.Phone=phone
        ob.Address=addr
        ob.Latitude=lat
        ob.Longitude=longg
        ob.Username=uname
        ob.Password=pswrd
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        print(uid)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)
def Deleteauto(request):
    uid=request.GET.get("qid")
    print(uid)
    try:
        ob=Auto_reg.objects.get(id=uid)
        ob.delete()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except:
        data={"status":0}
        return JsonResponse(data,safe=False)

def Admin_add_cat(request):
    lang=request.session["lang"]
    return render(request,'admin/Add_category.html',{"lang":lang})

def add_cat(request):
    cat=request.GET.get("cat")
    try:
        ob=Category_table.objects.get(Category=cat)
    
        data={"status":1}
        return JsonResponse(data,safe=False)
    except:
        ob=Category_table(Category=cat)
        ob.save()
        data={"status":0}
        return JsonResponse(data,safe=False)
def Admin_add_Subcat(request):
    lang=request.session["lang"]
    ob=Category_table.objects.all()
    return render(request,'admin/Add_sub_category.html',{"data":ob,"lang":lang})

def add_Subcat(request):
    subcat=request.GET.get("subcat")
    cat=request.GET.get("cat")
    
    try:
        ob=All_Category.objects.get(Category=cat,Sub_Category=subcat)
    
        data={"status":1}
        return JsonResponse(data,safe=False)
    except:
        ob=All_Category(Category=cat,Sub_Category=subcat)
        ob.save()
        data={"status":0}
        return JsonResponse(data,safe=False)




def Add_items(request):
    lang=request.session["lang"]
    uname=request.session["usernm"]
    print(uname)
    ob=Shop_reg.objects.get(Username=uname)
    Name=ob.Sname
    ob1=Category_table.objects.all()
    return render(request,'shop/Add_product.html',{"name":Name,"ob1":ob1,"lang":lang})

def get_sub_cat(request):
    cat=request.GET.get("cat")
    resp={}
    datalist=[]
    ob=All_Category.objects.filter(Category=cat)
    for i in ob:
        datalist.append(i.Sub_Category)

    resp["data"]=datalist
    print(resp)
    return JsonResponse(resp,safe=False)


@ensure_csrf_cookie
def upload_item(request):
    
    data={}
    if request.method == "GET":
        return render(request, 'Shophome.html', )
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        pname=request.POST.get("pname")
        cat=request.POST.get("cat")
        subcat=request.POST.get("subcat")
        price=request.POST.get("price")
        info=request.POST.get("info")
        stck=request.POST.get("stck")
        usernm=request.session["usernm"]
        print("shopname==>",usernm)
        print(pname+subcat+price+info+stck)
        print(cat)
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        dt_string=str(dt_string)+".jpg"
        


        try:
            ob=Product_table.objects.get(Shop_usernm=usernm,Product_name=pname)
            data["msg"]="exist"
        
            return JsonResponse(data,safe=False)
        except:
            for f in files:
                handle_uploaded_file(f,dt_string)
            ob=Product_table(Shop_usernm=usernm,Product_name=pname,Category=cat,Sub_Category=subcat,Price=price,Info=info,Stock=stck,Img_path=dt_string)
            ob.save()                
            data["msg"]="yes"
            print (data)
            return JsonResponse(data,safe=False)
    else:
        data["msg"]="error"
        print (data)
        return JsonResponse(data,safe=False)

def handle_uploaded_file(f,name):
    print(name)
    filename='app1/static/images/'+str(name)+'.jpg'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def View_items(request):
    lang=request.session["lang"]
    return render(request,'shop/View_product.html',{"lang":lang})




@ensure_csrf_cookie
def update_item(request):
    
    data={}
    if request.method == "GET":
        return render(request, 'Shophome.html', )
    if request.method == 'POST':
        files = request.FILES.getlist('files[]', None)
        print("length of file==>",len(files))
        pname=request.POST.get("pname")
        pid=request.POST.get("pid")
        price=request.POST.get("price")
        info=request.POST.get("info")
        stck=request.POST.get("stck")
        print(pname+pid+price+info+stck)
        usernm=request.session["usernm"]
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        dt_string=str(dt_string)+".jpg"

        k=False
        ob=Product_table.objects.filter(Product_name=pname,Shop_usernm=usernm)
        pidlist=[]
        for i in ob:
            prid=i.id
            if(int(pid)!=prid):
                k=True
            print(prid)
        
        if(k):
            data["msg"]="exist"
        else:
            ob1=Product_table.objects.get(id=int(pid))
            if(len(files)==0):
                
                ob1.Product_name=pname
                ob1.Price=price
                ob1.Info=info
                ob1.Stock=stck
                ob1.save()
                data["msg"]="yes"
            else:
                for f in files:
                    handle_uploaded_file(f,dt_string)
                ob1.Product_name=pname
                ob1.Price=price
                ob1.Info=info
                ob1.Stock=stck
                ob1.Img_path=dt_string
                ob1.save()
                data["msg"]="yes"

    
        return JsonResponse(data,safe=False)
    
    else:
        data["msg"]="error"
        print (data)
        return JsonResponse(data,safe=False)



def Autohome(request):
    uname=request.session["usernm"]
    lang=request.session["lang"]
    print(uname)
    ob=Auto_reg.objects.get(Username=uname)
    Name=ob.Name
    return render(request,'auto/Auto_home.html',{'name':Name,"lang":lang})





def updatelocation(request):
    uname=request.session["usernm"]
    lati=request.GET.get("lati")
    longi=request.GET.get("longi")
    ob=Auto_reg.objects.get(Username=uname)
    ob.Latitude=str(lati)
    ob.Longitude=str(longi)
    ob.save()
    data={"status":0}
    return JsonResponse(data,safe=False)




def Customershop(request):
    lang=request.session["lang"]
    print("yes")
    try:
        shid=request.POST.get("idno")
        ob=Shop_reg.objects.get(id=int(shid))
        Sname=ob.Sname
        print(shid)
        request.session["shopid"]=shid
    except:
        shid=request.session["shopid"]
        ob=Shop_reg.objects.get(id=int(shid))
        Sname=ob.Sname
        print(shid)
    return render(request,'customer/shop_page.html',{'sname':Sname,"lang":lang})


def Electronics_hone(request):
    shid=request.session["shopid"]
    lang=request.session["lang"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    usrnm=ob.Username
    data=Product_table.objects.filter(Shop_usernm=usrnm,Category='Electronics')
    
    return render(request,'customer/electronics.html',{'sname':Sname,'data':data,"lang":lang})



def addtocart(request):
    itemid=request.POST.get("idno")
    page=request.POST.get("page")
    print(page)
    ob0=Product_table.objects.get(id=int(itemid))
    pname=ob0.Product_name
    price=ob0.Price
    cat=ob0.Sub_Category
    shid=request.session["shopid"]
    uname=request.session["usernm"]
    print(itemid+pname+price+shid+uname)

    try:
        ob=Cart_table.objects.get(shopid=shid,usid=uname,itemid=itemid)
        if(page=="electronics"):
            return HttpResponse("<script>alert('Item already added!!');window.location.href='/Electronics_hone/'</script>")
        elif(page=="food"):
            return HttpResponse("<script>alert('Item already added!!');window.location.href='/Food_home/'</script>")
        elif(page=="dress"):
            return HttpResponse("<script>alert('Item already added!!');window.location.href='/Dress_home/'</script>")
        elif(page=="foot"):
            return HttpResponse("<script>alert('Item already added!!');window.location.href='/Footwear_home/'</script>")
        else:
            return HttpResponse("<script>alert('Item already added!!');window.location.href='/Grocery_home/'</script>")
    except:
        ob=Cart_table(shopid=shid,usid=uname,itemid=itemid,product=pname,price=price,category=cat)
        ob.save()
        if(page=="electronics"):
            return HttpResponse("<script>alert('Item added to cart');window.location.href='/Electronics_hone/'</script>")
        elif(page=="food"):
            return HttpResponse("<script>alert('Item added to cart');window.location.href='/Food_home/'</script>")
        elif(page=="dress"):
            return HttpResponse("<script>alert('Item added to cart');window.location.href='/Dress_home/'</script>")
        elif(page=="foot"):
            return HttpResponse("<script>alert('Item added to cart');window.location.href='/Footwear_home/'</script>")
        else:
            return HttpResponse("<script>alert('Item added to cart');window.location.href='/Grocery_home/'</script>")


def Dress_home(request):
    lang=request.session["lang"]
    shid=request.session["shopid"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    usrnm=ob.Username
    data=Product_table.objects.filter(Shop_usernm=usrnm,Category='Dress')
    
    return render(request,'customer/dress.html',{'sname':Sname,'data':data,"lang":lang})


def Food_home(request):
    shid=request.session["shopid"]
    lang=request.session["lang"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    usrnm=ob.Username
    data=Product_table.objects.filter(Shop_usernm=usrnm,Category='Food')
    
    return render(request,'customer/food.html',{'sname':Sname,'data':data,"lang":lang})

def Footwear_home(request):
    shid=request.session["shopid"]
    lang=request.session["lang"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    usrnm=ob.Username
    data=Product_table.objects.filter(Shop_usernm=usrnm,Category='Footwear')
    
    return render(request,'customer/footwear.html',{'sname':Sname,'data':data,"lang":lang})

def Grocery_home(request):
    lang=request.session["lang"]
    shid=request.session["shopid"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    usrnm=ob.Username
    data=Product_table.objects.filter(Shop_usernm=usrnm,Category='Footwear')
    
    return render(request,'customer/grocery.html',{'sname':Sname,'data':data,"lang":lang})



def Cart_page(request):
    print("cartpage")
    shid=request.session["shopid"]
    lang=request.session["lang"]
    ob=Shop_reg.objects.get(id=int(shid))
    Sname=ob.Sname
    uname=request.session["usernm"]
    data=Cart_table.objects.filter(shopid=shid,usid=uname)
    total=0
    for i in data:
        total=total+int(i.price)
    print("total==>",total)
    return render(request,'customer/cartpage.html',{'sname':Sname,'data':data,'total':total,"lang":lang})


def delete_cart(request):
    pid=request.GET.get("qid")
    ob=Cart_table.objects.get(id=int(pid))
    ob.delete()
    data={"status":0}
    return JsonResponse(data,safe=False)

def payment_page(request):
    lang=request.session["lang"]
    shid=request.session["shopid"]
    uname=request.session["usernm"]
    data=Cart_table.objects.filter(shopid=shid,usid=uname)
    total=0
    for i in data:
        total=total+int(i.price)
    print("total==>",total)
    return render(request,'customer/payment.html',{'total':total,"lang":lang})



def My_orders(request):
    lang=request.session["lang"]
    uname=request.session["usernm"]
    print(lang)
    ob=Purchase_table.objects.filter(usid=uname,status="ordered")
    return render(request,'customer/myorders.html',{'data':ob,"lang":lang})



def add_auto(request):
    pid=request.GET.get("qid")
    print(pid)
    request.session["pid"]=pid
    resp={"msg":0}
    return JsonResponse(resp,safe=False)



from math import sin, cos, sqrt, atan2, radians
def getdistance(latcar,longcar,lat1,long1):
    # approximate radius of earth in km
    R = 6373.0
    lati1=float(latcar)
    longi1=float(longcar)
    lati2=float(lat1)
    longi2=float(long1)
    lat1 = radians(lati1)
    lon1 = radians(longi1)
    lat2 = radians(lati2)
    lon2 = radians(longi2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print("Result:", distance)
    return int(distance)


def View_near_auto(request):
    lang=request.session["lang"]
    pid=request.session["pid"]
    print(pid)
    ob=Purchase_table.objects.get(id=int(pid))
    shopid=ob.shopid
    ob2=Shop_reg.objects.get(id=int(shopid))
    name=ob2.Sname
    lati=ob2.Latitude
    longi=ob2.Longitude



    mylist=[]
    try:
        ob1=Auto_reg.objects.all()
        
        for i in ob1:
            li1=[]
            lat1=i.Latitude
            long1=i.Longitude
            print(lat1,long1)
            dist=getdistance(lati,longi,lat1,long1)
            print("distance==>",dist)
            if(dist<41):
                li1.append(i.id)
                li1.append(i.Name)
                li1.append(i.Vnumber)
                li1.append(i.Phone)
                mylist.append(li1)
        print(mylist)
    except Exception as e:
        print(e)


    print(name)
    resp={}
    resp["datalist"]=mylist
    return render(request,'customer/view_near_auto.html',{"data":resp,"lang":lang})


def add_auto_notify(request):
    aid=request.GET.get("aid")
    pid=request.session["pid"]
    uname=request.session["usernm"]
    ob=Purchase_table.objects.get(id=int(pid))
    shopid=ob.shopid
    ob2=Shop_reg.objects.get(id=int(shopid))
    sname=ob2.Sname
    splc=ob2.Address
    items=ob.items
    category=ob.category
    price=ob.price
    total=ob.total
    date=ob.date
 
    print(pid)
    try:
        ob=Auto_notification_table.objects.get(orid=pid,autoid=aid)
        resp={"msg":0}
        return JsonResponse(resp,safe=False)
    except:
        ob=Auto_notification_table(orid=pid,autoid=aid,sname=sname,splace=splc,usid=uname,items=items,category=category
        ,price=price,total=total,date=date)
        ob.save()
        resp={"msg":1}
        return JsonResponse(resp,safe=False)




def my_notification(request):
    lang=request.session["lang"]
    uname=request.session["usernm"]
    ob=Auto_reg.objects.get(Username=uname)
    aid=ob.id
    print(aid)
    ob1=Auto_notification_table.objects.filter(autoid=str(aid),status="not accepted")
    return render(request,'auto/notifications.html',{'data':ob1,"lang":lang})


def accept_request(request):
    print("accept request")
    oid=request.GET.get("qid")
    ob=Auto_notification_table.objects.get(id=int(oid))
    prid=ob.orid
    ob.status="accepted"
    ob.save()
    ob2=Purchase_table.objects.get(id=int(prid))
    ob2.autoname=request.session["usernm"]
    ob2.save()
    resp={"msg":0}
    return JsonResponse(resp,safe=False)


def auto_delivery(request):
    uname=request.session["usernm"]
    lang=request.session["lang"]

    mylist=[]
    try:
        ob1=Purchase_table.objects.filter(autoname=uname,status="ordered")
        for i in ob1:
            li1=[]
            li1.append(i.id)
            li1.append(i.items)
            li1.append(i.total)
            shopid=i.shopid
            ob2=Shop_reg.objects.get(id=int(shopid))
            sname=ob2.Sname
            splc=ob2.Address
            li1.append(sname)
            li1.append(splc)
            cuid=i.usid
            ob3=Customer_reg.objects.get(Username=cuid)
            cname=ob3.Name
            cplc=ob3.Address
            li1.append(cname)
            li1.append(cplc)
            mylist.append(li1)
        print(mylist)
    except Exception as e:
        print(e)
    resp={}
    resp["datalist"]=mylist
    return render(request,'auto/delivery.html',{'data':resp,"lang":lang})


def complete_order(request):
    print("accept request")
    oid=request.GET.get("qid")
    ob=Purchase_table.objects.get(id=int(oid))   
    ob.status="delivered"
    ob.save()
    resp={"msg":0}
    return JsonResponse(resp,safe=False)


def Bot_response(request):
    qstn=request.GET.get("qstn")
    print(qstn)
    
    response = chatbot.get_response(qstn)
    print("bot-->",response)
    print(str(response))
    data={"msg":str(response)}
    return JsonResponse(data,safe=False)


 






