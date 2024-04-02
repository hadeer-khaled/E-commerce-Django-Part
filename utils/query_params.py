from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

def handle_query_params(queryset, params, search_fields):
    page = int(params.get('page', 1))
    limit = int(params.get('limit', 10))
    order_by = params.get('order', None)
    search = params.get('search', None)
    filters = {k: v for k, v in params.items() if k not in ['page', 'limit', 'order', 'search']}

    if page < 1 or limit < 1 or limit > 30:
        raise ValidationError({'detail': 'Invalid pagination parameters'})

    filter_conditions = Q()
    if search and search_fields:
        for field in search_fields:
            filter_conditions |= Q(**{f'{field}__icontains': search})

    if search and not search_fields:
        raise ValidationError({'detail': 'Invalid search parameters'})

    for key, value in filters.items():
        filter_conditions &= Q(**{key: value})

    queryset = queryset.filter(filter_conditions)

    if order_by:
        if order_by.startswith('-'):
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by(order_by)

    paginator = Paginator(queryset, limit)
    try:
        data = paginator.page(page)
    except EmptyPage:
        raise ValidationError({'detail': 'Page not found'})

    return {
        'data': data.object_list,
        'current_page': page,
        'total_pages': paginator.num_pages,
        'total_count': paginator.count
    }
