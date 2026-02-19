import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from apps.drivers.models import Driver
from apps.locations.models import City, State, Country

User = get_user_model()


class Command(BaseCommand):
    help = "Seed: Create many drivers"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--total", type=int, default=50)

    def handle(self, *args, **options) -> None:
        total = options["total"]
        self.stdout.write(self.style.SUCCESS(f"Creating {total} drivers..."))

        cities = list(City.objects.all())
        states = list(State.objects.all())
        countries = list(Country.objects.all())

        # Validar datos mínimos
        if not cities or not states or not countries:
            self.stdout.write(self.style.ERROR("Cities/States/Countries are empty!"))
            return

        for i in range(total):

            username = f"driver{i}"

            # Evita duplicados (idempotente)
            user, created_user = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}_{random.randint(1000,9999)}@example.com",
                    "password": "password123",
                },
            )

            # Si se creó nuevo, le seteamos password correctamente
            if created_user:
                user.set_password("password123")
                user.save()

            # Crear driver si no existe
            driver, created_driver = Driver.objects.get_or_create(
                user_id=user,
                defaults={
                    "phone": f"+56912345{i:03d}",
                    "birth_date": "1990-01-01",
                    "address": f"Fake Street #{i}",
                    "city_id": random.choice(cities),
                    "state_id": random.choice(states),
                    "country_id": random.choice(countries),
                    "vehicle_type": "car",
                    "status": "BRONCE",
                    "is_verified": bool(random.getrandbits(1)),
                    "is_active": True,
                },
            )

            # Si el driver ya existía, no volvemos a pisar archivos
            if created_driver:
                driver.driver_license = ContentFile(b"PDF content", name="license.pdf")
                driver.identification_document = ContentFile(
                    b"PDF content", name="id.pdf"
                )
                driver.social_security_certificate = ContentFile(
                    b"PDF content", name="social.pdf"
                )
                driver.criminal_record_certificate = ContentFile(
                    b"PDF content", name="criminal.pdf"
                )
                driver.save()

        self.stdout.write(self.style.SUCCESS("Seed completed successfully!"))
