from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from tasks.models import Priority, Category, Tasks, Note, SubTask


class Command(BaseCommand):
    help = 'Populate initial data for Priority, Category, Tasks, Notes, and SubTasks'

    def handle(self, *args, **kwargs):
        self.create_priorities()
        self.create_categories()
        self.create_tasks(10)  # generate 10 tasks with notes + subtasks

    def create_priorities(self):
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for p in priorities:
            Priority.objects.get_or_create(name=p)

        self.stdout.write(self.style.SUCCESS(
            '✔ Priorities created successfully.'
        ))

    def create_categories(self):
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for c in categories:
            Category.objects.get_or_create(name=c)

        self.stdout.write(self.style.SUCCESS(
            '✔ Categories created successfully.'
        ))

    def create_tasks(self, count):
        fake = Faker()
        for _ in range(count):
            task = Tasks.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=Category.objects.order_by("?").first(),
                priority=Priority.objects.order_by("?").first(),
            )

            # Add Notes
            for _ in range(random.randint(1, 3)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

            # Add SubTasks
            for _ in range(random.randint(1, 4)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=3),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                )

        self.stdout.write(self.style.SUCCESS(
            'Fake Tasks, Notes, and SubTasks created successfully.'
        ))