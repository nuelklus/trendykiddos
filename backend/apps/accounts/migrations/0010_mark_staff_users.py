from django.db import migrations


def mark_staff_users(apps, schema_editor):
    User = apps.get_model("accounts", "User")
    User.objects.filter(role="STAFF").update(is_staff=True)
    User.objects.filter(is_superuser=True).update(is_staff=True)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_user_is_staff"),
    ]

    operations = [
        migrations.RunPython(mark_staff_users, migrations.RunPython.noop),
    ]
