from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    HttpResponse,
)
from django.urls import reverse

from . models import (
    HeroSectionText,
    CarouselSectionText,
    CarouselInnerSection,
    SecondParallaxSection,
    StudyGroupText,
)

from ministries.models import Ministries

from . forms import (
    HeroSectionTextForm,
    CarouselSectionTextForm,
    CarouselInnerSectionForm,
    AddNewCarouselForm,
    SecondParallaxSectionForm,
    StudyGroupTextForm,
)


def index(request):
    """ A view to return the undex page """
    hero_heading = get_object_or_404(HeroSectionText, id=1)
    carousel_text = get_object_or_404(CarouselSectionText, id=1)
    second_parallax_section = get_object_or_404(SecondParallaxSection, id=1)
    carousel_inner_section = CarouselInnerSection.objects.all()
    second_parallax_section = get_object_or_404(SecondParallaxSection, id=1)
    study_group_text = get_object_or_404(StudyGroupText, id=1)
    alpha_study = get_object_or_404(CarouselSectionText, id=2)
    bible_study = get_object_or_404(CarouselSectionText, id=3)
    sunday_services = get_object_or_404(SecondParallaxSection, id=2)

    ministry = get_object_or_404(Ministries, id=1)

    if request.user.is_superuser:
        form = HeroSectionTextForm(instance=hero_heading)
        carousel_form = CarouselSectionTextForm(instance=carousel_text)
        second_parallax_form = SecondParallaxSectionForm(
            instance=second_parallax_section)
        new_carousel_form = AddNewCarouselForm()
        sunday_edit_form = SecondParallaxSectionForm(
            instance=sunday_services)
        group_title_edit_form = StudyGroupTextForm(
            instance=study_group_text)

        alpha_text_edit_form = CarouselSectionTextForm(instance=alpha_study)

        bible_study_text_edit_form = CarouselSectionTextForm(
            instance=bible_study)

        if request.method == 'POST':
            form = HeroSectionTextForm(request.POST, instance=hero_heading)
            if form.is_valid():
                form.save()
                messages.success(request, 'Text updated successfully.')

        context = {
            'hero_heading': hero_heading,
            'carousel_inner_section': carousel_inner_section,
            'carousel_text': carousel_text,
            'second_parallax_section': second_parallax_section,
            'study_group_text': study_group_text,
            'alpha_study': alpha_study,
            'bible_study': bible_study,
            'sunday_services': sunday_services,
            # all forms are below
            'form': form,
            'carousel_form': carousel_form,
            'new_carousel_form': new_carousel_form,
            'second_parallax_form': second_parallax_form,
            'sunday_edit_form': sunday_edit_form,
            'group_title_edit_form': group_title_edit_form,
            'alpha_text_edit_form': alpha_text_edit_form,
            'bible_study_text_edit_form': bible_study_text_edit_form,
            'ministry': ministry

        }
    else:
        context = {
            'hero_heading': hero_heading,
            'carousel_inner_section': carousel_inner_section,
            'carousel_text': carousel_text,
            'second_parallax_section': second_parallax_section,
            'study_group_text': study_group_text,
            'alpha_study': alpha_study,
            'bible_study': bible_study,
            'sunday_services': sunday_services,
        }
    template = 'home/index.html'
    return render(request, template, context)


def carousel_text_edit(request, id):
    carousel_text = get_object_or_404(CarouselSectionText, id=id)
    if request.method == 'POST':
        form = CarouselSectionTextForm(request.POST, instance=carousel_text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text updated successfully.')
            return redirect(reverse('home'))


def inner_carousel_edit(request, id):
    carousel_inner_text = get_object_or_404(CarouselInnerSection, id=id)
    if request.method == 'POST':
        form = CarouselInnerSectionForm(request.POST,
                                        request.FILES,
                                        instance=carousel_inner_text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text updated successfully.')
            return redirect(reverse('home'))

        else:
            messages.error(request, f'Please correct following.{form.errors}')
            return redirect(reverse('home'))


def add_new_carousel(request):

    if request.method == 'POST':
        form = AddNewCarouselForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Carousel Iteme added.")
        else:
            messages.error(request, "Add new carousel failed.")

    return redirect(reverse('home'))


def parallax_edit(request, id):
    second_parallax_section = get_object_or_404(SecondParallaxSection, id=id)

    if request.method == 'POST':
        form = SecondParallaxSectionForm(request.POST,
                                        instance=second_parallax_section)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text updated successfully.')
            return redirect(reverse('home'))

        else:
            messages.error(request, f'Please correct following.{form.errors}')
            return redirect(reverse('home'))


def study_group_edit(request):
    study_group_heading_text = get_object_or_404(StudyGroupText, id=1)

    if request.method == 'POST':
        form = StudyGroupTextForm(request.POST,
                                  instance=study_group_heading_text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text updated successfully.')
            return redirect(reverse('home'))

        else:
            messages.error(request, f'Please correct following.{form.errors}')
            return redirect(reverse('home'))
