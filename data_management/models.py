from django.db import models


PRECISION = 4
THRESHOLD = 0.1 ** PRECISION
CANDIDATES_COUNT = 100


class MyUser(models.Model):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    username = models.CharField(max_length=120, verbose_name='아이디', unique=True)
    name = models.CharField(max_length=30, verbose_name='이름')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

    class Meta:
        managed = False
        db_table = 'category_data_myuser'


class OriginalImage(models.Model):
    assigned_user = models.ForeignKey(MyUser, null=True, blank=True, on_delete=models.CASCADE, related_name='assigned_original_images')
    image_url = models.URLField(max_length=300, null=True)
    valid = models.NullBooleanField(default=False)
    image = models.ImageField(upload_to='original-bag-images-dev', null=True, blank=True)
    s3_image_url = models.URLField(max_length=300, null=True)
    image_review = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'category_data_originalimage'


class CroppedImage(models.Model):
    assigned_user = models.ForeignKey(MyUser, null=True, blank=True, on_delete=models.CASCADE, related_name='assigned_cropped_images')
    origin_source = models.ForeignKey(OriginalImage, related_name='cropped_images', on_delete=models.CASCADE)
    left = models.DecimalField(max_digits=PRECISION + 1, decimal_places=PRECISION)
    top = models.DecimalField(max_digits=PRECISION + 1, decimal_places=PRECISION)
    right = models.DecimalField(max_digits=PRECISION + 1, decimal_places=PRECISION)
    bottom = models.DecimalField(max_digits=PRECISION + 1, decimal_places=PRECISION)
    image = models.ImageField(upload_to='cropped-bag-images-dev', null=True, blank=True)
    image_url = models.URLField(null=True,blank=True, max_length=250, verbose_name='aws s3 이미지 url')

    class Meta:
        managed = False
        db_table = 'category_data_croppedimage'


# class ColorTag(models.Model):
#     color_name = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'category_data_colortag'


class ShapeTag(models.Model):
    shape_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category_data_shapetag'


# class HandleTag(models.Model):
#     handle_name = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'category_data_handletag'

class CoverTag(models.Model):
    cover_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '[3-2] Cover Tag'

    def __str__(self):
        return self.cover_name

class CharmTag(models.Model):
    charm_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category_data_charmtag'


class DecoTag(models.Model):
    deco_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category_data_decotag'


class PatternTag(models.Model):
    pattern_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category_data_patterntag'


class ProductCategories(models.Model):
    version = models.IntegerField(null=True)
    cropped_source = models.ForeignKey(CroppedImage, on_delete=models.CASCADE, related_name='categories')
#     color_source = models.ForeignKey(ColorTag, null=True, on_delete=models.CASCADE)
    shape_source = models.ForeignKey(ShapeTag, null=True, on_delete=models.CASCADE)
    cover_source = models.ForeignKey(CoverTag, null=True, on_delete=models.CASCADE)
    charm_source = models.ForeignKey(CharmTag, null=True, on_delete=models.CASCADE)
#     handle_source = models.ForeignKey(HandleTag, null=True, on_delete=models.CASCADE)
#     deco_source = models.ForeignKey(DecoTag, null=True, on_delete=models.CASCADE)
    pattern_source = models.ForeignKey(PatternTag, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'category_data_categories'
