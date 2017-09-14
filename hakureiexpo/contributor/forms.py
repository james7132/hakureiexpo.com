from django import forms

from contributor.models import Contributor


class ContributorSignupForm(forms.Form):
    display_name = forms.CharField(max_length=30)

    def signup(self, request, user):
        user.contributor.display_name = self.cleaned_data['display_name']
        user.save()
