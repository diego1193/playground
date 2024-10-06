from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import m2m_changed
from django.db import transaction

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(verbose_name="Escribe tu mensaje")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "Mensage de " + self.user.username

class ThreadManager(models.Manager):
    def find(self, list_users):
        print(list_users)
        queryset = self.filter(users=list_users[0]).filter(users=list_users[1])
        print(queryset)
        if len(queryset) > 0:
            print("No entra")
            return queryset[0]
        return None
    
    def find_or_create(self, list_users):
        thread = self.find(list_users)
        if thread == None:  
            print("entra")      
            with transaction.atomic():
                thread = Thread.objects.create()
                thread.users.set(list_users)
                thread.save()
        return thread       

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name="threads")
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']


def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None) # Conjuntos de Id de mensajes
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)
    
    #Buscarian los mensajes q si estan en el pk_set y lo borramos
    pk_set.difference_update(false_pk_set) # encuenta los numeros q se repiten en cada conjuno

    # Forzar la actualizacion haciendo un save
    instance.save()

m2m_changed.connect(messages_changed, sender=Thread.messages.through)
