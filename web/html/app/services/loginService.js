'use strict';
app.factory('loginService',function($http,$location,sessionService){
	return{
		login:function(form,scope){
			var $promise=$http.post('cgi-local/login.cgi',form);
			$promise.then(function(response){
				var valido = response.data.valido;
				var id = response.data.id;
				
				if(valido == "true") {
					sessionService.set('form',valido);
					$location.path('/home');
					scope.msg = "OK";
					console.log(id)
				}else {
					$location.path('/login');
					scope.msg = "Usuário ou senha invalido !";
				}
			});
		},
		logout:function(form) {
			sessionService.destroy('form');
			$location.path('/login');
		},
		islogged:function(){
			if(sessionService.get('form')) return true;
			return false;
		}
	}
});
