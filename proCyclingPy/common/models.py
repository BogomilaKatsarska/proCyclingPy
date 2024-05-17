from django.db import models

from proCyclingPy.team_manager.models import TeamManager


class Team(models.Model):
    NAME_MAX_LEN = 50
    CATEGORY_MAX_LEN = 20
    LOGO_MAX_LEN = 300
    ALPECIN = 'Alpecin - Deceuninck'
    ARKEA = 'Arkéa - B & B Hotels'
    ASTANA = 'Astana Qazaqstan Team'
    BAHRAIN = 'Bahrain - Victorious'
    BORA = 'BORA - hansgrohe'
    COFIDIS = 'Cofidis'
    EF = 'EF Education - EasyPost'
    FDJ = 'Groupama - FDJ'
    INEOS = 'INEOS Grenadiers'
    INTERMARCHE = 'Intermarché - Wanty'
    LIDL = 'Lidl - Trek'
    MOVISTAR = 'Movistar Team'
    QUICK_STEP = 'Soudal Quick - Step'
    DSM = 'Team dsm - firmenich'
    POST_NL = 'PostNL'
    JAYCO = 'Team Jayco AlUla'
    VISMA = 'Team Visma | Lease a Bike'
    UAE = 'UAE Team Emirates'

    ONE_ONE = '1.1'
    WORLD_TOUR = 'World Tour'
    TWO_ONE = '2.1'
    TWO_TWO = '2.2'

    TEAMS = (
        (ARKEA, ARKEA),
        (ASTANA, ASTANA),
        (ALPECIN, ALPECIN),
        (BORA, BORA),
        (BAHRAIN, BAHRAIN),
        (COFIDIS, COFIDIS),
        (DSM, DSM),
        (FDJ, FDJ),
        (INEOS, INEOS),
        (INTERMARCHE, INTERMARCHE),
        (JAYCO, JAYCO),
        (LIDL, LIDL),
        (MOVISTAR, MOVISTAR),
        (POST_NL, POST_NL),
        (QUICK_STEP, QUICK_STEP),
        (UAE, UAE),
        (VISMA, VISMA)
    )

    CATEGORIES = (
        (ONE_ONE, ONE_ONE),
        (WORLD_TOUR, WORLD_TOUR),
        (TWO_ONE, TWO_ONE),
        (TWO_TWO, TWO_TWO),
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        choices=TEAMS,
        null=False,
        blank=False,
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )
    manager = models.OneToOneField(
        TeamManager,
        on_delete=models.RESTRICT,
        primary_key=True,
    )
    logo = models.URLField(
        max_length=LOGO_MAX_LEN,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
