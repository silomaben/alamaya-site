from django.shortcuts import render
from .models import Video,Gallery,Destination
from django.views.generic import ListView,DetailView
from .models import Post

from .forms import ContactForm,BookingForm
from django.conf import settings


from django.core.mail import send_mail
from safari.settings import EMAIL_HOST_USER



def home(request):
        video=Video.objects.all()

        return render(request, 'home.html', {"video":video})

def destinations(request):
        return render(request, 'destinations.html', {})

def destination_details(request, tag):
        destination = Destination.objects.filter(tag=tag)

        destination_name = tag.replace('-', ' ')
        print(destination_name)
        
        context = {
                'destination': tag,
                'Destination': destination,
                'destinationTitle': destination_name,
        }
        return render(request, 'destination.html', context)


def packages(request):
        return render(request, 'packages.html', {})

def package_1(request):
        return render(request, 'package_1_maasaimara.html', {})
def package_2(request):
        return render(request, 'package_2_hidden_gems.html', {})
def package_3(request):
        return render(request, 'package_3_magical_kenya.html', {})
def package_4(request):
        return render(request, 'package_4_budget_camp.html', {})
def package_5(request):
        return render(request, 'package_5_mid_range.html', {})


def booking(request):

        
        destination = request.GET.get('destination', '')
        


        if request.method == "POST":

                print("post detected")

                # Inspect raw form data before cleaning
                print("Raw form data:", request.POST)


                form = BookingForm(request.POST)

                

                if form.is_valid():
                        print("Form data:", form.cleaned_data)

                        print("form is valid")

                        name = form.cleaned_data['name']
                        email = form.cleaned_data['email']
                        phone_no = form.cleaned_data['phone_no']
                        no_of_guests = form.cleaned_data['number_of_guests']
                        destination = form.cleaned_data['destination']
                        datefrom = form.cleaned_data['datetime_from']
                        dateto = form.cleaned_data['datetime_to']
                        message = form.cleaned_data['special_request']


                        #send email
                        subject = "Booking request from " + name
                        email_body = f"Name: {name}\nEmail: {email}\nPhone No: {phone_no}\nDestination:{destination} \nNumber of Guests: {no_of_guests}\nFrom : {datefrom} to {dateto}\n\nSpecial Request:\n{message}"
                        send_mail(
                        subject,
                        email_body,
                        EMAIL_HOST_USER,
                        ["ignit3graphics@gmail.com"]

                        # ,"adrielngugi@gmail.com"
                        
                        )
                        # ["smichire@gmail.com","sifaspecialneedsnetwork@gmail.com"]
                        message = f"Thank you for choosing Alamaya Adventures Limited! We have received your booking.\n\nOur team is processing it and will respond soon.\n\nThank you for your patience, and we look forward to connecting with you shortly.\n\nBest regards,\nSamuel Ngugi\nAlamaya Adventures Limited"

                        send_mail(
                        "Processing Booking",
                        message,
                        EMAIL_HOST_USER,
                        [email]
                        )

                        form = BookingForm()

                        context = {
                        'destination': destination,
                        'name':name,
                        'form': form
                        }
                        
                        

                        return render(request, 'booking.html',context )
                else:
                        print(form.errors)

                        print('form seems invalid')
                        context = {
                        'destination': destination,
                        'form': form
                        }
                        
                        

                        return render(request, 'booking.html',context )

        else:

                form = BookingForm()

        print(form.errors)

        context = {
        'destination': destination,
        'form': form
        }
        
        return render(request, 'booking.html', context)
                
        
       

def contact(request):
        if request.method == "POST":
                # name = request.POST['name']
                # email = request.POST['email']
                # subject = request.POST['subject']
                # message = request.POST['message']

                form = ContactForm(request.POST)

                print("Raw form data:", request.POST)

                if form.is_valid():
                        name = form.cleaned_data['name']
                        email = form.cleaned_data['email']
                        subject = form.cleaned_data['subject']
                        message = form.cleaned_data['message']

                        print(form.cleaned_data)


                        
                        subject = "New message from " + name
                        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
                        send_mail(subject, email_body, EMAIL_HOST_USER, ["ignit3graphics@gmail.com"])
                        
                        message2 = f"Thank you for reaching out to Alamaya Adventures Limited! We have received your message and appreciate your inquiry.\n\nOur team is reviewing it and will respond soon.\n\nThank you for your patience, and we look forward to connecting with you shortly.\n\nBest regards,\nSamuel Ngugi\nAlamaya Adventures Limited"

                        send_mail("Thank you for contacting us!", message2, EMAIL_HOST_USER, [email])

                        form = ContactForm()

                        return render(request, 'contact.html', {'form': form, 'success_message': 'Your message has been sent!','site_key':settings.RECAPTCHA_PUBLIC_KEY})
                
        else:    
                form = ContactForm()

        print(form.errors)        

        return render(request, 'contact.html', {'form': form})

      
    # return render(request, 'contact.html', {})


def album(request, tag):
    images = Gallery.objects.filter(tag=tag)
    
    context = {
        'tag': tag,
        'images': images,
    }
    return render(request, 'album.html', context)



def gallery(request):
        return render(request, 'gallery.html', {})

def about(request):
        return render(request, 'about.html', {})

# def blog(request):
#         return render(request, 'blog.html', {})

class blogView(ListView):
       model = Post
       template_name = 'blog.html'
class articleDetailView(DetailView):
       model = Post
       template_name = 'article_details.html'



