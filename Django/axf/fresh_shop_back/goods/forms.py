
from django import forms

from goods.models import GoodsCategory


class GoodsForm(forms.Form):
    name = forms.CharField(required=True, max_length=20,
                           error_messages={
                               'required': '商品名称必填',
                               'max_length': '商品名称长度不能超过20字符'
                           })
    goods_sn = forms.CharField(required=True,
                               error_messages={
                                   'required': '商品数量必填',
                               })
    category = forms.CharField(required=True,
                               error_messages={
                                   'required': '商品分类必填',
                               })
    goods_nums = forms.CharField(required=True,
                               error_messages={
                                   'required': '商品库存必填'
                               })
    market_price = forms.CharField(required=True,
                               error_messages={
                                   'required': '市场价格必填'
                               })
    shop_price = forms.CharField(required=True,
                               error_messages={
                                   'required': '超市价格必填'
                               })
    goods_brief = forms.CharField(required=True,
                                  error_messages={
                                   'required': '商品描述必填'
                               })
    goods_front_image = forms.ImageField(required=False)

    def clean_category(self):
        id = self.cleaned_data.get('category')
        # 获取分类对象
        category = GoodsCategory.objects.filter(pk=id).first()
        return category
