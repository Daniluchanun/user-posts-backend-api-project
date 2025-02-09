from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 3  # Default number of items per page
    max_page_size = 10  # Maximum allowed items per page
    page_size_query_param = 'size'  # Query parameter for specifying page size

    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,  # Total number of items
            'total_pages': self.page.paginator.num_pages,  # Total number of pages
            'prev': bool(self.get_previous_link()),  # Is there a previous page?
            'next': bool(self.get_next_link()),  # Is there a next page?
            'data': data  # Current page's data (зробив для себе коменти що до чого)
        })