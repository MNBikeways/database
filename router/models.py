from django.contrib.gis.db import models


# Here is the Hennepin County Street Centerlines table

#the shapefile has EPSG:26915 crs
class HennepinStreets(models.Model):
    object_id = models.IntegerField()
    street_name = models.CharField(max_length=83)
    cost = models.FloatField()
    join_id = models.IntegerField()

    source = models.IntegerField(null=True,blank=True)
    target = models.IntegerField(null=True,blank=True)

    the_geom = models.LineStringField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.street_name, str(self.cost))


class MinneapolisStreets(models.Model):
    object_id = models.FloatField()
    street_name = models.CharField(max_length=35)
    speed_lim = models.IntegerField()
    oneway = models.CharField(max_length=2)
    cost = models.FloatField()

    source = models.IntegerField(null=True, blank=True)
    target = models.IntegerField(null=True,blank=True)

    the_geom = models.LineStringField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.street_name, str(self.cost))



class masterbiketrails(models.Model):
    objectid = models.IntegerField()
    source = models.CharField(max_length=20)
    side = models.CharField(max_length=13)
    type = models.CharField(max_length=50)
    jurisdicti = models.CharField(max_length=10)
    active = models.IntegerField()
    notes = models.CharField(max_length=250)
    name = models.CharField(max_length=50)
    fac_id = models.CharField(max_length=50)
    miles = models.FloatField()
    width = models.IntegerField()
    direction = models.CharField(max_length=10)
    grade = models.CharField(max_length=1)
    speed = models.IntegerField()
    fac_qual = models.CharField(max_length=50)
    lighted = models.CharField(max_length=1)
    opperation = models.CharField(max_length=50)
    proposed = models.CharField(max_length=1)
    arterial = models.CharField(max_length=1)
    conn_gap = models.CharField(max_length=1)
    stops = models.IntegerField()
    class_ = models.CharField(max_length=12)
    road_name = models.CharField(max_length=35)
    road_numb = models.CharField(max_length=10)
    road_code = models.CharField(max_length=2)
    road_speed = models.IntegerField()
    road_comm = models.CharField(max_length=1)
    lane_numb = models.IntegerField()
    lane_width = models.IntegerField()
    lane_dir = models.CharField(max_length=10)
    lane_type = models.CharField(max_length=24)
    shld_width = models.FloatField()
    shld_type = models.CharField(max_length=50)
    shld_rumb = models.CharField(max_length=1)
    shld_park = models.CharField(max_length=24)
    shld_bus = models.CharField(max_length=1)
    shape_leng = models.FloatField()
    maintainer = models.CharField(max_length=35)
    install_yr = models.CharField(max_length=16)
    install_or = models.CharField(max_length=32)
    suitabilit = models.CharField(max_length=24)
    shld_date = models.DateField()
    shld_plow = models.CharField(max_length=3)
    shld_drain = models.CharField(max_length=3)
    road_aadt = models.IntegerField()
    road_hcadt = models.CharField(max_length=1)
    surf_type = models.CharField(max_length=25)
    surf_qaul = models.CharField(max_length=25)
    geom = models.LineStringField(srid=26915)
    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.name, str(self.shape_leng))