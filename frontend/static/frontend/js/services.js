angular.module('teconApp.services', []).factory('testManager', function ($rootScope) {
    var _files = [];
    return {
        add: function (file) {
            _files.push(file);
        },
        clear: function () {
            _files = [];
        },
    };
});