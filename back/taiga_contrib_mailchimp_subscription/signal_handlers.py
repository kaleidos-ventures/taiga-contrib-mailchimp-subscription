# Copyright (C) 2014-2016 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2016 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2016 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2016 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .utils import suscribe_user, unsuscribe_user

from django.conf import settings


def subscribe_to_newsletter(sender, **kwargs):
    user = kwargs["user"]
    suscribe_user(user, settings.MAILCHIMP_NEWSLETTER_ID, settings.MAILCHIMP_API_KEY)


def unsubscribe_from_newsletter(sender, **kwargs):
    user = kwargs["user"]
    request_data = kwargs.get("request_data", None)

    if not request_data:
        return

    unsuscribe = request_data.get("unsuscribe", None)
    if unsuscribe is not None:
        unsuscribe_user(user, settings.MAILCHIMP_NEWSLETTER_ID, settings.MAILCHIMP_API_KEY)
