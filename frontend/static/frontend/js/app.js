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
}).directive('answerInput', function factory($rootScope){
    return {
        restrict: 'A',
        scope: {
            answers: '=',
            thisQuestionType: '=',
            questionTypes: '='
        },
        link: function(scope, element, attrs) {
            if (scope.thisQuestionType.title === scope.questionTypes[0].title){
                attrs.$set('type', 'radio');
            }
            else {
                attrs.$set('type', 'checkbox');
            }
            element.bind('click', function(){
                if (scope.thisQuestionType.title === scope.questionTypes[0].title){
                    scope.answers[attrs.questionIndex] = [attrs.variantIndex];
                }
                else {
                    console.log(scope.answers[attrs.questionIndex] instanceof Array);
                    if (scope.answers[attrs.questionIndex] instanceof Array){
                        var i = scope.answers[attrs.questionIndex].indexOf(attrs.variantIndex);
                        console.log('ww');
                        if (i != -1) {
                            scope.answers[attrs.questionIndex].splice(i, 1);
                        }
                        else{
                            scope.answers[attrs.questionIndex].push(attrs.variantIndex);
                        }
                    }
                    else {
                        scope.answers[attrs.questionIndex] = [attrs.variantIndex];       
                    }
                }
                $rootScope.$digest();
                //console.log(attrs.variantIndex);
            })
        }
    }
});
