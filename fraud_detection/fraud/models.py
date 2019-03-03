from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Account_holder(models.Model):
    acc_no = models.BigIntegerField(primary_key=True,validators=[MaxValueValidator(9999999999),MinValueValidator(10000000000)])
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    balance = models.FloatField(max_length=50,blank=True,null=True)
    date_of_opening = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    EDUCATION = (
        ("JD","JD"),
		("High School","High School"),
		("Associate","Associate"),
		("MD","MD"),
		("Masters","Masters"),
		("PhD","PhD"),
		("College","College"),
    )
    education = models.CharField(max_length=10, choices=EDUCATION, blank=True, null=True)
    OCCUPATION = (
        ("machine-op-inspct","machine-op-inspct"),
    	("prof-specialty","prof-specialty"),
    	("tech-support","tech-support"),
    	("exec-managerial","exec-managerial"),
    	("sales","sales"),
    	("craft-repair","craft-repair"),
    	("Transport-moving","Transport-moving"),
    	("other-service","other-service"),
    	("priv-house-serv","priv-house-serv"),
    	("armed-forces","armed-forces"),
    	("adm-clerical","adm-clerical"),
    	("protective-serv","protective-serv"),
    	("handlers-cleaners","handlers-cleaners"),
    	("farming-fishing","farming-fishing"),
    )
    occupation = models.CharField(max_length=10, choices=OCCUPATION, blank=True, null=True)
    capital_gains = models.CharField(max_length=10, blank=True, null=True)
    capital_loss = models.CharField(max_length=10, blank=True, null=True)


