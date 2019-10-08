from django.db import migrations
import gnosis.eth.django.models



class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0024_delete_internaltx'),
    ]

    operations = [
        migrations.AddField(
            model_name='SafeCreation2',
            name='to',
            field=gnosis.eth.django.models.EthereumAddressField(null=True)
        ),
    ]
