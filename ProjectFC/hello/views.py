from django.shortcuts import render, redirect
from django.db.models import Sum
from hello.models import MainDataBase, ConfigDataBase, passWordDB, MatchingWordsDB


def firstScreenSetup(request):
  configdatabaseallentries = ConfigDataBase.objects.all()
  freqCardTarget = request.GET.get('freqCardTarget', 0)
  print('Méthode firstScreenSetup***********************************')
  print('freqCardTarget : ', freqCardTarget)

  if request.method == 'POST':
    freqCardTarget = request.POST.get('freqCardTarget', 0)
    if freqCardTarget == '':
        freqCardTarget = 0
    setup = ConfigDataBase.objects.last()

    print('Méthode POST***********************************')
    print('freqCardTarget : ', freqCardTarget)
    print('setup : ', setup)
    if setup != None:
      setup.freqCardTarget = freqCardTarget
      setup.save()
      return redirect(mainScreen)
    else:
      phraseMystere = ''
      ConfigDataBase.objects.create(freqCardTarget=freqCardTarget, phraseMystere=phraseMystere)
      return redirect(mainScreen)

  context = {
    'configdatabaseallentries': configdatabaseallentries,
  }

  return render(request, 'firstScreenSetup.html', context)


def mainScreen(request):

    fc_target = getattr(ConfigDataBase.objects.last(), 'freqCardTarget')
    fc_counter = MainDataBase.objects.aggregate(sum=Sum('freqCard'))['sum']
    if fc_counter is None:
        fc_counter = 0

    if request.method == 'GET':
        nomid = int(request.GET.get('nomid', 0))
        nom = request.GET.get('nom', '')
        freqCard = request.GET.get('freqCard', 0)
        maindatabaseallentries = MainDataBase.objects.all()
        print('Type du get all : ', type(maindatabaseallentries))
        print(maindatabaseallentries)

    if request.method == 'POST':
        nomid = int(request.POST.get('nomid', 0))
        nom = request.POST.get('nom')
        freqCard = request.POST.get('freqCard', 0)
        maindatabaseallentries = MainDataBase.objects.all()

        if nomid > 0:
            enregistrement = MainDataBase.objects.get(pk=nomid)
            enregistrement.nom = nom
            enregistrement.freqCard = freqCard
            enregistrement.save()
            return redirect(mainScreen)
        else:
            if nom != '':
                if not freqCard.isnumeric():
                    freqCard = 0
                enregistrement = MainDataBase.objects.create(nom=nom.capitalize(), freqCard=freqCard)
                return redirect(mainScreen)

    if nomid > 0:
        enregistrement = MainDataBase.objects.get(pk=nomid)
    else:
        enregistrement = ''

    context = {
        'nomid': nomid,
        'maindatabaseallentries': maindatabaseallentries,
        'enregistrement': enregistrement,
        'fc_counter': fc_counter,
        'fc_target': fc_target
    }

    return render(request, 'mainScreen.html', context)


def delete_eleve(request):
    MainDataBase.objects.all().delete()
    return redirect(mainScreen)


def resultScreen(request):
    phraseMystere = getattr(ConfigDataBase.objects.last(), 'phraseMystere')

    context = {
      'phraseMystere': phraseMystere,
    }
    return render(request, 'resultScreen.html', context)


def phraseScreenSetup(request):
    configdatabaseallentries = ConfigDataBase.objects.all()

    if request.method == 'POST':
      phraseMystere = request.POST.get('phraseMystere', '')
      print('phraseMystere : ', phraseMystere)
      if phraseMystere == '':
          phraseMystere = '42.'
      setup = ConfigDataBase.objects.last()

      if setup != None:
        setup.phraseMystere = phraseMystere
        setup.save()
        return redirect(firstScreenSetup)
      else:
        freqCardTarget = 0
        ConfigDataBase.objects.create(freqCardTarget=freqCardTarget, phraseMystere=phraseMystere)
        return redirect(firstScreenSetup)

    context = {
      'configdatabaseallentries': configdatabaseallentries,
    }

    return render(request, 'phraseScreenSetup.html', context)

def matchingWordsScreen(request):

    id_select = 0
    screenToBeDisplayed = 'matchingWordsScreen.html'
    matchingwordsdbAllEntries = MatchingWordsDB.objects.order_by('?')
    listCodesToCheck = list()
    listCodesUserEntryDropDown = list()

    for texte in matchingwordsdbAllEntries:
        listCodesToCheck.append(texte.iDTexte)
    print("listCodesToCheck  =====", listCodesToCheck)

    for reponse in matchingwordsdbAllEntries:
        userEntryDropDown = request.POST.get(str(reponse.id), '')
        try:
            listCodesUserEntryDropDown.append(int(userEntryDropDown))
        except:
            pass

    if listCodesToCheck == listCodesUserEntryDropDown:
        screenToBeDisplayed = "successScreen.html"

    context = {
        'matchingwordsdbAllEntries': matchingwordsdbAllEntries,
    }
    print("context", context)

    return render(request, screenToBeDisplayed, context)

def mainMenu(request):

  context = {}
  return render(request, 'mainMenu.html', context)

def lockedMenu(request):
    passWord = getattr(passWordDB.objects.last(), 'passWord')
    screenToBeDisplayed = 'lockedMenu.html'

    if request.method == 'POST':
        passWordEntry = request.POST.get('passWordEntry', '')
        if passWordEntry == passWord:
            screenToBeDisplayed = 'mainMenu.html'
        else:
            screenToBeDisplayed = 'lockedMenu.html'

    context = {}
    return render(request, screenToBeDisplayed, context)