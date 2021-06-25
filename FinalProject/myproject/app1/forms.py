from django import forms


class registerform(forms.Form):
    n_ame=forms.CharField(max_length=30)
    a_ddress=forms.CharField(max_length=50)
    e_mail=forms.CharField(max_length=20)
    p_wd=forms.CharField(max_length=20)


class loginform(forms.Form):
    e_mail=forms.CharField(max_length=20)
    p_wd=forms.CharField(max_length=20)


class adminform(forms.Form):
    a_dministrator=forms.CharField(max_length=30)
    a_dminpwd=forms.CharField(max_length=20)


class recipeform(forms.Form):
    i_tem=forms.CharField(max_length=20)
    p_rice=forms.IntegerField()
    f_ile=forms.ImageField()
