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

from . forms import (
    HeroSectionTextForm,
    CarouselSectionTextForm,
    CarouselInnerSectionForm,
    AddNewCarouselForm,
    SecondParallaxSectionForm
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

    if request.user.is_superuser:
        form = HeroSectionTextForm(instance=hero_heading)
        carousel_form = CarouselSectionTextForm(instance=carousel_text)
        second_parallax_form = SecondParallaxSectionForm(
            instance=second_parallax_section)
        new_carousel_form = AddNewCarouselForm()
        sunday_edit_form = SecondParallaxSectionForm(
            instance=sunday_services)

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


def carousel_text_edit(request):
    carousel_text = get_object_or_404(CarouselSectionText, id=1)
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


def second_parallax_edit(request):
    second_parallax_section = get_object_or_404(SecondParallaxSection, id=1)

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


def sunday_parallax_edit(request):
    sunday_parallax_section = get_object_or_404(SecondParallaxSection, id=2)

    if request.method == 'POST':
        form = SecondParallaxSectionForm(request.POST,
                                         instance=sunday_parallax_section)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text updated successfully.')
            return redirect(reverse('home'))

        else:
            messages.error(request, f'Please correct following.{form.errors}')
            return redirect(reverse('home'))