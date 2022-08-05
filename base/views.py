from ast import operator
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.
def getRoutes(request):
    routes = [
        'http://0.0.0.0:8000/api/',
        'http://0.0.0.0:8000/api/clients',
        'http://0.0.0.0:8000/api/mails/<int:pk>',
        'http://0.0.0.0:8000/api/mails/full',
        'http://0.0.0.0:8000/api/messages',
    ]

@api_view(['POST'])
def createClient(request):
    data = request.data
    client = Client.objects.create(
        number=data['number'],
        operator_code=data['operator_code'],
        tag=data['tag'],
        timezone=data['timezone']
    )
    serializer = ClientSerializer(client, many=False)

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return Response('Client deleted.')

@api_view(['PUT'])
def updateClient(request, pk):
    data = request.data
    client = Client.objects.get(id=pk)
    serializer = ClientSerializer(instance=client, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)










@api_view(['GET'])
def mailings(request, pk):
    mailings = MailSender.objects.get(id=pk)
    serializer = MailingSerializer(mailings, many=False)

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMailing(request, pk):
    mailing = MailSender.objects.get(id=pk)
    mailing.delete()

    return Response('MailSender was deleted.')

@api_view(['POST'])
def createMailSender(request):
    data = request.data
    mailSender = MailSender.objects.create(
        start_time=data['start_time'],
        end_time=data['end_time'],

        start_day=data['start_day'],
        end_day=data['end_day'],

        body=data['body'],
        tag=data['tag'],
        operator_code=data['operator_code'],
    )
    serializer = MailingSerializer(mailSender, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def updateMailSender(request, pk):
    data = request.data
    mailing = MailSender.objects.get(id=pk)
    serializer = MailingSerializer(instance=mailing, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)











@api_view(['GET'])
def clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def full_info(request):

    total_messages = MailSender.objects.count()
    mailing = MailSender.objects.values('id')
    messages_sent = Message.objects.filter(status='Sent').count()
    context = {'Total number of mailings': total_messages,
                   'The number of messages sent': messages_sent}
    result = {} 
        
    for row in mailing:
        res = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
        mail = Message.objects.filter(mail_sender=row['id']).all()
        group_sent = mail.filter(status='Sent').count()
        group_no_sent = mail.filter(status='No sent').count()
        res['Total messages'] = len(mail)
        res['Sent'] = group_sent
        res['No sent'] = group_no_sent
        result[row['id']] = res
        
    context['Total sent messages'] = result
    return Response(context)
