app.directive('myDirectiveFile', function ($parse) {
return {
    restrict: 'A',
    link: function(scope, element, attrs) {
        var model = $parse(attrs.myDirectiveFile);
        element.bind('change', function(){
        model.assign(scope, element[0].files[0]);
        scope.$apply();
        //console.log(model.assign(scope, element[0].files[0]));
        //console.log(model.assign(scope, angular.toJson(element[0].files[0])))
        });
      }
    }
});