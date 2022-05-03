# Generated by Django 4.0.3 on 2022-05-03 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('customer_email', models.EmailField(max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default='+', max_length=20, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('comment', models.TextField(blank=True, default='Please put here any comment', null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kiddilycare.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('purchase_price', models.FloatField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('product_main_image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('digital', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('Beauté', 'Beaute'), ('Santé', 'Sante'), ('Accessoires', 'Accessoires'), ('Visage', 'Visage'), ('Corps', 'Corps'), ('Ete', 'Ete'), ('PierresJade', 'PierresJade')], max_length=100, null=True)),
                ('isPromotional', models.CharField(choices=[('Promo', 'Promo'), ('No Promo', 'No Promo')], default='No Promo', max_length=20)),
                ('promotion', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=100, null=True)),
                ('provider_email', models.EmailField(max_length=254, null=True)),
                ('provider_address', models.CharField(blank=True, max_length=200, null=True)),
                ('provider_phone', models.CharField(default='+', max_length=20, null=True)),
                ('provider_activty', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(max_length=500)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kiddilycare.product')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(default='Country', max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kiddilycare.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kiddilycare.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kiddilycare.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kiddilycare.provider'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kiddilycare.order')),
                ('product', models.ForeignKey(default='Product', null=True, on_delete=django.db.models.deletion.SET_NULL, to='kiddilycare.product')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charac', models.CharField(max_length=500)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kiddilycare.product')),
            ],
        ),
    ]
