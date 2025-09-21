from django.db import models

# Create your models here.


class Listing(models.Model):

    class Meta:
        db_table = 'listing'

    def __str__(self):
        return f"Listing {self.listing_id}"


class Booking(models.Model):

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return f"Booking {self.booking_id}"


class Review(models.Model):

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review {self.review_id}"
