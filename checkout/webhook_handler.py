from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # event listner for Test24 payment
    def handle_test_payment_intent_succeeded(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_test_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
