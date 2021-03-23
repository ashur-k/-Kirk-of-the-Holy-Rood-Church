from events.models import Events


def payment_bag_contents(request):
    payment_bag = request.session.get('payment_bag', {})
    payment_bag = request.session.get('payment_bag')
    grand_total = payment_bag['total_amount']

    context = {
        'grand_total': grand_total,
    }
    return context
