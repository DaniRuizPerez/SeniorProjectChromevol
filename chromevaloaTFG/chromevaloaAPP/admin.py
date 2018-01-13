from django.contrib import admin
from chromevaloaAPP.models import SelUnigeneTable,Read2,SelContigTable,SelUnigeneTable
from chromevaloaAPP.models import Fulllengther2,Cluster2,Read2
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django import forms

#For removing Group 
#admin.site.unregister(Group)
#admin.site.unregister(Site)


admin.site.site_header = _('Chromevaloa Administration')
admin.site.site_title= _('Chromevaloa Administration')


'''

class ReadOnlyPasswordHashWidget(forms.Widget):
    def render(self, name, value, attrs):
        encoded = value
        final_attrs = self.build_attrs(attrs)

        if not encoded or encoded == UNUSABLE_PASSWORD:
            summary = mark_safe("<strong>%s</strong>" % ugettext("No password set."))
        else:
            try:
                hasher = identify_hasher(encoded)
            except ValueError:
                summary = mark_safe("<strong>%s</strong>" % ugettext(
                    "Invalid password format or unknown hashing algorithm."))
            else:
                summary = format_html_join('',
                                           "<strong>{0}</strong>: {1} ",
                                           ((ugettext(key), value)
                                            for key, value in hasher.safe_summary(encoded).items())
                                           )

        return format_html("<div{0}>{1}</div>", flatatt(final_attrs), summary)

class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        super(ReadOnlyPasswordHashField, self).__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        # Always return initial because the widget doesn't
        # render an input field.
        return initial




class UserAdmin(admin.ModelAdmin):
    fieldsets = ( 
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ) 
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'groups')
    password = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

'''

class Cluster2Admin(admin.ModelAdmin):
    list_display = ('idcluster','clusterseq') 
    search_fields = ['idcluster','clusterseq']

admin.site.register(Cluster2,Cluster2Admin)

class Read2Admin(admin.ModelAdmin):
    list_display = ('idread','readseq') 
    search_fields = ['idread','readseq']

admin.site.register(Read2,Read2Admin)


class SelContigTableAdmin(admin.ModelAdmin):
    list_display = ('idcontig','descrip') 
    search_fields = ['idcontig','descrip']

admin.site.register(SelContigTable,SelContigTableAdmin)


class SelUnigeneTableAdmin(admin.ModelAdmin):
    list_display = ('idcontig','descrip') 
    search_fields = ['idcontig','descrip']

admin.site.register(SelUnigeneTable,SelUnigeneTableAdmin)
