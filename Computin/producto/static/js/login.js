$(document).ready(function () {
    
    $("#btnlog").click(function()
    {

            val1 = true;
            val2 = true;
            //Exprecion regular 
            emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
            correo = document.getElementById("secione").value;
            clave = document.getElementById("secionc").value;
            if (emailRegex.test(correo) & correo != "")
            {
               val1 = false;
               document.getElementById("secione").style.border = "green solid 1px"
               document.getElementById("error-email").innerHTML = "";
            }
            
            if(val1)
            {
          
              document.getElementById("error-email").innerHTML = "<i class='fas fa-exclamation-circle'></i>¡Correo Electronico Invalido!";
              document.getElementById("error-email").style.color = "red";
              document.getElementById("error-email").style.left = "5px";
              document.getElementById("error-email").style.width = "300px";
              document.getElementById("secione").style.border = "black solid 1px";
              return false;
          
            }
            if (clave != "")
            {
               val2 = false;
               document.getElementById("secionc").style.border = "green solid 1px"
               document.getElementById("error-clave").innerHTML = "";
            }
            
            if(val2)
            {
          
              document.getElementById("error-clave").innerHTML = "<i class='fas fa-exclamation-circle'></i>¡Ingrese Contraseña!";
              document.getElementById("error-clave").style.color = "red";
              document.getElementById("error-clave").style.width = "300px";
              document.getElementById("secionc").style.border = "black solid 1px";
              return false;
          
            }
            if(val1 == false & val2 == false)
            {
               alert("Inicio De Sesión Exitoso!")
            }
    });

    $("#btnregistrar").click(function()
    {

            val1 = true;
            val2 = true;
            //Exprecion regular 
            emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
            correo = document.getElementById("regiscorreo").value;
            clave = document.getElementById("regisclave").value;
            if (emailRegex.test(correo) & correo != "")
            {
               val1 = false;
               document.getElementById("regiscorreo").style.border = "green solid 1px"
               document.getElementById("error-regiscorreo").innerHTML = "";
            }
            
            if(val1)
            {
          
              document.getElementById("error-regiscorreo").innerHTML = "<i class='fas fa-exclamation-circle'></i>¡Correo Electronico Invalido!";
              document.getElementById("error-regiscorreo").style.color = "red";
              document.getElementById("error-regiscorreo").style.left = "5px";
              document.getElementById("error-regiscorreo").style.width = "300px";
              document.getElementById("regiscorreo").style.border = "black solid 1px";
              return false;
          
            }
            if (clave != "")
            {
               val2 = false;
               document.getElementById("regisclave").style.border = "green solid 1px"
               document.getElementById("error-regisclave").innerHTML = "";
            }
            
            if(val2)
            {
          
              document.getElementById("error-regisclave").innerHTML = "<i class='fas fa-exclamation-circle'></i>¡Ingrese Contraseña!";
              document.getElementById("error-regisclave").style.color = "red";
              document.getElementById("error-regisclave").style.width = "300px";
              document.getElementById("regisclave").style.border = "black solid 1px";
              return false;
          
            }
            if(val1 == false & val2 == false)
            {
               alert("Cuenta Creada con Exitoso!")
            }
    });

  });