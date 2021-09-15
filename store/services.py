from .models import Order


def get_order_status_history(order: Order):
    statuses = {}

    for history in order.history.order_by('history_date'):
        if history.order_status.name not in statuses.keys():
            statuses[history.order_status.name] = {
                'date': history.history_date,
                'status': history.order_status.name
            }

    return statuses