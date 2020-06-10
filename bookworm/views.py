from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models import Q
from datetime import datetime
import qrcode
from django.contrib import admin
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import keyboard
import ctypes
from datetime import timedelta
from datetime import date

def search(request):
    search_result = Author.objects.all().order_by('last_name')
    context = {'author':  Author.objects.all().order_by('last_name'), 'country': Country.objects.all()}
    return render(request, 'bookworm/search.html', context)


def loan_modifier(request):
        if "create_loan" in request.POST:
            cap = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_PLAIN
            id_utente = ""
            id_volume = []
            c=1
            volumes = Volume.objects.all()
            while c!=4:
                try:
                    _, frame = cap.read()
                    qr_data = pyzbar.decode(frame)
                    for data in qr_data:
                        if c==2:
                            if len(id_volume) > 0:
                                cv2.putText(frame, "libro riconosciuto: " + data.data.decode('ascii'), (50, 50), font, 2,(255, 0, 0), 3)
                            else:
                                cv2.putText(frame, "utente accettato: " + data.data.decode('ascii'), (50, 50), font, 2,(255, 0, 0), 3)
                        type, id = data.data.decode('ascii').split('_', 1)
                    #check utente
                        if type == "utente" and c==1:
                            print(id)
                            id_utente = int(id)
                            try:
                                user = Extra_user_info.objects.get(id__exact=id_utente)
                                c=2
                            except Extra_user_info.DoesNotExist:
                                user  = None
                    #check volumi
                        if type == "volume" and c == 2 and int(id) not in id_volume:
                            try:
                                if len(id_volume) <= 5:
                                    vol = volumes.get(id__exact=int(id)).book.book_name
                                    c=2
                                    id_volume.append(int(id))
                                    #cv2.putText(frame, "il volume " + vol + " è stato accettato", (50, 50), font, 2,(255, 0, 0), 3)
                                else:
                                    ctypes.windll.user32.MessageBoxW(0, "Hai raggiunto il numero massimo di libri che puoi prendere in prestito", "Attenzione!!!", 1)
                            except Volume.DoesNotExist:
                                vol = None

                except ValueError:
                    ctypes.windll.user32.MessageBoxW(0, "qr_code inserito non valido, ripetere il processo", "Attenzione!!!", 1)
                    c=4
                    cv2.destroyAllWindows()

                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1)
                if key == 27:
                    if c==1:
                        ctypes.windll.user32.MessageBoxW(0, "noleggio annullato", "Attenzione!!!", 1)
                        c=4
                    elif c==2 and id_volume == []:
                        ctypes.windll.user32.MessageBoxW(0, "noleggio annullato", "Attenzione!!!", 1)
                        c=4
                    elif c==2:
                        volumes = volumes.filter(pk__in=id_volume)
                        ctypes.windll.user32.MessageBoxW(0, "Operazione effettuata con successo l'utente "
                        + user.user.username + " ha preso in prestito " + str(len(id_volume)) + " libri", "Attenzione!!!", 1)
                        volumes = volumes.filter(pk__in=id_volume)
                        user = user.user
                        for id_vol in id_volume:
                            vol = Volume.objects.get(id__exact=id_vol)
                            print("ho creato " + vol.book.book_name)
                            l = Loan(return_date=datetime.now()+timedelta(days=30), borrow_date=datetime.now(), user=user, volume=vol, prolungato=False)
                            l.save()
                        c=4
                    cv2.destroyAllWindows()

            return HttpResponseRedirect("http://127.0.0.1:8000/admin/bookworm/loan")

        elif "delete_loan" in request.POST:
            cap = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_PLAIN
            id_utente = ""
            c=1
            l = Loan.objects.all()
            while c!=2:
                try:
                    _, frame = cap.read()
                    qr_data = pyzbar.decode(frame)
                    for data in qr_data:
                        type, id = data.data.decode('ascii').split('_', 1)
                        if type == "volume":
                            cv2.putText(frame, "libro riconosciuto: " + data.data.decode('ascii'), (50, 50), font, 2,(255, 0, 0), 3)
                            if l.filter(volume__id__exact=int(id)).exists():
                                l.get(volume__id__exact=int(id)).delete()

                except ValueError:
                    ctypes.windll.user32.MessageBoxW(0, "qr_code inserito non valido, ripetere il processo", "Attenzione!!!", 1)
                    c=2
                    cv2.destroyAllWindows()

                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1)
                if key == 27:
                    ctypes.windll.user32.MessageBoxW(0, "Operazione effettuata con successo", "Attenzione!!!", 1)
                    c=2
                    cv2.destroyAllWindows()

            return HttpResponseRedirect("http://127.0.0.1:8000/admin/bookworm/loan")
            #return render(request, 'admin/')



#/*
#search_result=""
#genre_list = Genre.objects.all()
#if request.method == 'GET': # If the form is submitted
#    if(request.GET.get('choice', None) = 'book'):
#    if(request.GET.get('editore', None)):
#        search_result = Editor.objects.all().order_by('name')
#        search_result = search_result.filter(name__contains=request.GET.get('search_box', ""))
#        search_result = search_result.filter(country__name=request.GET.get('country', ""))
#    if(request.GET.get('author', None)):
#        search_result = Author.objects.all().order_by('last_name')
#        search_result = search_result.filter(Q(first_name__contains=request.GET.get('search_box_first_name', "")) | Q(last_name__contains=request.GET.get('search_box_last_name', "")))
#        search_result = search_result.filter(country_id__name=request.GET.get('country', ""))
#else:
##    search_result = Book.objects.order_by('book_name')[:5]
###context = {'search_result': search_result,
####            'genre_list': genre_list}
#return render(request, 'bookworm/search.html', context)
