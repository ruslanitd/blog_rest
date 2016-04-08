/**
 * Created by ruslan on 07.04.16.
 */
var blogApp = angular.module('blogApp', []);

blogApp.controller('TopicsCtrl', function($scope, $http) {
    $http.get('http://127.0.0.1:8000/api/').success(function(data, status, headers, config){
        $scope.topics = data;
        console.log(data)
    });
})
