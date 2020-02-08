"""Celery tasks"""

import time

from django.core.mail import send_mail

from celery import shared_task
from random_word import RandomWords

from .models import RandomWord


@shared_task
def create_word(user_id):
    time.sleep(10)
    generator = RandomWords()
    word = generator.get_random_word()

    random_word = RandomWord.objects.create(user_id=user_id, word=word)

    # send_mail(
    #     subject='Se ha creado tu palabra',
    #     from_email='djangopruebas@yandex.com',
    #     message='Ahora puedes ir a verlo a https://localhost:8000/generator',
    #     recipient_list=['mauricio@eterna.digital'],
    #     fail_silently=False,
    # )

    return random_word
