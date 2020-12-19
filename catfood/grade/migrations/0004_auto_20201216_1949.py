# Generated by Django 3.1.2 on 2020-12-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20201216_1914'),
        ('grade', '0003_auto_20201211_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
        migrations.AlterField(
            model_name='gradeproportion',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course.course'),
        ),
    ]