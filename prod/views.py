from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Oferta
from django.urls import reverse


def inblog(request):
    latest_articles_list = Oferta.objects.order_by('-pub_date')[:10]
    return render(request, 'oferta/oferta.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Oferta.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена!')
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'oferta/oferta_detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Oferta.objects.get(id=article_id)
        latest_comments_list = a.comment_set.order_by('-id')[:10]
    except:
        raise Http404('Статья не найдена!')
    ctx = {
        'article': a,
        'latest_comments_list': latest_comments_list
    }
    author = request.POST['name']
    comment = request.POST['text']

    if not author:
        ctx['message'] = 'Author name cannot be empty!'
        return render(request, 'oferta/oferta_detail.html', ctx)
    if not comment:
        ctx['message'] = 'Write comment!'
        return render(request, 'oferta/oferta_detail.html', ctx)

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('oferta:detail', args=(a.id,)))
