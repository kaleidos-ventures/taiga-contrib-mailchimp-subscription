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

import mailchimp
import logging

logger = logging.getLogger(__name__)


def _get_mailchimp_api(mailchimp_api_key):
    return mailchimp.Mailchimp(mailchimp_api_key)


def suscribe_user(user, newsletter_id, mailchimp_api_key):
    m = _get_mailchimp_api(mailchimp_api_key)
    try:
        m.lists.subscribe(id=newsletter_id,
            email={"email": user.email}, double_optin=False)
    except Exception as e:
        logger.error("[Mailchimp] error on subscription: {}".format(str(e)))


def unsuscribe_user(user, newsletter_id, mailchimp_api_key):
    m = _get_mailchimp_api(mailchimp_api_key)
    try:
        m.lists.unsubscribe(id=newsletter_id,
            email={"email": user.email}, send_goodbye=False)
    except Exception as e:
        logger.error("[Mailchimp] error on unsubscription: {}".format(str(e)))
