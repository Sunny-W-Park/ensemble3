from django import forms
from .models import Post,  Order, Product #,Comment 

class OrderForm(forms.Form):
    author = forms.CharField(max_length =60)
    quantity = forms.IntegerField(max_value = 10,
            widget=forms.TextInput(attrs={"placeholder": "1회 주문 최대 10장"
                })
            )
    email = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder':'Email'})
            )
    phone = forms.CharField(max_length=120)
    message_store = forms.CharField(max_length=256)

#class OrderForm(forms.Form):
#   author = forms.CharField(
#            max_length=60,
#            widget=forms.TextInput(attrs={
#                "class": "form-control",
#                "placeholder": " 이름 또는 닉네임을 적어주세요!"
#                })
#            )
#    quantity  = forms.IntegerField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "주문 수량(1회 주문 최대 10장) "
#                 })
#             )
#    phone = forms.CharField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "휴대폰 번호: 양식 010-OOOO-OOOO "
#                })
#            )
#    message_store  = forms.CharField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "사장님께 보내는 한마디(전체공개) "
#                })
#            )

#class CommentForm(forms.Form):
#    author = forms.CharField(
#            max_length=60,
#            widget=forms.TextInput(attrs={
#                "class": "form-control",
#                "placeholder": "Your Name | 이름을 적어주세요!"
#                })
#            )
#    body = forms.CharField(widget=forms.Textarea(attrs={
#            "class": "form-control",
#            "placeholder": "Leave a comment! | 댓글을 남겨주세요! "
#            })
#        )

