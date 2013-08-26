function TeconCntl($scope) {
    $scope.qty = 1;
    $scope.cost = 19.95;
    $scope.questions = [
        {
            title: "",
            variants: [
                {
                    text: "",
                    is_answer: false
                },
            ]
        },
    ];
    $scope.add_variant = function(index){
        var variant = {
            text: "",
            is_answer: false
        };
        $scope.questions[index].variants.push(variant);
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
        $scope.questions.push(question);
    };
    $scope.remove_question = function(question) {
        var questions = $scope.questions;
        for (var i = 0, ii = questions.length; i < ii; i++) {
          if (question === questions[i]) {
            questions.splice(i, 1);
          }
        }
    };
    $scope.remove_variant = function(variant, question){
        var questions = $scope.questions;
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
}
