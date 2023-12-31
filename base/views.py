from django.shortcuts import render
from .models import Video,Gallery,Destination
from django.views.generic import ListView,DetailView
from .models import Post


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
                name = request.POST['name']
                email = request.POST['email']
                phone_no = request.POST['phone_no']
                no_of_guests = request.POST['number-of-guests']
                destination = request.POST.get('destination', '')
                datefrom = request.POST['datetime']
                dateto = request.POST['datetime1']
                message = request.POST['message']


                #send email
                subject = "Booking request from " + name
                email_body = f"Name: {name}\nEmail: {email}\nPhone No: {phone_no}\nDestination:{destination} \nNumber of Guests: {no_of_guests}\nFrom : {datefrom} to {dateto}\n\nMessage:\n{message}"
                send_mail(
                subject,
                email_body,
                EMAIL_HOST_USER,
                ["ignit3graphics@gmail.com","adrielngugim@gmail.com"]

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
                context = {
                'destination': destination,
                'name':name
                }
                
                

                return render(request, 'booking.html',context )
        else:
                context = {
                'destination': destination
                }
                
                return render(request, 'booking.html', context)
                
        
       

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send email
        subject = "New message from " + name
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
        send_mail(subject, email_body, EMAIL_HOST_USER, ["ignit3graphics@gmail.com","adrielngugim@gmail.com"])
        
        message2 = f"Thank you for reaching out to Alamaya Adventures Limited! We have received your message and appreciate your inquiry.\n\nOur team is reviewing it and will respond soon.\n\nThank you for your patience, and we look forward to connecting with you shortly.\n\nBest regards,\nSamuel Ngugi\nAlamaya Adventures Limited"

        send_mail("Thank you for contacting us!", message2, EMAIL_HOST_USER, [email])
        
        return render(request, 'contact.html',{} )
    else:           
        return render(request, 'contact.html', {})
            
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



