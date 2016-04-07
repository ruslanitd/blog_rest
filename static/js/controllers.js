/**
 * Created by ruslan on 07.04.16.
 */
var blogApp = angular.module('blogApp', []);

blogApp.controller('TopicsCtrl', function($scope) {
    $scope.topics = [
        {'name': "Test1"},
        {'name': "Test2"},
        {'name': "Test3"},
        {'name': "Test4"},
    ]
})
