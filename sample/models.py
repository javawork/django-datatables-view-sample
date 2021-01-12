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

    age = models.CharField(
        verbose_name='age',
        max_length=8,
    )

    tm = models.CharField(
        verbose_name='tm',
        max_length=8,
    )

    g = models.CharField(
        verbose_name='g',
        max_length=8,
    )

    gs = models.CharField(
        verbose_name='gs',
        max_length=8,
    )

    mp = models.CharField(
        verbose_name='mp',
        max_length=8,
    )

    fg = models.CharField(
        verbose_name='fg',
        max_length=8,
    )

    fga = models.CharField(
        verbose_name='fga',
        max_length=8,
    )

    fgp = models.CharField(
        verbose_name='fgp',
        max_length=8,
    )

    threep = models.CharField(
        verbose_name='threep',
        max_length=8,
    )

    threepa = models.CharField(
        verbose_name='threepa',
        max_length=8,
    )

    threepp = models.CharField(
        verbose_name='threepp',
        max_length=8,
    )

    twop = models.CharField(
        verbose_name='twop',
        max_length=8,
    )

    twopa = models.CharField(
        verbose_name='twopa',
        max_length=8,
    )

    twopp = models.CharField(
        verbose_name='twopp',
        max_length=8,
    )

    efgp = models.CharField(
        verbose_name='efgp',
        max_length=8,
    )

    ft = models.CharField(
        verbose_name='ft',
        max_length=8,
    )

    fta = models.CharField(
        verbose_name='fta',
        max_length=8,
    )

    ftp = models.CharField(
        verbose_name='ftp',
        max_length=8,
    )

    orb = models.CharField(
        verbose_name='orb',
        max_length=8,
    )

    drb = models.CharField(
        verbose_name='drb',
        max_length=8,
    )

    trb = models.CharField(
        verbose_name='trb',
        max_length=8,
    )

    ast = models.CharField(
        verbose_name='ast',
        max_length=8,
    )

    stl = models.CharField(
        verbose_name='stl',
        max_length=8,
    )

    blk = models.CharField(
        verbose_name='blk',
        max_length=8,
    )

    tov = models.CharField(
        verbose_name='tov',
        max_length=8,
    )

    pf = models.CharField(
        verbose_name='pf',
        max_length=8,
    )

    pts = models.CharField(
        verbose_name='pts',
        max_length=8,
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NBA'
        verbose_name_plural = 'NBA'
