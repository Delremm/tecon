// Declare app level module which depends on filters, and services
'use strict';
angular.module('teconApp', ['teconApp.controllers', 'teconApp.services', 'teconApp.directives']);

angular.module('teconApp.directives', []).directive('upload', function factory($rootScope) {
    return {
        restrict: 'A',
        scope: { imageModel:'=' },
        link: function (scope, element, attrs) {
            $(element).fileupload({
                dataType: 'text',
                done: function (e, data) {
                    scope.imageModel = JSON.parse(data.result);
                    $rootScope.$digest();
                },
                formData: function (form) {
                    return [{
                        name: "csrfmiddlewaretoken",
                        value: document.getElementsByName('csrfmiddlewaretoken')[0].value
                    },]
                },
                disableImageResize: false,
                imageMaxHeight: 350,
            });
        }
    };
});
