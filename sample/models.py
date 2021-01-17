from django.db import models


# Create your models here.
class Item(models.Model):

    name = models.CharField(
        verbose_name='name',
        max_length=24,
    )

    pos = models.CharField(
        verbose_name='pos',
        max_length=8,
    )

    age = models.FloatField(
        verbose_name='age',
    )

    tm = models.CharField(
        verbose_name='tm',
        max_length=8,
    )

    g = models.IntegerField(
        verbose_name='g',
    )

    gs = models.IntegerField(
        verbose_name='gs',
    )

    mp = models.FloatField(
        verbose_name='mp',
    )

    fg = models.FloatField(
        verbose_name='fg',
    )

    fga = models.FloatField(
        verbose_name='fga',
    )

    fgp = models.FloatField(
        verbose_name='fgp',
    )

    threep = models.FloatField(
        verbose_name='threep',
    )

    threepa = models.FloatField(
        verbose_name='threepa',
    )

    threepp = models.FloatField(
        verbose_name='threepp',
    )

    twop = models.FloatField(
        verbose_name='twop',
    )

    twopa = models.FloatField(
        verbose_name='twopa',
    )

    twopp = models.FloatField(
        verbose_name='twopp',
    )

    ft = models.FloatField(
        verbose_name='ft',
    )

    fta = models.FloatField(
        verbose_name='fta',
    )

    ftp = models.FloatField(
        verbose_name='ftp',
    )

    orb = models.FloatField(
        verbose_name='orb',
    )

    drb = models.FloatField(
        verbose_name='drb',
    )

    trb = models.FloatField(
        verbose_name='trb',
    )

    ast = models.FloatField(
        verbose_name='ast',
    )

    stl = models.FloatField(
        verbose_name='stl',
    )

    blk = models.FloatField(
        verbose_name='blk',
    )

    tov = models.FloatField(
        verbose_name='tov',
    )

    pf = models.FloatField(
        verbose_name='pf',
    )

    pts = models.FloatField(
        verbose_name='pts',
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NBA'
        verbose_name_plural = 'NBA'
