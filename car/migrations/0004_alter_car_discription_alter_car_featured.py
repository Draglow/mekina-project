# Generated by Django 5.0 on 2023-12-16 21:47

import ckeditor.fields
import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0003_alter_car_doors_alter_car_fuel_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="discription", field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="car",
            name="featured",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Cruise Control", "Cruise Control"),
                    ("Audio Interface", "Audio Interface"),
                    ("Airbags", "Airbags"),
                    ("Air Conditioning", "Air Conditioning"),
                    ("Seat Heating", "Seat Heating"),
                    ("Alarm System", "Alarm System"),
                    ("ParkAssist", "ParkAssist"),
                    ("Power Steering", "Power Steering"),
                    ("Reversing Camera", "Reversing Camera"),
                    ("Direct Fuel Injection", "Direct Fuel Injection"),
                    ("Auto Start/Stop", "Auto Start/Stop"),
                    ("Wind Deflector", "Wind Deflector"),
                    ("Bluetooth Handset", "Bluetooth Handset"),
                ],
                max_length=200,
            ),
        ),
    ]