# Generated by Django 4.2.2 on 2024-05-06 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=300)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("BKASH", "BKASH"),
                            ("NAGAD", "NAGAD"),
                            ("ROCKET", "ROCKET"),
                            ("SSL-COMMERZ", "SSL-COMMERZ"),
                            ("CASH-ON-DELIVERY", "CASH-ON-DELIVERY"),
                        ],
                        max_length=300,
                    ),
                ),
                ("transaction_id", models.CharField(default="0", max_length=100)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("total_amount", models.CharField(default=0, max_length=50)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("HOLD", "HOLD"),
                            ("DELIVERED", "DELIVERED"),
                            ("IN-DELIVERY", "IN-DELIVERY"),
                            ("CANCLED", "CANCLED"),
                        ],
                        default="PENDING",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]