class Insurance(models.Model):
    acc_no = models.ForeignKey(Account_holder,related_name="insurance",on_delete=models.CASCADE)

    policy_no = models.BigIntegerField(validators=[MaxValueValidator(99999999),MinValueValidator(99999)], blank=True, null=True)

    INSUARANCE = (
        ("Car Insurance", "Car"),
        ("Life Insurance", "Life"),
        ("Health Insurance","Health"),
        ("Fire Insurance","Fire"),
        ("Travel Insurance","Travel"),
    )
    type = models.CharField(max_length=20,choices=INSUARANCE)

    STATE = (
        ("Maharashtra", "Maharashtra"),
        ("Gujarat", "Gujarat"),
        ("Karnataka", "Karnataka"),
    )
    policy_state = models.CharField(max_length=20,choices=STATE)

    annual_premium = models.IntegerField(null=True,blank=True)

    incident_date = models.DateField(blank=True, null=True)

    INCIDENT_TYPE = (
        ("Multi-vehicle Collision","Multi-vehicle Collision"),
    	("Single Vehicle Collision","Single Vehicle Collision"),
    	("Vehicle Theft","Vehicle Theft"),
    	("Parked Car","Parked Car"),
    )
    incident_type = models.CharField(max_length=20,choices=INCIDENT_TYPE,null=True,blank=True)

    COLLISION_TYPE = (
        ("Rear Collision","Rear Collision"),
    	("Side Collision","Side Collision"),
    	("Front Collision","Front Collision"),
    	("Top Collision","?"),
    )
    collision_type = models.CharField(max_length=20,choices=COLLISION_TYPE,null=True,blank=True)

    SEVERITY = (
        ("Minor Damage","Minor Damage"),
    	("Total Loss","Total Loss"),
    	("Major Damage","Major Damage"),
    	("Trivial Damage","Trivial Damage"),
    )
    severity = models.CharField(max_length=20,choices=SEVERITY,null=True,blank=True)

    AUTHORITIES =  (
        ("Police","Police"),
    	("Fire","Fire"),
    	("Other","Other"),
    	("Ambulance","Ambulance"),
    	("None","None"),
    )
    authorities = models.CharField(max_length=20,choices=AUTHORITIES,null=True,blank=True)

    STATE = (
        ("Maharashtra", "Maharashtra"),
        ("Goa", "Goa"),
        ("Punjab", "Punjab"),
        ("Delhi","Delhi"),
        ("Karnataka","Karnataka"),
        ("Bihar","Bihar"),
        ("Kerela","Kerela"),
    )
    state = models.CharField(max_length=20,choices=STATE,null=True,blank=True)

    CITY = (
        ("Mumbai","Mumbai"),
        ("Kolkata","Kolkata"),
        ("Bangalore","Bangalore"),
        ("Patna","Patna"),
        ("Lucknow","Lucknow"),
        ("Amritsar","Amritsar"),
    )
    city = models.CharField(max_length=20,choices=CITY,null=True,blank=True)

    incident_hour = models.IntegerField(max_length=20,null=True,blank=True)

    no_of_vehicles = models.IntegerField(null=True,blank=True)

    DAMAGE = (
        ("?","?"),
        ("Y","YES"),
        ("N","NO"),
    )
    property_damage = models.CharField(max_length=20,choices=DAMAGE,null=True,blank=True)

    injuries = models.IntegerField(null=True,blank=True)

    witnesses = models.IntegerField(null=True,blank=True)

    police_report_available = models.IntegerField(null=True,blank=True)

    total_claim = models.FloatField(max_length=50,null=True,blank=True)

    injury_claim = models.FloatField(max_length=50,null=True,blank=True)

    property_claim = models.FloatField(max_length=50,null=True,blank=True)

    vehicle_claim = models.FloatField(max_length=50,null=True,blank=True)

    BRAND = (
        ("Suburu","Suburu"),
    	("Dodge","Dodge"),
    	("Saab","Saab"),
    	("Nissan","Nissan"),
    	("Chevrolet","Chevrolet"),
    	("Ford","Ford"),
    	("BMW","BMW"),
    	("Toyota","Toyota"),
    	("Audi","Audi"),
    	("Accura","Accura"),
    	("Volkswagen","Volkswagen"),
    	("Jeep","Jeep"),
    	("Mercedes","Mercedes"),
    	("Honda","Honda"),
    )
    vehicle_brand = models.CharField(max_length=20,choices=BRAND,null=True,blank=True)

    MODEL = (
    	("MDX","MDX"),
        ("RAM","RAM"),
        ("Wrangler","Wrangler"),
        ("Neon","Neon"),
        ("A3","A3")  ,
    	("Jetta","Jetta"),
    	("Passat","Passat"),
    	("A5","A5"),
    	("Legacy","Legacy"),
    	("Pathfinder","Pathfinder"),
    	("Malibu","Malibu" ),
    	("92x","92x"    ),
    	("Camry","Camry"  ),
    	("Forrestor","Forrestor"),
    	("95","95"  ),
    	("E400","E400"),
    	("F150","F150"),
    	("Grand Cherokee","Grand Cherokee"),
    	("93","93"),
    	("Maxima","Maxima"  ),
    	("Escape","Escape"  ) ,
    	("Tahoe","Tahoe"    ),
    	("Ultima","Ultima"   ),
    	("X5","X5"       ),
    	("Silverado","Silverado"),
    	("Civic","Civic" ),
    	("Highlander","Highlander"),
    	("Fusion","Fusion"),
    	("Impreza","Impreza"),
    	("ML350","ML350"),
    	("Corolla","Corolla"),
    	("TL","TL"),
    	("CRV","CRV"),
    	("3 Series","3 Series"),
    	("C300","C300"),
    	("X6","X6"),
    	("M5","M5"),
    	("Accord","Accord"),
    	("RSX","RSX"),

    )
    vehicle_model = models.CharField(max_length=20,choices=MODEL,null=True,blank=True)

    year_of_manufacture = models.IntegerField(null=True,blank=True)

    RELATION = (
        ("own-child","own-child"),
    	("other-relative","other-relative"),
    	("not-in-family","not-in-family"),
    	("husband","husband"),
    	("wife","wife"),
    	("unmarried","unmarried"),
    )
    relation = models.CharField(max_length=20,choices=RELATION,null=True,blank=True)
