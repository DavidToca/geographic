from django.db import migrations, models
import django.db.models.deletion

def create_continent(apps, schema_editor):
    Continent = apps.get_model("continents", "Continent")

    Continent.objects.create(name="asia", color="#EE65EE", translate="asia")
    Continent.objects.create(name="américa", color="#000000", translate="america")
    Continent.objects.create(name="antártida", color="#FFFF00", translate="antarcticasia")
    Continent.objects.create(name="europa", color="#F1D142", translate="europe")
    Continent.objects.create(name="áfrica", color="#F04261", translate="africa")
    Continent.objects.create(name="oceanía", color="#EE65DD", translate="oceania")


class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('countries', '0002_auto_20180110_2018'),
    ]

    operations = [
        migrations.RunPython(create_continent),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='continents.Continent'),
            preserve_default=False,
        ),
    ]
