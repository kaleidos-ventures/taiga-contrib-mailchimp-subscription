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
