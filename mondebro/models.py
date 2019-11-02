from django.db import models
import jsonfield

class ProductMaster(models.Model):
    """
    crawling 이후 db sync를 통해 옮겨온 상품 원본 정보입니다.
    db_id를 통해 crawler 와 sync를 맞추고, 크롤링 하면서 저장한 이미지를 불러와 product_image 에 옮겨옵니다.
    master 모델을 기반으로 shape, pattern, decoration, charm, 등을 추출합니다. (deco와 charm은 추가적인 논의 필요)
    ready_for_service : 승인 버튼 클릭 시 True 로 바뀌며, main server에서 이 값을 참조하여 sync 할 product를 참고합니다,
    """
    db_id = models.PositiveIntegerField(unique=True, help_text="crawler id")
    name = models.CharField(max_length=100, null=True, blank=True)
    is_valid = models.BooleanField(help_text='크롤링 시 삭제되면 is_valid=False')
    crawler_created_at = models.DateTimeField(blank=True, null=True)
    crawler_updated_at = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shopping_mall = models.IntegerField()
    product_image = models.ImageField(help_text='s3 image')
    product_url = models.URLField(help_text='상품 url')
    is_available = models.BooleanField(default=True, help_text="카테고리 쌓으면서 사용 가능한 상품인지 저장하는 필드")
    ready_for_service = models.BooleanField(default=False, help_text="crop, categories 까지 나오면 True")

    class Meta:
        managed = False
        db_table = 'bro_manager_productmaster'

    @property
    def product_image_url(self):
        return self.product_image.url


class ProductManager(models.Model):
    """
    master 작업 관리하는 모델입니다.
    모든 항목에 대해 태깅이 완료되면 is_completed = True, 승인시 is_approved = True

    """
    master = models.OneToOneField(ProductMaster, on_delete=models.CASCADE, related_name='manager')
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'bro_manager_productmanager'


class Categories(models.Model):
    """
    ProductMaster 와 OneToOne관계인 Categories 모델입니다. 상품 이미지의 카테고리들을 저장합니다.
    categories.models TaggingCategories가 만들어지면 해당 인스턴스가 생성됩니다.
    형식은 json으로 저장되며 shape_result = {'square': 0.8, 'trapezoid': 0.1, 'circle': 0.1}처럼 top3 를 저장합니다.
    단, 손으로 태깅하는 경우는 shape_result = {'square': 1} 처럼 저장됩니다. main server에서 검색시 문제가 발생할 수 있습니다.

    cover의 경우 손 태깅시에는 커버로 구분된 shape 대로 데이터 쌓고, 이후 cover에 대한 트레이닝 결과가 나오면
    shape result 에 square + cover 유무 로 구분한 결과값 저장.
    """
    master = models.OneToOneField(ProductMaster, on_delete=models.CASCADE, related_name="categories")
    shape_result = jsonfield.JSONField() # detail 포함, cover 포함.
    type_result = jsonfield.JSONField()
    # color_result = jsonfield.JSONField() # color 는 crawling 한 상품 색상으로
    charm_result = jsonfield.JSONField()
    deco_result = jsonfield.JSONField()
    pattern_result = jsonfield.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bro_manager_categories'
        app_label = 'mondebro'
