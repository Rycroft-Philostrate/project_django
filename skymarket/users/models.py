from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = (
        (USER, USER),
        (ADMIN, ADMIN),
    )


class User(AbstractBaseUser):
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите фамилию",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите адрес электронной почты",
    )
    role = models.CharField(
        max_length=5,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name="Роль пользователя",
        help_text="Выберите роль пользователя",
    )
    phone = PhoneNumberField(
        verbose_name="Телефон для связи",
        help_text="Введите номер телефона",

    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Статус аккаунта",
        help_text="Выберите статус аккаунта"
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
