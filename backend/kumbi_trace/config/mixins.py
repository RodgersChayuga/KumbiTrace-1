from django.db import models

class County(Enum):
    MOMBASA = "001 Mombasa"
    KWALE = "002 Kwale"
    KILIFI = "003 Kilifi"
    TANA_RIVER = "004 Tana River"
    LAMU = "005 Lamu"
    TAITA = "006 Taita/Taveta"
    GARISSA = "007 Garissa"
    WAJIR = "008 Wajir"
    MANDERA = "009 Mandera"
    MARSABIT = "010 Marsabit"
    ISIOLO = "011 Isiolo"
    MERU = "012 Meru"
    THARAKA = "013 Tharaka-Nithi"
    EMBU = "014 Embu"
    KITUI = "015 Kitui"
    MACHAKOS = "016 Machakos"
    MAKUENI = "017 Makueni"
    NYANDARUA = "018 Nyandarua"
    NYERI = "019 Nyeri"
    KIRINYAGA = "020 Kirinyaga"
    MURANGA = "021 Muranga"
    KIAMBU = "022 Kiambu"
    TURKANA = "023 Turkana"
    POKOT = "024 West Pokot"
    SAMBURU = "025 Samburu"
    TRANSNZOIA = "026 Trans Nzoia"
    UASINGISHU = "027 Uasin Gishu"
    ELGEYO = "028 Elgeyo/Marakwet"
    NANDI = "029 Nandi"
    BARINGO = "030 Baringo"
    LAIKIPIA = "031 Laikipia"
    NAKURU = "032 Nakuru"
    NAROK = "033 Narok"
    KAJIADO = "034 Kajiado"
    KERICHO = "035 Kericho"
    BOMET = "036 Bomet"
    KAKAMEGA = "037 Kakamega"
    VIHIGA = "038 Vihiga"
    BUNGOMA = "039 Bungoma"
    BUSIA = "040 Busia"
    SIAYA = "041 Siaya"
    KISUMU = "042 Kisumu"
    HOMABAY = "043 Homa Bay"
    MIGORI = "044 Migori"
    KISII = "045 Kisii"
    NYAMIRA = "046 Nyamira"
    NAIROBI = "047 Nairobi"


class TimeStampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Erasable(TimeStampable):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Humanifiable(Erasable):
    GENDER_OPTIONS = (
        ("male'", "Male"),
        ('female', 'Female')
    )

    gender = models.CharField(blank=False, choices=GENDER_OPTIONS)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField()
    id_number = models.PositiveIntegerField(blank=True)


class Describeable(Humanifiable):
    BUILDS = (
        ("tall'", "Tall"),
        ("petite'", "Petite"),
        ("heavyset'", "Heavyset"),
        ("slim'", "Slim"),
        ("average'", "Average"),
    )

    COMPLEXIONS = (
        ("dark'", "Dark"),
        ("light'", "Light"),
        ("chocolate'", "Chocolate"),
    )

    ETHNICITIES = (
        ("African'", "African"),
        ("Caucasian'", "Caucasian"),
        ("Asian'", "Asian"),
        ("Indian'", "Indian"),
        ("Arab'", "Arab"),
    )

   AGE_GROUPS = (
        ("child'", "Child (0-12"),
        ("teen'", "Teen (13-19"),
        ("adult'", "Young Adult (20-32"),
        ("middle-aged'", "Middle Aged Adult (32-49"),
        ('old', 'Old Adult (50+')
    )

    AGE_GROUPS = (
        ("child'", "Child (0-12"),
        ("teen'", "Teen (13-19"),
        ("adult'", "Young Adult (20-32"),
        ("middle-aged'", "Middle Aged Adult (32-49"),
        ('old', 'Old Adult (50+')
    )

    age_group = models.CharField(choices=AGE_GROUPS)
    verbose_description = models.TextField()
    height = models.CharField(null=True)
    complexion = models.CharField(null=True, choices=COMPLEXIONS)
    clothing = models.CharField(null=True)
    ethnicity = models.CharField(choices=ETHNICITIES)
    build = models.CharField(null=True, choices=BUILDS)


class Contactable():
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    alt_phone_no = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=15, black=True, null=True)


class Sociable(Contactable):
    x_handle = models.CharField(max_length=155)
    instagram_handle = models.CharField(max_length=155)
    facebook_hanle = models.CharField(max_length=155)
    tiktok_handle = models.CharField(max_length=155)


class Addressable():
        street = models.CharField(max_length=250, blank=True)
    building = models.CharField(max_length=100)
    floor = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)
    estate = models.CharField(max_length=155, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(blank=True, choices=COUNTIES)
    physical_address = models.TextField(blank=True, null=True)


class Locatable(Addressable):
    maps_url = models.URLField()
    maps_code = models.CharField()
    longitude = models.CharField(max_length=75)
    latitude = models.CharField(max_length=75)
