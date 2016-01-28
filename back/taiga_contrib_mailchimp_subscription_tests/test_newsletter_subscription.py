from taiga.auth.signals import user_registered as user_registered_signal
from taiga.users.signals import user_cancel_account as user_cancel_account_signal

from tests import factories as f
from unittest import mock

from django.core import mail

import mailchimp
import pytest
pytestmark = pytest.mark.django_db


def test_user_registry_signal_ok(settings, client):
    user = f.UserFactory.create()
    with mock.patch.object(mailchimp.Lists, 'subscribe') as subscribe_mock_method:
        user_registered_signal.send(sender=user.__class__, user=user)
        subscribe_mock_method.assert_called_once_with(id="Y",
            email={"email": user.email}, double_optin=False)


def test_user_registry_signal_ko(settings, client):
    user = f.UserFactory.create()
    with mock.patch.object(mailchimp.Lists, 'subscribe') as subscribe_mock_method, \
            mock.patch('taiga_contrib_mailchimp_subscription.utils.logger') as mock_logger:
        subscribe_mock_method.side_effect = mailchimp.ListAlreadySubscribedError(
                                     "x@y.com is already subscribed to the list.")
        user_registered_signal.send(sender=user.__class__, user=user)
        subscribe_mock_method.assert_called_once_with(id="Y",
            email={"email": user.email}, double_optin=False)

        mock_logger.error.assert_called_with("[Mailchimp] error on subscription: "
                                       "x@y.com is already subscribed to the list.")


def test_user_cancel_account_signal_ok(settings, client):
    user = f.UserFactory.create()
    with mock.patch.object(mailchimp.Lists, 'unsubscribe') as unsubscribe_mock_method:
        request_data = {'unsuscribe': 1}
        user_cancel_account_signal.send(sender=user.__class__, user=user,
            request_data=request_data)
        unsubscribe_mock_method.assert_called_once_with(id="Y",
            email={"email": user.email}, send_goodbye=False)


def test_user_cancel_account_signal_ok_with_bad_request_data(settings, client):
    user = f.UserFactory.create()
    with mock.patch.object(mailchimp.Lists, 'unsubscribe') as unsubscribe_mock_method:
        request_data = None
        user_cancel_account_signal.send(sender=user.__class__, user=user,
            request_data=request_data)
        assert not unsubscribe_mock_method.called


def test_user_cancel_account_signal_ko(settings, client):
    user = f.UserFactory.create()
    with mock.patch.object(mailchimp.Lists, 'unsubscribe') as unsubscribe_mock_method, \
            mock.patch('taiga_contrib_mailchimp_subscription.utils.logger') as mock_logger:
        unsubscribe_mock_method.side_effect = mailchimp.ListAlreadySubscribedError(
                                           "x@y.com is not subscribed to list test")
        request_data = {'unsuscribe': 1}
        user_cancel_account_signal.send(sender=user.__class__, user=user,
            request_data=request_data)
        unsubscribe_mock_method.assert_called_once_with(id="Y",
            email={"email": user.email}, send_goodbye=False)

        mock_logger.error.assert_called_with("[Mailchimp] error on unsubscription: "
                                       "x@y.com is not subscribed to list test")
