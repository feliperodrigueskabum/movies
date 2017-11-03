app.controller('homeCtrl', function($scope,loginService){
	$scope.home = 'teste213231';
});

app.controller('listagemCtrl',['$scope', '$http', 'multipartForm','$location', function($scope,$http,multipartForm,$location) {
	$scope.cadEdi = 'Cadastrar';
	//PREVIEW DA FOTO
	$scope.previewPhoto = function(event){
		var preview = document.querySelector('img');
		var file    = document.querySelector('input[type=file]').files[0];
		var reader  = new FileReader();

		reader.onload = function(e) {
			$scope.$apply(function(){
				$scope.photo = e.target.result;
			})
		}
		reader.readAsDataURL(file);
		$scope.carregarFoto= true;

	}


	//CADASTRANDO
	$scope.submit = function() {
		
		var form = $scope.frm;
		var fd = new FormData();

		fd.append('filme_nome', form.filme_nome);
		fd.append('filme_preco', form.filme_preco);
		fd.append('filme_tipo', form.filme_tipo);
		fd.append('filme_img', form.filme_img);
		fd.append('filme_id',form.filme_id);

		multipartForm.uploadData(fd, function(response){
		});
	}

	
	//LISTANDO
	$scope.carrega = function (){

	  $http({
	      method: 'GET',
	      url: 'cgi-local/listagem.cgi'
	    })
	    .then(function successCallback(response) {
	      $scope.movies = response.data;
	      $scope.excluir = function (id,index,status) {
	      	$http({
	      		method: 'GET',
	      		url: 'cgi-local/listagem.cgi',
	      		params: {funcao: 'excluir', id: id, status: status}
	      	})
	      	.then(function successCallback(response) {
			}, function errorCallback(response) {
				console.log(err);
			});
	      }
	    }, function errorCallback(response) {
	    });
	}

	$scope.carrega();
	$scope.limpar = function() {
		$scope.frm = {filme_nome: "", filme_img:"", filme_preco:"", filme_tipo: ""}

	}

	//PEGANDO O EVENTO PRA ATUALIZAR A LISTA DPS QUE CADASTROU
	$scope.$on('atualizandoLista', function(event, obj){
		$scope.carrega();
		$scope.limpar();
		$scope.carregarFoto= false;
		$scope.cadEdi = 'Cadastrar';
	});

	//TRAZENDO OS CAMPOS PRA ATUALIZAR
	$scope.edit = function (movie) {
		$scope.cadEdi = 'Editar';
		$scope.frm = movie;
		//angular.copy(movie,$scope.frm);
		console.log($scope.frm);
	}
}]);

app.controller('cadastroCtrl', ['$scope', '$http', 'multipartForm','$location', function($scope,$http,multipartForm,$location){
	
}]);
app.controller('loginCtrl', function($scope,loginService){
	$scope.msg="";
	$scope.loginSubmit = function(form) {
		loginService.login(form, $scope);
	}
});