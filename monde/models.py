from django.db import models
import jsonfield


class Product(models.Model):
    """
    mondebro , crawler를 참고하여 sync 맞춘 후 서비스에서 이 모델을 기준으로 사용합니다.
    """
    db_id = models.PositiveIntegerField(unique=True, help_text="for sync")
    shopping_mall = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    product_url = models.URLField()
    product_image_url = models.URLField(help_text="상품 이미지 url", null=True)
    price = models.IntegerField(help_text='db로 옮기면서 integer로 바꿈')

    class Meta:
        managed = False
        db_table = 'monde_product'


class ProductCategories(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="categories")
    shape_result = jsonfield.JSONField()  # detail 포함, cover 포함.
    type_result = jsonfield.JSONField()
    charm_result = jsonfield.JSONField()
    deco_result = jsonfield.JSONField()
    pattern_result = jsonfield.JSONField()
    colors = jsonfield.JSONField()

    class Meta:
        managed = False
        db_table = 'monde_productcategories'
