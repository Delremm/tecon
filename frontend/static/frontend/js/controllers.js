question_types = [
    {
        type_id: 1,
        title: 'выбор одного варианта',
        description: 'Выбор одного варианта из предложенных, под правильным вариантом поставьте галочку "является ответом"'
    },
    {
        type_id: 2,
        title: 'выбор нескольких вариантов',
        description: 'Выбор одного или нескольких вариантов, под правильными вариантами поставьте галочку'
    }
];
angular.module('teconApp.controllers', []).controller(
        'CreateEditTestCntl', ['$scope', '$rootScope', 'testManager', function($scope, $rootScope, testManager) {
    //$scope.new_test_data = testManager.get_test_data(test_data_exists, test_data_url);
    testManager.get_test_data(test_data_url, test_data_exists, function(data){
        $scope.new_test_data = data;
    });
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
                    is_answer: true
                },
                {
                    text: "",
                    is_answer: false
                },
            ],
            type: $scope.question_types[0]
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
    };
    $scope.question_types = question_types;
    $scope.set_answer = function(variant_i, variant, question_i, question){
        if (question.type.title == question_types[0].title){
            for (var v_i in $scope.new_test_data.questions[question_i].variants){
                var is_answer = false;
                if (v_i == variant_i){
                    is_answer = true;
                }
                $scope.new_test_data.questions[question_i].variants[v_i].is_answer = is_answer;
            }
        }
        else {
            $scope.new_test_data.questions[question_i].variants[variant_i]
            .is_answer = !($scope.new_test_data.questions[question_i].variants[variant_i].is_answer)
        }
    }


}]).controller(
    'TestDetailsCtrl',
    ['$scope', '$http', '$rootScope', 'testManager', function($scope, $http, $rootScope, testManager){
    /*
    test_data -- dict with "questions" key which contains list of questions
    */

    /* answers contains position of variant in variants array at position of question(questions array) 
    e.g [2,1,0,1] --- answer to  the first question is third variant with index 2 of variants array to this question
    answer to the second question is second variant with index 1. to the third question the answer is fist variant.
    */
    //$scope.test_data = testManager.get(test_data_url);
    testManager.get_test_data(test_data_url, test_data_exists, function(data){
      $scope.test_data = data;
    });

    $scope.answers = [];
    $scope.result = '';
    $rootScope.test_checked = false;
    $scope.question_types = question_types;
    function get_right_answer(question_num){
        var question = $scope.test_data.questions[question_num];
        var answer = {
            indexes: [],
            values: []
        };
        for (var i in question.variants){
            if (question.variants[i].is_answer){
                answer.values.push(question.variants[i]);
                answer.indexes.push(i);
            }
        };
        return answer
    };
    function all_answered(){
        /* check if all questions are answered */
        var questions_num = $scope.test_data.questions.length;
        var answers = [];
        //answers must have no "null" elements, this is why "if ($scope.answers[i])" 
        for (i in $scope.answers){
            if ($scope.answers[i]){
                answers.push($scope.answers[i]);
            }
        };
        return (questions_num == answers.length)?true:false;
    }
    $scope.check_answers = function(){
        var errors = [];
        if (all_answered()){
            for (var answer_i in $scope.answers){
                var user_answer = $scope.answers[answer_i]
                var right_answer = get_right_answer(answer_i);
                var user_is_right = true;
                console.log('user_answer: ', user_answer);
                console.log('right_answer: ', right_answer.indexes);
                if (user_answer.length == right_answer.indexes.length) {
                    for (var i in right_answer.indexes) {
                        console.log((user_answer.indexOf(right_answer.indexes[i]) == '-1'));
                        if (user_answer.indexOf(right_answer.indexes[i]) == '-1') {
                            user_is_right = false;
                        }
                    }
                }
                else {
                    user_is_right = false;
                };
                if (!user_is_right) {
                    var wrong_answer = {
                        question: parseInt(answer_i),
                        right_answer: right_answer,
                        user_answer: user_answer
                    }
                    errors.push(wrong_answer);
                }
            }
            var questions_num = $scope.test_data.questions.length;
            $scope.result = {
                text: ['Верно ', questions_num-errors.length, ' из ', questions_num].join(""),
                errors: errors
            }
        }
        else {
            $scope.result = {
                text: 'Не на все вопросы даны ответы.',
                errors: ''
            };
        }
        $rootScope.test_checked = true;
    }
}]);
