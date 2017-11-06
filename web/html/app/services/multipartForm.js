app.factory('multipartForm', ['$http','$rootScope','$location', function($http,$rootScope,$location) {
	return {
		uploadData : function(data, callback){
		  var request = $http({
			method: 'POST',
			url:'../cgi-local/cadastrar.cgi',
			data: data,
			transformRequest: angular.identity,
			headers: {
				'Content-Type' : undefined
			}
		  });
		  request.then(function successCallback(response) {
		  	$rootScope.$broadcast('atualizandoLista', 'id: id');

		  }, function errorCallback(response) {

		  });
		}
	}
}]);