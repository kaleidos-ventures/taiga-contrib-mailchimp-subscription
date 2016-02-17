###
# Copyright (C) 2014-2016 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2016 Jesús Espino Garcia <jespinog@gmail.com>
# Copyright (C) 2014-2016 David Barragán Merino <bameda@dbarragan.com>
# Copyright (C) 2014-2016 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# Copyright (C) 2014-2016 Juan Francisco Alcántara <juanfran.alcantara@kaleidos.net>
# Copyright (C) 2014-2016 Xavi Julian <xavier.julian@kaleidos.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# File: mailchimp-subscription.coffee
###
template = """
<a class="close" href="" title="close">
    <span class="icon icon-delete"></span>
</a>
<form>
    <h2 class="title", translate="LIGHTBOX.DELETE_ACCOUNT.SECTION_NAME"></h2>
    <p>
        <span class="question" translate="LIGHTBOX.DELETE_ACCOUNT.CONFIRM"></span>
        <span class="subtitle" translate="LIGHTBOX.DELETE_ACCOUNT.SUBTITLE"></span>
    </p>

    <div class="newsletter">
        <input name="unsuscribe", type="checkbox", id="unsuscribe" />
        <label for="unsuscribe" translate="LIGHTBOX.DELETE_ACCOUNT.NEWSLETTER_LABEL_TEXT"></label>
    </div>

    <div class="options">
        <a class="button-green" href="" title="{{'COMMON.ACCEPT' | translate}}")>
            <span translate="COMMON.ACCEPT"></span>
        <a class="button-red" href="" title="{{'COMMON.CANCEL' | translate}}">
            <span translate="COMMON.CANCEL"></span>
        </a>
    </div>
</form>
"""

decorator = [
    '$delegate',
    '$tgRepo',
    '$tgAuth',
    '$tgLocation',
    '$tgNavUrls',
    'lightboxService',
    ($delegate, $repo, $auth, $location, $navUrls, lightboxService) ->
        directive = $delegate[0]

        directive.template = template
        directive.templateUrl = null

        directive.compile = () ->
            return ($scope, $el, $attrs) ->
                $scope.$on "deletelightbox:new", (ctx, user)->
                    lightboxService.open($el)

                $scope.$on "$destroy", ->
                    $el.off()

                submit = ->
                    unsuscribe = $el.find("input[name='unsuscribe']").is(':checked')
                    params = {}

                    if unsuscribe
                        params["unsuscribe"] = unsuscribe

                    promise = $repo.remove($scope.user, params)

                    promise.then (data) ->
                        lightboxService.close($el)
                        $auth.logout()
                        $location.path($navUrls.resolve("login"))

                    promise.then null, ->
                        console.log "FAIL"

                $el.on "click", ".button-red", (event) ->
                    event.preventDefault()
                    lightboxService.close($el)

                $el.on "click", ".button-green", window.taiga.debounce 2000, (event) ->
                    event.preventDefault()
                    submit()

        return $delegate
]

window.addDecorator("tgLbDeleteUserDirective", decorator)
