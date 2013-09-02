angular.module('teconApp.services', []).factory('testManager', ['$http', function ($http) {
    _test_data = '';
    return {
        get_test_data: function(url, condition, callback){
            if (condition){
                $http.get(url).success(function(data) {
                    data.data = JSON.parse(data.data);
                    callback(data.data);
                });
            }
            else {
                var data = {
                    main_image_url: '',
                    questions: [
                        {
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
                            //question type is comming from a global variable
                            type: question_types[0]
                        },
                    ]
                };
                callback(data);
            }
        }
    };
}]);