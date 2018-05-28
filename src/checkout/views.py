from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        # print(request.POST)
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency="usd",
                source=token,
                description="Example charge"
            )
        except stripe.error.CardError as e:
            pass
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)
