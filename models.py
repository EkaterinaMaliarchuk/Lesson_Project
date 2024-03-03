from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
import math



class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def grant_access(self, user):
        if self.start_date > timezone.now().date():
            # Сначала отсортируем пользователей по количеству уже имеющихся у них групп
            users = list(self.access.all())
            users.sort(key=lambda u: u.group_set.count())

            # Пересобираем группы с учетом ограничений
            groups = Group.objects.filter(product=self)
            min_users = min([group.min_users for group in groups])
            max_users = max([group.max_users for group in groups])

            while users:
                for group in groups:
                    if group.students.count() < max_users:
                        # Определяем количество пользователей, которых можно добавить в группу
                        remaining_capacity = max_users - group.students.count()
                        desired_capacity = min(max_users, max(min_users, len(users) // len(groups)))
                        capacity = min(remaining_capacity, desired_capacity)

                        # Добавляем пользователей в группу
                        group.students.add(*users[:capacity])
                        users = users[capacity:]
                        group.save()
                        break

        # Добавляем пользователя в список доступа
        self.access.add(user)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.title


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    students = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.title
