"""Generator app views"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .tasks import create_word
from .models import Identicon, RandomWord


@login_required
def identicon(request):
    context = {
        'words': RandomWord.objects.filter(user=request.user),
        'identicons': Identicon.objects.filter(user=request.user),
    }
    if request.method == 'POST':
        image = request.FILES.get('identicon')
        Identicon.objects.create(user=request.user, image=image)
        create_word.delay(request.user.id)
        context['message'] = 'Se está generando la palabra y se ha subido la imagen'

    return render(request, 'generator/identicon.html', context)
