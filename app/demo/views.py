# import sys
# sys.path.append('/Users/jong-yeollee/Projects/Delivery_App/Web/GoogleCloud/venv/lib/python3.9/site-packages')

import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.shortcuts import render, redirect
from .forms import PersonForm
#import psutil

#print("####### Processes in views: begin")
#for proc in psutil.process_iter():
#    print(proc.name())
#print("####### Processes in views: end")

# Create your views here.
def demo(request):
    # Use the application default credentials
    logging.warning('In demo1')
    cred = credentials.ApplicationDefault()
    logging.warning('In demo2')

    print(firebase_admin._apps)
    print(firebase_admin.App)

    app = firebase_admin.initialize_app(cred, {
        'projectId': 'kakaocall-0929',
    })
    logging.warning('In demo3')

    # cred = credentials.Certificate('/serviceAccountKey.json')
    # firebase_admin.initialize_app(cred)

    db = firestore.client()
    logging.warning('In demo4')
    doc_ref = db.collection(u'users').document(u'abell')
    doc_ref.set({
    u'first': u'Jong-Yeol',
    u'last': u'Lee',
    u'born': 1815
    })

    # doc_ref = db.collection(u'users').document(u'astevejobs')
    # doc_ref.set({
    #    u'first': u'Steve',
    #    u'middle': u'Mathison',
    #    u'last': u'Jobs',
    #    u'born': 1912
    # })

    users_ref = db.collection(u'users')
    logging.warning('In demo5')
    docs = users_ref.stream()
    logging.warning('In demo6')

    doc_list = []
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        doc_list.append(doc.to_dict())

    logging.warning('In demo7')
    firebase_admin.delete_app(app)

    # logging.basicConfig(level=logging.NOTSET)
    logging.warning("Log message goes here.")

    # FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    # logging.basicConfig(format=FORMAT)
    # d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    # logging.warning('Protocol problem: %s', 'connection reset', extra=d)
    # 2022-08-18 02: 38:18,520 192.168.0.1 fbloggs Protocol problem: connection reset

    form = PersonForm()

    print('Context:')
    for d in doc_list:
        # print(d)
        print('last: ', d['last'], ', first: ', d['first'], ', born: ', d['born'])

    context = {
        'test': '####### TEST String (테스트 스트링입니다)@@@@ #######',
        'test2': '####### 2nd TEST String (두번째 테스트 스트링입니다)@@@@ #######',
        'doc_list': doc_list,
        'form': form,
    }

    logging.warning('In views.demo')
    return render(request, 'demo/demo.html', context)

def login(request):
    context = {
        'phone_number': 'Phone number',
        'name': 'name',
    }
    return render(request, 'demo/login.html', context)

def policy(request):
    context = {
        'phone_number': 'Phone number',
        'name': 'name',
    }
    return render(request, 'demo/policy.html', context)

def input_data(request):
    logging.warning('In input_data1')

    if request.method == 'POST':
        """
        last = request.POST.get('last')
        first = request.POST.get('first')
        born = request.POST.get('born')

        if last == 'None':
            last = 'last_default'
        if first == 'None':
            first = 'first_default'
        if born == 'None':
            born = 'born_default'

        if last == '':
            last = 'last_default2'
        if first == '':
            first = 'first_default2'
        if born == '':
            born = 'born_default2'



        logging.warning('Last: %s', last)
        logging.warning('First: %s', first)
        logging.warning('Born: %s', born)

        cred = credentials.ApplicationDefault()
        logging.warning('In input_data2')
        app = firebase_admin.initialize_app(cred, {
            'projectId': 'kakaocallge',
        })
        logging.warning('In input_data3')
        db = firestore.client()
        logging.warning('In input_data4')
        doc_ref = db.collection(u'users').document(last)
        logging.warning('In input_data5')
        doc_ref.set({
            u'first': first,
            u'last': last,
            u'born': born
        })
        logging.warning('In input_data6')
        firebase_admin.delete_app(app)
        logging.warning('In input_data7')
        # FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
        # logging.basicConfig(format=FORMAT)
        # d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        # logging.warning('Protocol problem: %s', 'connection reset', extra=d)

        # 2022-08-18 02: 38:18,520 192.168.0.1 fbloggs Protocol problem: connection reset

        # FORMAT = '%(asctime)s %(last)-15s %(first)-8s %(born)s'
        # logging.basicConfig(format=FORMAT)
        # d = {'last': last, 'first': first, 'born': born}
        # logging.warning('In input_data: %s', 'test', extra=d)
        # 2022-08-18 02: 38:18,520 192.168.0.1 fbloggs Protocol problem: connection reset
    """




        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            last = person.last
            first = person.first
            born = person.born

            #last = 'test_last'
            #first = 'test_first'
            #born = 'test_born'

            cred = credentials.ApplicationDefault()

            logging.warning('In input_data2')
            app = firebase_admin.initialize_app(cred, {
                'projectId': 'kakaocall-0929',
            })
            logging.warning('In input_data3')
            db = firestore.client()
            logging.warning('In input_data4')
            doc_ref = db.collection(u'users').document(last)
            logging.warning('In input_data5')

            doc_ref.set({
                u'first': first,
                u'last': last,
                u'born': born
            })
            logging.warning('In input_data6')
            firebase_admin.delete_app(app)

    return redirect('demo:demo')    #demo/urls.py에 정의된 URL의 별칭 path('', views.demo, name='demo')





