from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Mask import mask_rcnn_demo
from . import models
import json
import datetime

from .models import Player

username = "dd"


def index(request):
    return render(request, "index.html")


def start1(request):
    try:
        level = request.POST.get('level').strip()
        fig_name = request.POST.get('fig_name').strip()
        global username
        username = request.POST.get("username").strip()
        if level is '' or fig_name is '' or username is '':
            messages = models.Message.objects.all()
            context = {"none": 0, 'messages': messages}
            return render(request, 'start.html', context)
        else:
            if Player.objects.filter(name=username):
                score = Player.objects.get(name=username).score
            else:
                player = models.Player(name=username, score=0)
                player.save()
                score = Player.objects.get(name=username).score
            label_list0, label_list1, label_list2 = mask_rcnn_demo.mask(level, fig_name, 0)
    except BaseException:
        messages = models.Message.objects.all()
        context = {"none": 2, 'messages': messages}
        return render(request, 'start.html', context)
    else:
        messages = models.Message.objects.all()
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'messages': messages,
                   'score': score, 'times': 1}
        return render(request, 'start1.html', context)


def start2(request):
    try:
        level = 2
        global username
        username = request.POST.get("username").strip()
        if level is '' or username is '':
            messages = models.Message.objects.all()
            context = {"none": 0, 'messages': messages}
            return render(request, 'random.html', context)
        else:
            if Player.objects.filter(name=username):
                score = Player.objects.get(name=username).score
            else:
                player = models.Player(name=username, score=0)
                player.save()
                score = Player.objects.get(name=username).score
            label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandomeasy(level, 0, 1)
    except BaseException:
        messages = models.Message.objects.all()
        context = {"none": 2, 'messages': messages}
        return render(request, 'random.html', context)
    else:
        messages = models.Message.objects.all()
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'messages': messages, 'score': score, 'times': json.dumps(2)}
        return render(request, 'randomeasy1.html', context)


def start21(request):
    try:
        level = 2
        score = Player.objects.get(name=username).score
        label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandomeasy(level, 0, 1)
    except BaseException:
        return render(request, 'random.html')
    else:
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'score': score, 'times': json.dumps(2)}
        return render(request, 'randomeasy1.html', context)


def start3(request):
    try:
        level = 2
        global username
        username = request.POST.get("username").strip()
        if level is '' or username is '':
            messages = models.Message.objects.all()
            context = {"none": 0, 'messages': messages}
            return render(request, 'random.html', context)
        else:
            if Player.objects.filter(name=username):
                score = Player.objects.get(name=username).score
            else:
                player = models.Player(name=username, score=0)
                player.save()
                score = Player.objects.get(name=username).score
            label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandommiddle(level, 0, 1)
    except BaseException:
        messages = models.Message.objects.all()
        context = {"none": 2, 'messages': messages}
        return render(request, 'random.html', context)
    else:
        messages = models.Message.objects.all()
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'messages': messages, 'score': score, 'times': json.dumps(3)}
        return render(request, 'middle.html', context)


def start31(request):
    try:
        level = 2
        score = Player.objects.get(name=username).score
        label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandommiddle(level, 0, 1)
    except BaseException:
        return render(request, 'random.html')
    else:
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'score': score, 'times': json.dumps(3)}
    return render(request, 'middle.html', context)


def start4(request):
    try:
        level = 2
        global username
        username = request.POST.get("username").strip()
        if level is '' or username is '':
            messages = models.Message.objects.all()
            context = {"none": 0, 'messages': messages}
            return render(request, 'random.html', context)
        else:
            if Player.objects.filter(name=username):
                score = Player.objects.get(name=username).score
            else:
                player = models.Player(name=username, score=0)
                player.save()
                score = Player.objects.get(name=username).score
            label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandomhard(level, 0, 1)
    except BaseException:
        messages = models.Message.objects.all()
        context = {"none": 2, 'messages': messages}
        return render(request, 'random.html', context)
    else:
        messages = models.Message.objects.all()
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'messages': messages, 'score': score, 'times': json.dumps(4)}
        return render(request, 'hard.html', context)


def start41(request):
    try:
        level = 2
        score = Player.objects.get(name=username).score
        label_list0, label_list1, label_list2 = mask_rcnn_demo.maskrandomhard(level, 0, 1)
    except BaseException:
        return render(request, 'random.html')
    else:
        context = {'label_list0': json.dumps(label_list0),
                   'label_list1': json.dumps(label_list1),
                   'label_list2': json.dumps(label_list2), 'score': score, 'times': json.dumps(4)}
    return render(request, 'hard.html', context)


def start(request):
    messages = models.Message.objects.all()
    return render(request, 'start.html', {'messages': messages})


def random(request):
    return render(request, 'random.html')


def newbie(request):
    return render(request, "newbie.html")


def newbie2(request):
    return render(request, "newbie2.html")


def newbie3(request):
    return render(request, "newbie3.html")


def answer(request):
    return render(request, "answer.html")


def answer1(request):
    return render(request, 'answer1.html')


def randomeasyans(request):
    return render(request, 'randomeasyans.html')


def middleans(request):
    return render(request, 'middleans.html')


def hardans(request):
    return render(request, 'hardans.html')


def upload(request):
    return render(request, 'upload.html')


def Timeout(request):
    return render(request, 'Timeout.html')


def message(request):
    if request.method == 'POST':
        fig = request.FILES.get('fig')
        # context = {'name': name}
        username1 = request.POST.get("username").strip()
        title = request.POST.get("fig_name").strip()
        content = request.POST.get("content")
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = models.Message(title=title, content=content, username=username1, publish=publish)
        if username1 is '' or title is '' or content is None or fig is None:
            return render(request, 'upload.html', {"none": 0})
        elif models.Message.objects.filter(title=title):
            return render(request, 'upload.html', {"none": 2})
        else:
            message.save()
            messages = models.Message.objects.all()
            mask_rcnn_demo.upload(fig, title)
            context = {"none": 1, 'messages': messages}
            # limit = 10
            # paginator = Paginator(messages, limit)  # 按每页10条分页
            # page = request.GET.get('page', '1')  # 默认跳转到第一页
            # result = paginator.page(page)
            return render(request, 'message.html', context)
    else:
        messages = models.Message.objects.all()
        # messages = models.Message.objects.filter(title='0027.jpg ').delete()
        return render(request, 'message.html', {'messages': messages})


def score1(request):
    score = Player.objects.get(name=username).score
    addscore = int(request.POST.get('score1'))
    Player.objects.filter(name=username).update(score=score + addscore)
    return HttpResponse("ok")


@csrf_exempt
def score(request):
    players = models.Player.objects.order_by("-score")
    # players = models.Player.objects.filter(name='16206801').delete()
    return render(request, 'score.html', {'players': players})
