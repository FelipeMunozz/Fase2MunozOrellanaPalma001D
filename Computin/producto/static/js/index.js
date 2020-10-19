
const btn_menu = document.querySelector("#botonMenu");
console.log(btn_menu);

btn_menu.addEventListener("click" , function()
{
    document.getElementById("barra").classList.toggle("active");

})



const btnMarca = document.getElementById("btnMarca");

/*Tab*/
function openPage(pageName, elmnt, color) 
{
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  /*oculta todos los elementos que tiene los div con la clase tabcontent*/
  for (i = 0; i < tabcontent.length; i++)
  {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablink");
  /*elimina a todos los botones su color*/
  for (i = 0; i < tablinks.length; i++) 
  {
    tablinks[i].style.backgroundColor = "";
  }

  /*Muestra el contenido segun el nombre del boton*/
  document.getElementById(pageName).style.display = "block";
  /*se le añade el color al boton*/
  elmnt.style.backgroundColor = color;
}
/*al entrar la pagina hace que clase defaultOpen haga un click en un boton*/
document.getElementById("defaultOpen").click();

