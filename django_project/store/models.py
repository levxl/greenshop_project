from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    amount = models.CharField("Количество", max_length=20)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Flowers(models.Model):
    title = models.TextField("Название", max_length=250, blank=True)
    price = models.CharField("Цена", max_length=50, blank=True)
    img = models.ImageField("Изоброжения", upload_to="flowers/")
    description = models.TextField("Описание", max_length=500, blank=True)
    url = models.SlugField(max_length=130, unique=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Растения'
        verbose_name_plural = 'Растения'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    flowers = models.ForeignKey(Flowers, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"