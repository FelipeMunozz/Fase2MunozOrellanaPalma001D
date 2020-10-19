$(document).ready(function () {
      //Esta es la instruccion para tomar el id del URL detalle.html?id=<identificador>
  var id = location.search
  id = id.substring(id.length -5 ,id.length);
  document.getElementById("prod").value = id;
});