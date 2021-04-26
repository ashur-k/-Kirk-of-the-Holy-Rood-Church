from django.shortcuts import(
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404)
from .models import Notice, NewsLetter
from .forms import NoticeForm


def notices(request):
    news_letter = NewsLetter.objects.all().order_by('-id')[:1]

    notices = Notice.objects.filter(notice_display_status=True)
    notice_form = NoticeForm()

    print(news_letter)
    for item in news_letter:
        print(item.title)

    context = {
        'notices': notices,
        'notice_form': notice_form,
        'news_letter': news_letter,
    }
    template = 'notices/notices.html'
    return render(request, template, context)


def add_new_notice(request):
    if request.method == 'POST':
        notice_form = NoticeForm(request.POST)
        if notice_form.is_valid():
            notice_form.save()
        else:
            return HttpResponse(notice_form.errors)

    return redirect(reverse('notices'))


def edit_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        notice_form = NoticeForm(request.POST, instance=notice)
        if notice_form.is_valid():
            notice_form.save()
        else:
            return HttpResponse(notice_form.errors)

    return redirect(reverse('notices'))


def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.delete()
    return redirect(reverse('notices'))
