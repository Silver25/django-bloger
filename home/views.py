from django.shortcuts import render, redirect  # redirect by Copilot
from django.contrib import messages
from .forms import NewsletterForm
# Create a view to handle the subscription form submission
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    """
    Renders the Home page
    """

    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(request, messages.SUCCESS, "Your request for newsletter was send! You can soon expect news from us.")

    newsletter_form = NewsletterForm()

    # return render(request, 'home/index.html' by Copilot

    return render(
        request,
        "home/index.html",
        {
            #"home": home,
            # passed above variable into the template context
            "newsletter_form": newsletter_form
        },
    )

# Create a view to handle the subscription form submission
#@csrf_exempt
#def subscribe(request):
#    if request.method == 'POST':
#        email = request.POST['email']
#        # Add code here to save the email or send it to your newsletter service
#        return redirect('home') # by Copilot
#    return render(request, 'home/index.html')