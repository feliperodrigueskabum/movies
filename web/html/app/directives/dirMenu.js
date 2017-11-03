'use strict';

angular.module('app')
.directive('ngNav', ['loginService', function(loginService) {
	return {
		restrict:'A',
		template:  '<ul class="nav nav-tabs" ng-if="ta_logado()"><li><a href="#/home">Inicio</a></li><li><a href="#/cadastro">Cadastrar</a></li><li><a href="#/listagem">Ver produtos</a></li><li id="menu_sair"><a href="" ng-click="logout()">sair</a></li></ul>',
		link: function(scope, element, attrs) {
			scope.logout=function(){
				loginService.logout();
			}
			scope.ta_logado = function() {
				return loginService.islogged();
			}
		}
	}	
}]);
