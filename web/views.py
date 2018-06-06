from django.shortcuts import render

from .models import Site


def index_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/index.html", context)


def about_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/about.html", context)


def services_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/services.html", context)


def rental_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/car_rental.html", context)


def contact_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/contact.html", context)


def gallery_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/gallery.html", context)


def blog_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/blog.html", context)


def topography_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/typography.html", context)


def projects_view(request):
    details = Site.objects.all()

    context = {
        "details": details,
    }

    return render(request, "Web/projects.html", context)

