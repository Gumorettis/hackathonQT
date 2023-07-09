import csv
from datetime import date

from django.core.management.base import BaseCommand

from core.app.models import Client, Loan, User


class Command(BaseCommand):
    help = "seed with data"

    def handle(self, *args, **options):
        clients_file = "client.txt"
        with open(clients_file, "r") as clients_file:
            clients_reader = csv.reader(clients_file, delimiter=";")
            for row in clients_reader:
                _, first_name, username, _, income, password = row
                income = int(income)
                user = User(
                    first_name=first_name,
                    username=username,
                )
                user.set_password(password)
                user.save()
                Client.objects.create(user=user, income=income)

        loans_file = "loan.txt"
        with open(loans_file, "r") as loans_file:
            loans_reader = csv.reader(loans_file, delimiter=";")
            for row in loans_reader:
                _, user_id, _, start, end, _ = row
                user_id = int(user_id)
                start = date.fromisoformat(start)
                end = date.fromisoformat(end)
                Loan.objects.create(client_id=user_id, start=start, end=end)
