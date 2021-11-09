from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=10)


class Company(models.Model):
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return ", ".join([company_name.name for company_name in self.name_set.all()])

class CompanyName(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    language = models.ForeignKey(Language, models.DO_NOTHING)


class Tag(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, models.DO_NOTHING)


class CompanyTag(models.Model):
    company = models.ForeignKey(Company, models.DO_NOTHING)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
