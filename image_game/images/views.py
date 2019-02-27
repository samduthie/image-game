import random

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import TemplateView, View

from images.models import Image, Tag


def get_random_image():
    return Image.objects.order_by('?').first()


def get_random_tags():
    # todo need a method that gets tags NOT in the image tag_set
    return Tag.objects.order_by('?')[:4]


def get_list_of_tags(image):
    tags = [image.description for image in image.tag_set.order_by('?')[:1]]

    tags.extend(get_random_tags())

    random.shuffle(tags)
    return tags


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = Image.objects.all()[0]
        context['image_url'] = image.url

        context['tags'] = get_list_of_tags(image)

        return context


class NextView(View):

    def get(self, request, image_id, tag):
        # todo validate this in a django form

        image = Image.objects.get(pk=image_id)
        # todo move this code to the model
        image_tag_descriptions = [
            tag.description.lower() for tag in image.tag_set.all()
        ]

        correct_guess = False
        if tag.lower() in image_tag_descriptions:
            correct_guess = True

        t = get_template('index.html')

        image = get_random_image()

        context = {
            'tags': get_list_of_tags(image),
            'correct_guess': correct_guess,
            'image_url': image.url,
            'image_id': image.id
        }
        html = t.render(context=context)

        return HttpResponse(html)





