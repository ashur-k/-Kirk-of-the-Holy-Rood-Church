from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404)
from .models import Notice, NewsLetter
from .forms import NoticeForm, NewsLetterForm
from django.contrib.auth.decorators import login_required


def notices(request):
    news_letter = NewsLetter.objects.all().order_by('-id')[:1]

    notices = Notice.objects.filter(notice_display_status=True)
    notice_form = NoticeForm()

    context = {
        'notices': notices,
        'notice_form': notice_form,
        'news_letter': news_letter,
    }
    template = 'notices/notices.html'
    return render(request, template, context)


@login_required
def add_new_notice(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        notice_form = NoticeForm(request.POST)
        if notice_form.is_valid():
            notice_form.save()
        else:
            return HttpResponse(notice_form.errors)

    return redirect(reverse('notices'))


@login_required
def edit_notice(request, notice_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        notice_form = NoticeForm(request.POST, instance=notice)
        if notice_form.is_valid():
            notice_form.save()
            messages.success(request, 'You have succesfully updated the page!')
        else:
            messages.error(request, 'Please check there is error in form')

    return redirect(reverse('notices'))


@login_required
def delete_notice(request, notice_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    notice = get_object_or_404(Notice, id=notice_id)
    notice.delete()
    return redirect(reverse('notices'))


@login_required
def add_new_newsletter(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        news_letter_form = NewsLetterForm(request.POST, request.FILES)
        if news_letter_form.is_valid():
            news_letter_form.save()
            messages.success(
                request,
                'You have succesfully added new news letter!'
                )
            return redirect(reverse('notices'))
        else:
            messages.error(
                request,
                'Please fill in form properly'
                )

    news_letter_form = NewsLetterForm()
    context = {
        'news_letter_form': news_letter_form,
     }
    template = 'notices/add_new_newsletter.html'
    return render(request, template, context)
