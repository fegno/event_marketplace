import razorpay, json
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.events.models import Event
from apps.orders.models import Order, Inquiry
from apps.payment.models import PaymentGateWayResponse


# Create your views here.

class PaymentStatus:
    SUCCESS = "Success"
    FAILURE = "Failure"
    PENDING = "Pending"


def pay(request):
    return render(request, "payment/index.html")


def order_payment(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        try:

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            razorpay_order = client.order.create(
                {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
            )
            # import pdb;pdb.set_trace()
            inquiry = Inquiry.objects.create(event=Event.objects.all().first(), user=request.user)
            order = Order.objects.create(inquiry=inquiry)
            pg = PaymentGateWayResponse.objects.create(
                amount=amount, provider_order_id=razorpay_order["id"], order=order
            )
            pg.save()
            print(f"razorpay order id {razorpay_order['id']}")
            context['callback_url'] = request.build_absolute_uri().strip('payment/') + "/callback/"
            context['razorpay_key'] = settings.RAZORPAY_KEY_ID
            context['pg'] = pg
            # import pdb;pdb.set_trace()
            return render(
                request,
                "payment/payment.html",
                {
                    'callback_url': request.build_absolute_uri().strip('payment/') + "/callback/",
                    'razorpay_key': settings.RAZORPAY_KEY_ID,
                    'pg': pg
                }
            )
        except Exception as e:
            print(e)
            context['messages'] = str(e)

    return render(request, "payment/payment.html", context)

@csrf_exempt
def callback(request):
    context = {}

    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)


    if "razorpay_payment_id" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        print(f"razorpay payment id {payment_id}")

        pg = PaymentGateWayResponse.objects.get(provider_order_id=provider_order_id)
        pg.payment_id = payment_id
        pg.signature_id = signature_id
        pg.save()
        if not verify_signature(request.POST):
            pg.payment_status = PaymentStatus.SUCCESS
            pg.save()
            return render(request, "payment/callback.html", context={"status": pg.payment_status})
        else:
            pg.payment_status = PaymentStatus.FAILURE
            pg.save()
            return render(request, "payment/callback.html", context={"status": pg.payment_status})
    else:
        if request.POST['error']:
            context['error'] = request.POST.get('error')
            return render(request, "payment/callback.html", context)

        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )

        pg = PaymentGateWayResponse.objects.get(provider_order_id=provider_order_id)
        pg.payment_id = payment_id
        pg.payment_status = PaymentStatus.FAILURE
        pg.save()
        context["status"] = pg.payment_status
        return render(request, "payment/callback.html", context)
