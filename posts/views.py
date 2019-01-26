from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from .models import (
    Posts,
    Text,
    Countries,
    Destination,
    Activity,
    CitizenshipCountries
)
from .forms import PlanForm, CitizenshipForm, ContactForm
from django.db.models import Q
from django.views import View
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def index(request):
    return render(request, 'posts/index.html')


def about(request):
    return render(request, 'posts/about.html')


class PlanRelocation(View):
    form_class = PlanForm
    template_name = 'posts/plan_relocation.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PlanForm(request.POST)
        try:
            if form.is_valid():
                country_id = form.cleaned_data['countries']
                destination_id = form.cleaned_data['destinations']
                activity_id = form.cleaned_data['activities']
                result = country_id + "_" + destination_id + "_" + activity_id
                if not Text.objects.filter(option_key=result).exists():
                    return redirect('error_page')
                result_text = Text.objects.values_list('text', flat=True).get(option_key=result)
                context = {
                    'country': Countries.objects.get(pk=int(country_id)),
                    'destination': Destination.objects.get(pk=int(destination_id)),
                    'activity': Activity.objects.get(pk=int(activity_id)),
                    'information': result_text
                }
                return render(request, 'posts/information.html', context)
            else:
                return redirect('error_page')
        except TypeError:
            return redirect('error_page')


def immigration_blog(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'posts/expat_blog.html', context)


class PostListView(ListView):
    model = Posts
    template_name = 'posts/expat_blog.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 4


class SearchView(View):
    template_name = 'posts/search_results.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        results = Posts.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
        context = {'results': results}

        return render(self.request, self.template_name, context)


class PostDetailView(DetailView):
    model = Posts


def privacy_policy(request):
    return render(request, 'posts/privacy_policy.html')


def terms_of_use(request):
    return render(request, 'posts/terms_of_use.html')


def subscribe(request):
    return render(request, 'posts/subscribe.html')


def error_page(request):
    return render(request, 'posts/error_page.html')


class Citizenship(View):
    form_class = CitizenshipForm
    template_name = 'posts/citizenship.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CitizenshipForm(request.POST)
        try:
            if form.is_valid():
                country_id = form.cleaned_data['citizenship_countries']
                if not CitizenshipCountries.objects.filter(id=country_id).exists():
                    return redirect('error_page')
                result_text = CitizenshipCountries.objects.values_list('text', flat=True).get(id=country_id)
                context = {
                    'country': CitizenshipCountries.objects.get(pk=int(country_id)),
                    'information': result_text,
                    'form': self.form_class
                }
                return render(request, self.template_name, context)
            else:
                raise Http404
        except TypeError:
            raise Http404


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "posts/contact.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            print(from_email)
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message + "\n" + from_email, from_email, ['aliya.tastemirova@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "posts/contact.html", {'form': form})


def successView(request):
    return render(request, "posts/success.html")

