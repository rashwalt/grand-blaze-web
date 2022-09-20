# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

from django.core.mail.utils import CachedDnsName, DNS_NAME

from django.core.mail.message import (
    EmailMessage, EmailMultiAlternatives,
    SafeMIMEText, SafeMIMEMultipart,
    DEFAULT_ATTACHMENT_MIME_TYPE, make_msgid,
    BadHeaderError, forbid_multi_line_headers)

from library.zenhan import h2z, KANA

CONVERT_STRINGS = [
 (u'\u00a6',u'\u007c'),#broken bar=>vertical bar
 (u'\u2014',u'\u2015'),#horizontal bar=>em dash
 (u'\u2225',u'\u2016'),#parallel to=>double vertical line
 (u'\uff0d',u'\u2212'),#minus sign=>fullwidth hyphen minus
 (u'\uff5e',u'\u301c'),#fullwidth tilde=>wave dash
 (u'\uffe0',u'\u00a2'),#fullwidth cent sign=>cent sign
 (u'\uffe1',u'\u00a3'),#fullwidth pound sign=>pound sign
 (u'\uffe2',u'\u00ac'),#fullwidth not sign=>not sign
 (u'\uff65',u'\u30fb'),#半角なかぐろ
 (u'\u2721',u''),# ほしまーく。削除するのです。
 (u'\u98ba',u''),
 (u'\xb7', u'\u30fb'),
 (u'\xa9', u''),
]

def unsafe2safe(string):
    for unsafe, safe in CONVERT_STRINGS:
        string = string.replace(unsafe, safe)
    return string

def get_connection(backend=None, fail_silently=False, **kwds):
    path = backend or settings.EMAIL_BACKEND
    try:
        mod_name, klass_name = path.rsplit('.', 1)
        mod = import_module(mod_name)
    except ImportError, e:
        raise ImproperlyConfigured(('Error importing email backend module %s: "%s"'
                                    % (mod_name, e)))
    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured(('Module "%s" does not define a '
                                    '"%s" class' % (mod_name, klass_name)))
    return klass(fail_silently=fail_silently, **kwds)


def send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None):
    connection = connection or get_connection(username=auth_user,
                                    password=auth_password,
                                    fail_silently=fail_silently)
    message = h2z(message, mode=KANA)
    email_message = EmailMessage(subject, message, from_email, recipient_list,
                        connection=connection)
    #email_message.encoding = 'iso-2022-jp'
    email_message.encoding = 'utf-8'
    return email_message.send()


def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
                   auth_password=None, connection=None):
    """
    Given a datatuple of (subject, message, from_email, recipient_list), sends
    each message to each recipient list. Returns the number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    connection = connection or get_connection(username=auth_user,
                                    password=auth_password,
                                    fail_silently=fail_silently)
    messages = []
    for subject, message, sender, recipient in datatuple:
        email_message = EmailMessage(subject, message, sender, recipient)
        email_message.encoding = 'iso-2022-jp'
        messages.append(email_message)
    return connection.send_messages(messages)


def mail_admins(subject, message, fail_silently=False, connection=None,
                html_message=None):
    """Sends a message to the admins, as defined by the ADMINS setting."""
    if not settings.ADMINS:
        return
    mail = EmailMultiAlternatives(u'%s%s' % (settings.EMAIL_SUBJECT_PREFIX, subject),
                message, settings.SERVER_EMAIL, [a[1] for a in settings.ADMINS],
                connection=connection)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')
    mail.send(fail_silently=fail_silently)


def mail_managers(subject, message, fail_silently=False, connection=None,
                  html_message=None):
    """Sends a message to the managers, as defined by the MANAGERS setting."""
    if not settings.MANAGERS:
        return
    mail = EmailMultiAlternatives(u'%s%s' % (settings.EMAIL_SUBJECT_PREFIX, subject),
                message, settings.SERVER_EMAIL, [a[1] for a in settings.MANAGERS],
                connection=connection)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')
    mail.send(fail_silently=fail_silently)
    