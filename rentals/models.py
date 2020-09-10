from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save


class Product(models.Model):
    COLOR_CHOICES =[("BL", "Black"),
                    ("WH", "White"),
                    ("GY", "Gray"),
                    ("BR", "Browns"),
                    ("GR", "Green"),
                    ("BU", "Blue"),
                    ("PU", "Purple"),
                    ("RE", "Red"),
                    ("OR", "Orange"),
                    ("YE", "Yellow"),
    ]

    THEME_CHOICES =[("NE", "Neon"),
                    ("BW", "Black & White"),
                    ("CR", "Carnival"),
                    ("DS", "Disco"),
                    ("SR", "Soirées"),
                    ("CK", "Cocktail"),
                    ("SH", "Showers"),
                    ("PP", "Pool Parties"),
                    ("FR", "Farewell"),
                    ("OD", "Outdoor"),
                    ("FN", "Fancy"),

    ]

    CATEGORY_CHOICES =[ ("TB", "Tables"),
                        ("CH", "Chairs"),
                        ("GZ", "Arches & Gazebos"),
                        ("TN", "Tents"),
                        ("TA", "Tent Accessories"),
                        ("ST", "Stages"),
                        ("PR", "Projectors & Screens"),
                        ("EF", "Special Effects Equipments"),
                        ("AU", "Audio Systems"),
                        ("LT", "Lighting"),
                        ("LN", "Lenin"),
                        ("HN", "Hangers"),
                        ("GL", "Glasses & Stemware"),
                        ("FO", "Fun Food Equip"),
                        ("FL", "Floral Accessories"),
                        ("CR", "Floors & Carpet"),
                        ("TR", "Serving Trays"),
                        ("WR", "Flatware"),

    ]

    name          = models.CharField(max_length = 50)
    img           = models.ImageField(null=True, blank=True)
    measures      = models.CharField(max_length = 50, null = True, blank = True)
    quantity      = models.IntegerField(null=True, blank = True) #throwing errors
    description   = models.TextField(null = True, blank = True)
    price_per_day = models.FloatField()
    is_rented     = models.BooleanField(default= False)
    category      = models.CharField(max_length=2, choices = CATEGORY_CHOICES, null = True, blank = True)
    color         = models.CharField(max_length=2, choices = COLOR_CHOICES, null = True, blank = True)
    theme         = models.CharField(max_length=2, choices = THEME_CHOICES, null = True, blank = True)


    def __str__(self):
        return "{} {} - ${}/day".format(self.name, self.measures, self.price_per_day)

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'product_id':self.id})
