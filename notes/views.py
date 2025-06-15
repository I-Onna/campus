from django.shortcuts import render

from .models import *

def avaluacio(request):
    queryset = Grup.objects.all()
    return render(request,"index.html",{"grups":queryset})

def assignatures_grup(request,grup_id):
    grup = Grup.objects.get(pk=grup_id)
    grup_string = grup.nivell + ' ' + grup.grau
    queryset = Assignatura.objects.filter(grup=grup)

    return render(request,"assignatures_grup.html",{"assignatures":queryset,"grup":grup_string,"grup_id":grup_id,})

def grup_notes_assignatura(request,grup_id,assignatura_id):
    grup = Grup.objects.get(pk=grup_id)
    assignatura  = Assignatura.objects.get(pk=assignatura_id)
    notes = Nota.objects.filter(matricula__assignatura__id=assignatura_id,
            matricula__alumne__grup__id=grup_id)
    matricules = Matricula.objects.filter(assignatura=assignatura, alumne__grup=grup)

    return render(request,"grup_notes_assignatura.html",{"matricules":matricules,"assignatura":assignatura.nom, "notes":notes})

"""def classificacio(request,lliga_id):
    lliga = Lliga.objects.get(pk=lliga_id)
    equips = lliga.equips.all()
    classi = []
 
    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        for partit in lliga.partits.filter(local=equip):
            if partit.gols_local() > partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        for partit in lliga.partits.filter(visitant=equip):
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
        classi.append( (punts,equip.nom) )
    # ordenem llista
    classi.sort(reverse=True)
    return render(request,"classificacio.html",
                {
                    "classificacio":classi,
                })
                """