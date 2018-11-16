
from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, min_length=2,
                               error_messages={
                                   'required': '姓名必填',
                                   'max_length': '姓名不能超过20字符',
                                   'min_length': '姓名不能短于2字符'
                               })
    pwd = forms.CharField(required=True, min_length=5,
                          error_messages={
                              'required':'密码必填',
                              'min_length': '密码不能短于5字符'
                          })
    cpwd = forms.CharField(required=True, min_length=5,
                           error_messages={
                              'required':'密码必填',
                              'min_length': '密码不能短于5字符'
                          })
    email = forms.CharField(required=True,
                            error_messages={
                                'required': '邮箱必填'
                            })

    def clean(self):
        # 先判断用户是否注册
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            raise forms.ValidationError({'username': '该账号已注册，请去登录'})
        # 验证密码
        pwd = self.cleaned_data.get('pwd')
        cpwd = self.cleaned_data.get('cpwd')
        if pwd != cpwd:
            raise forms.ValidationError({'pwd': '两次密码不一致'})
        return self.cleaned_data


class UserAddressForm(forms.Form):
    # 用户地址保存的表单验证
    signer_name = forms.CharField(required=True, error_messages={'required': '收件人必填'})
    address = forms.CharField(required=True, error_messages={'required': '详细地址必填'})
    signer_mobile = forms.CharField(required=True, error_messages={'required': '收件人手机号码必填'})
    signer_postcode = forms.CharField(required=True, error_messages={'required': '邮编必填'})
