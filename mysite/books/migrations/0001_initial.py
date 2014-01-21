# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('first_name', models.CharField(max_length=30),), ('last_name', models.CharField(max_length=40),), ('email', models.EmailField(max_length=75),)],
            bases = (models.Model,),
            options = {},
            name = 'Author',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=30),), ('address', models.CharField(max_length=50),), ('city', models.CharField(max_length=60),), ('state_province', models.CharField(max_length=30),), ('country', models.CharField(max_length=50),), ('website', models.URLField(),)],
            bases = (models.Model,),
            options = {},
            name = 'Publisher',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('title', models.CharField(max_length=100),), ('publisher', models.ForeignKey(to='books.Publisher', to_field=u'id'),), ('publication_date', models.DateField(),), ('authors', models.ManyToManyField(to='books.Author'),)],
            bases = (models.Model,),
            options = {},
            name = 'Book',
        ),
    ]
