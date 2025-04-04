# categories/choices.py

class ProductStatus:
    NEW = 'new'
    OLD = 'old'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (OLD, 'Old'),
    ]


class AvailabilityStatus:
    SOLD = 'Sold'
    NOT_SOLD = 'not_sold'
    DELETED = 'deleted'

    AVAILABILITY_CHOICES = [
        (SOLD, 'Sold'),
        (NOT_SOLD, 'Not Sold'),
        (DELETED, 'Deleted'),
    ]
