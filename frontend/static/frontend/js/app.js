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
            // array with answers which are arrays of indexes of answers
            answers: '=',
            // question type which is element of global "question_types" 
            thisQuestionType: '=',
            // model reflecting global variable "question_types"
            questionTypes: '='
        },
        link: function(scope, element, attrs) {
            /* If question type is "one answer" then radio, else checkbox "multiple answers"*/
            if (scope.thisQuestionType.title === scope.questionTypes[0].title){
                attrs.$set('type', 'radio');
            }
            else {
                attrs.$set('type', 'checkbox');
            }
            /*
            on click create(or push if exist) list with variants(or a variant if "one answer" type) at question index 
            position of "answers" array.
            if answers = []; after clicking the second answer of third question it will become "[null, null, ['1']]""
            */
            element.bind('click', function(){
                $rootScope.test_checked = false;
                if (scope.thisQuestionType.title === scope.questionTypes[0].title){
                    scope.answers[attrs.questionIndex] = [attrs.variantIndex];
                }
                else {
                    if (scope.answers[attrs.questionIndex] instanceof Array){
                        var i = scope.answers[attrs.questionIndex].indexOf(attrs.variantIndex);
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
            })
        }
    }
}).directive('resultUserAnswer', function factory($compile, $rootScope){
    return {
        restrict: 'A',
        scope: {
            errorQuestion: '=',
            errorAnswer: '=',
            questions: '=',
        },
        link: function(scope, element, attrs) {
            function get_formated_answer(error_answer){
                var local_formated_answer = [];
                for (var i in error_answer){
                    var variant_num = parseInt(scope.errorAnswer[i])+1;
                    var a = '' + variant_num +'. ' + scope.questions[parseInt(scope.errorQuestion)].variants[error_answer[i]].text;
                    local_formated_answer.push(a);
                }
                return local_formated_answer;
            }
            scope.formated_answer = get_formated_answer(scope.errorAnswer);
            scope.$watchCollection('errorAnswer', function(new_val, old_val){
                scope.formated_answer = get_formated_answer(new_val);
            });
            var answer  = angular.element(element);
            
            var answers_t = "<div ng-repeat='ans in formated_answer'>{{ ans }}</div>";
            answer.append(angular.element($compile(answers_t)(scope)));
        }
    }
}).directive('resultRightAnswer', function factory($compile, $rootScope) {
    return {
        restrict: 'A',
        scope: {
            rightAnswer: '=',
        },
        link: function(scope, element, attrs) {
            scope.formated_answer = [];
            for (var i in scope.rightAnswer.indexes){
                var variant_num = parseInt(scope.rightAnswer.indexes[i]) + 1;
                scope.formated_answer[i] = '' + variant_num + '. ' + scope.rightAnswer.values[i].text;
            }
            var answer  = angular.element(element);
            var answers_t = "<div ng-repeat='ans in formated_answer'>{{ ans }}</div>";
            answer.append(angular.element($compile(answers_t)(scope)));
        }
    }
});
