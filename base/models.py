import pytz
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    
    validator = RegexValidator(regex=r'^7\d{10}$',
                                 message="Number should be in format 7XXXXXXXXXX! ")
    number = models.CharField(validators=[validator], max_length=11)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=100, blank=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    class Meta:
        verbose_name_plural = 'Clients'
    
    def __str__(self):
        return f"Client's number is {self.number}"

class MailSender(models.Model):

    start_time = models.TimeField(verbose_name='Time to start send a message')
    end_time = models.TimeField(verbose_name='Time to end send a message')

    start_day = models.DateTimeField(verbose_name='Sender to start')
    end_day = models.DateTimeField(verbose_name='Sender to end')

    body = models.TextField(max_length=255)
    tag = models.CharField(max_length=100, blank=True)
    operator_code = models.CharField(max_length=3, blank=True)

    class Meta:
        verbose_name_plural = 'MailSenders'

    @property
    def send_is_valid(self):
        moment = timezone.now()
        time_before = self.start_day
        time_after = self.end_day

        if time_before <= moment and moment <= time_after:
            return True

        return False

    def __str__(self):
        return self.body[0:50] 
    
        
class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"
    
    STATUS = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]
    
    mail_sender = models.ForeignKey(MailSender, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    created = models.DateTimeField(verbose_name='Time create', auto_now_add=True)
    status = models.CharField(verbose_name='Sending status', max_length=15, choices=STATUS)

    class Meta:
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message text {self.mail_sender} for {self.client}'
