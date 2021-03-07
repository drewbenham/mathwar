from django.db import models

# Create your models here.
class UnitProfile(models.Model):
    name = models.CharField(max_length=200)
    movement = models.IntegerField()
    weapon_skill = models.IntegerField()
    ballistic_skill = models.IntegerField()
    strength = models.IntegerField()
    toughness = models.IntegerField()
    wounds = models.IntegerField()
    attacks = models.IntegerField()
    leadership = models.IntegerField()
    save = models.IntegerField()
    
    @classmethod
    def create(cls, name, movement, weapon_skill, ballistic_skill, 
               strength, toughness, wounds, attacks, leadership,
               save):
        unit = cls(name=name, movement=movement, weapon_skill=weapon_skill,
                   ballistic_skill=ballistic_skill, strength=strength,
                   toughness=toughness, wounds=wounds, attacks=attacks,
                   leadership=leadership, save=save)
        return unit
    
class WeaponProfile(models.Model):
    RAPID_FIRE = 'RF'
    HEAVY = 'H'
    ASSAULT = 'A'
    PISTOL = 'P'
    GRENADE = 'G'
    
    weapon_id = models.ForeignKey(UnitProfile, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=200)
    w_range = models.IntegerField()
    w_type_choices = [
            (RAPID_FIRE, 'Rapid Fire'),
            (HEAVY, 'Heavy'),
            (ASSAULT, 'Assault'),
            (PISTOL, 'Pistol'),
            (GRENADE, 'Grenade')
            ]
    w_type = models.CharField(max_length=15, choices=w_type_choices)
    w_shots = models.IntegerField()
    w_strengh = models.IntegerField()
    