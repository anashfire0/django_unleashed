from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import mail_managers


class ContactForm(forms.Form):

    FEEDBACK = 'F'
    CORRECTION = 'C'
    SUPPORT = 'S'
    REASON_CHOICES = (
        (FEEDBACK, 'Feedback'),
        (CORRECTION, 'Correction'),
        (SUPPORT, 'Support'),
    )

    email = forms.EmailField(initial='youremail@gmail.com')
    text = forms.CharField(widget=forms.Textarea)

    reason = forms.ChoiceField(
        choices=REASON_CHOICES,
        initial=FEEDBACK)

    def send_mail(self):
        reason = self.cleaned_data.get('reason')
        reason_dict = dict(self.REASON_CHOICES)
        full_reason = reason_dict.get(reason)
        email = self.cleaned_data.get('email')
        text = self.cleaned_data.get('text')
        body = f'Message from : {email}: \n {text}'

        try:
            mail_managers(full_reason, body)
        except:
            self.add_error(
                None,
                ValidationError('could not send an email\n'
                                'extra headers not allowed in email body',
                code='badheader'))
            return False
        else:
            return True
