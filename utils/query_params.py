from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

def handle_query_params(queryset, params, search_fields):
    params = params.copy()
    max_limit = 50
    if params.get('page', 1) == '':
        page = 1
    else:
        page = int(params.get('page', 1))
    if params.get('limit', 10) == '':
        limit = max_limit
    else:
        limit = int(params.get('limit', 10))

    order_by = params.get('order', None)
    search = params.get('search', None)
    filters = {k: v for k, v in params.items() if k not in ['page', 'limit', 'order', 'search']}

    for key, value in list(params.items()):
        if value == '':
            del params[key]

    if page < 1 or limit < 1 or limit > max_limit:
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
        # Return empty array if page is not found
        return {
            'data': [],
            'current_page': 1,
            'total_pages': 1,
            'total_count': 0
        }

    return {
        'data': data.object_list,
        'current_page': page,
        'total_pages': paginator.num_pages,
        'total_count': paginator.count
    }
