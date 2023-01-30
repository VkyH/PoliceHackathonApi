from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others')
    ]

    districts = [
        ( 'Bagalkot' , 'Bagalkot' ),
        ( 'Ballari' , 'Ballari' ),
        ( 'Belagavi' , 'Belagavi' ),
        ( 'Bengaluru Rural' , 'Bengaluru Rural' ),
        ( 'Bengaluru Urban' , 'Bengaluru Urban' ),
        ( 'Bidar' , 'Bidar' ),
        ( 'Chamarajanagar' , 'Chamarajanagar' ),
        ( 'Chikkaballapura' , 'Chikkaballapura' ),
        ( 'Chikkamagaluru' , 'Chikkamagaluru' ),
        ( 'Chitradurga' , 'Chitradurga' ),
        ( 'Dakshina Kannada' , 'Dakshina Kannada' ),
        ( 'Davangere' , 'Davangere' ),
        ( 'Dharwad' , 'Dharwad' ),
        ( 'Gadag' , 'Gadag' ),
        ( 'Gulbarga' , 'Gulbarga' ),
        ( 'Hassan' , 'Hassan' ),
        ( 'Haveri' , 'Haveri' ),
        ( 'Kalaburagi' , 'Kalaburagi' ),
        ( 'Kodagu' , 'Kodagu' ),
        ( 'Kolar' , 'Kolar' ),
        ( 'Koppal' , 'Koppal' ),
        ( 'Mandya' , 'Mandya' ),
        ( 'Mysuru' , 'Mysuru' ),
        ( 'Raichur' , 'Raichur' ),
        ( 'Ramanagara' , 'Ramanagara' ),
        ( 'Shivamogga' , 'Shivamogga' ),
        ( 'Tumakuru' , 'Tumakuru' ),
        ( 'Udupi' , 'Udupi' ),
        ( 'Uttara Kannada' , 'Uttara Kannada' ),
        ( 'Vijayapura' , 'Vijayapura' ),
        ( 'Yadgir' , 'Yadgir' ),
    ]


    id = models.AutoField(primary_key=True)
    aadhar_Number=models.CharField(max_length=12)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    # image_url = models.URLField()
    encodings=models.TextField(blank=True,null=True)
    # gender = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField()

    guardian_name=models.CharField(max_length=255)
    guardian_phone_no=models.CharField(max_length=15)

    station_id=models.CharField(max_length=30)
    station_district=models.CharField(max_length=50,choices=districts)

    last_seen_address=models.TextField()

    resolved=models.BooleanField(default=False)



    def __str__(self):
        return self.aadhar_Number


