var app = angular.module('app', ['ngRoute','ngMaterial']);

app.config(function($routeProvider, $locationProvider)
{
   $routeProvider
   .when('/home', {
      templateUrl : 'app/views/home.html',
      controller  : 'homeCtrl'
   })
   .when('/listagem', {
      templateUrl : 'app/views/listagem.html',
      controller  : 'listagemCtrl'
   })
   .when('/cadastro', {
      templateUrl : 'app/views/cadastro.html',
      controller  : 'cadastroCtrl'

   })
   .when('/login', {
      templateUrl : 'app/views/login.html',
      controller  : 'loginCtrl'
   })
   .otherwise ({ redirectTo: '/home' });
});
app.run(function($rootScope, $location, loginService){
   var routespermission=['/home'];
   $rootScope.$on('$routeChangeStart', function() {
      if (routespermission.indexOf($location.path()) !=1 && !loginService.islogged())
      {
         $location.path('/login');
      }
   });
});