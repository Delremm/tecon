angular.module('teconApp.controllers', []).controller(
        'CreateTestCntl', ['$scope', '$rootScope', 'testManager', function($scope, $rootScope, $eval, testManager) {
    $scope.new_test_data = {
        main_image_url: '',
        questions: [
            {
                title: "",
                variants: [
                    {
                        text: "",
                        is_answer: false
                    },
                ]
            },
        ]
    }
    $scope.add_variant = function(index){
        var variant = {
            text: "",
            is_answer: false
        };
        $scope.new_test_data.questions[index].variants.push(variant);
    }
    $scope.add_question = function(questions){
        var question = {
            title: "",
            variants: [
                {
                    text: "",
                    is_answer: false
                },
            ]
        };
        $scope.new_test_data.questions.push(question);
    };
    $scope.remove_question = function(question) {
        var questions = $scope.new_test_data.questions;
        for (var i = 0, ii = questions.length; i < ii; i++) {
          if (question === questions[i]) {
            questions.splice(i, 1);
          }
        }
    };
    $scope.remove_variant = function(variant, question){
        var questions = $scope.new_test_data.questions;
        for (var i = 0, ii = questions.length; i<ii; i++) {
            if (question === questions[i]) {
                var variants = questions[i].variants;
                for (var j=0, jj=variants.length; j<jj; j++) {
                    if (variant === variants[j]) {
                        variants.splice(j, 1);
                    }
                }
            }
        }
    };
    $scope.remove_main_image = function(img_model){
        $scope.new_test_data.main_image_url = '';
        $scope.$digest();
    }

}]).controller('TestDetailsCtrl', ['$scope', function($scope){
    /*
    test_data -- dict with "questions" key which contains list of questions
    */
    $scope.test_data = JSON.parse(test_data);
    /* answers contains position of variant in variants array at position of question(questions array) 
    e.g [2,1,0,1] --- answer to  the first question is third variant with index 2 of variants array to this question
    answer to the second question is second variant with index 1. to the third question the answer is fist variant.
    */
    $scope.answers = [];
    $scope.result = '';
    function get_right_answer(question_num){
        var question = $scope.test_data.questions[question_num];
        var answer = {
            index: '',
            value: ''
        };
        for (i in question.variants){
            if (question.variants[i].is_answer){
                answer.value = question.variants[i].text;
                answer.index = i;
            }
        };
        return answer
    };
    function all_answered(){
        var questions_num = $scope.test_data.questions.length;
        var answers = [];
        for (i in $scope.answers){
            if ($scope.answers[i]){
                answers.push($scope.answers[i]);
            }
        };
        if (questions_num == answers.length){
            return true
        }
        else{
            return false
        }
    }
    $scope.check_answers = function(){
        var errors = []
        for (answer_i in $scope.answers){
            if ($scope.test_data.questions[answer_i].variants[parseInt($scope.answers[answer_i])]){
                if (get_right_answer(answer_i).index != $scope.answers[answer_i]){
                    var user_answer = {
                        question: answer_i,
                        right: get_right_answer(answer_i).index,
                        users: $scope.answers[answer_i]
                    };
                    errors.push(user_answer);
                };
            }
        }
        var questions_num = $scope.test_data.questions.length;
        if (all_answered()){
            $scope.result = ['Верно ', questions_num-errors.length, ' из ', questions_num].join("");
        }
        else {
            $scope.result = 'Не на все вопросы даны ответы.';
        }
        $scope.checked = true;
    }
}]).controller(
        'EditTestCntl', ['$scope', '$rootScope', 'testManager', function($scope, $rootScope, $eval, testManager) {
    $scope.new_test_data = JSON.parse(test_data);
    $scope.add_variant = function(index){
        var variant = {
            text: "",
            is_answer: false
        };
        $scope.new_test_data.questions[index].variants.push(variant);
    }
    $scope.add_question = function(questions){
        var question = {
            title: "",
            variants: [
                {
                    text: "",
                    is_answer: false
                },
            ]
        };
        $scope.new_test_data.questions.push(question);
    };
    $scope.remove_question = function(question) {
        var questions = $scope.new_test_data.questions;
        for (var i = 0, ii = questions.length; i < ii; i++) {
          if (question === questions[i]) {
            questions.splice(i, 1);
          }
        }
    };
    $scope.remove_variant = function(variant, question){
        var questions = $scope.new_test_data.questions;
        for (var i = 0, ii = questions.length; i<ii; i++) {
            if (question === questions[i]) {
                var variants = questions[i].variants;
                for (var j=0, jj=variants.length; j<jj; j++) {
                    if (variant === variants[j]) {
                        variants.splice(j, 1);
                    }
                }
            }
        }
    };
    $scope.remove_main_image = function(img_model){
        $scope.new_test_data.main_image_url = '';
        $scope.$digest();
    }

}]);
