$(document).ready(function(){


    var sel=false;

    $("#tipos").change(function () {

        sel=true;

    });

    $("#creaAnimal").click(function() {

        if($("#recipient-name").val()==''){

            alert("Inserte el nombre de la mascota por favor");
            event.preventDefault();

        }else if($("#recipient-name").val().length>25){

            alert("El nombre es demasiado largo");
            event.preventDefault();

        }else if(validarFormatoFecha($("#date-pick").val())){
            var datos=$("#date-pick").val().split("-");

            if((datos[1]<1)||(datos[1]>12)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();



            } else if((datos[2]<1)||(datos[2]>31)){

                    alert("Introduzca correctamente la fecha de nacimiento por favor");
                    event.preventDefault();

            }else if($("#message-text").val().length>25){

                    alert("La descripcion es demasiado larga");
                    event.preventDefault();

            }else{

                    if(sel==false) {

                        alert("Elija un tipo de animal por favor");
                        event.preventDefault();
                    }

            }

        }else if(!validarFormatoFecha($("#date-pick").val())){

            alert("Introduzca correctamente la fecha de nacimiento por favor");
            event.preventDefault();

        }

    });


    $("#modAnimal").click(function() {


        if($("#recipient-name").val()==''){

            alert("Inserte el nombre de la mascota por favor");
            event.preventDefault();

        }else if($("#recipient-name").val().length>25){

            alert("El nombre es demasiado largo");
            event.preventDefault();

        }else if(validarFormatoFecha($("#date-pick").val())){
            var datos=$("#date-pick").val().split("-");

            if((datos[1]<1)||(datos[1]>12)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();



            } else if((datos[2]<1)||(datos[2]>31)){

                    alert("Introduzca correctamente la fecha de nacimiento por favor");
                    event.preventDefault();

            }else if($("#message-text").val().length>25){

                    alert("La descripcion es demasiado larga");
                    event.preventDefault();

            }

        }else if(!validarFormatoFecha($("#date-pick").val())){

            alert("Introduzca correctamente la fecha de nacimiento por favor");
            event.preventDefault();

        }

    });

    $("#creaTar").click(function(){

        if($("#recipient-nameTar").val()==''){

            alert("Inserte el nombre de la tarea por favor");
            event.preventDefault();

        }else if($("#recipient-nameTar").val().length>30) {

            alert("El nombre de la tarea es demasiado largo");
            event.preventDefault();

        }else if($("#mascota option:selected").val()==''){

            alert("Seleccione una mascota por favor");
            event.preventDefault();

        }else if(validarFormatoFecha($("#date-pickFec").val())) {
            var datos = $("#date-pickFec").val().split("-");

            if ((datos[1] < 1) || (datos[1] > 12)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();


            } else if ((datos[2] < 1) || (datos[2] > 31)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();

            } else if (validarHora($("#date-pick2").val())) {
                var datos2 = $("#date-pick2").val().split(":");

                   if (datos2[0] > 23) {

                    alert("Introduzca correctamente la hora por favor");
                    event.preventDefault();


                   } else if (datos2[1] > 59) {

                    alert("Introduzca correctamente la hora por favor");
                    event.preventDefault();

                   } else if ($("#message-textTar").val().length > 35) {

                    alert("La descripcion es demasiado larga");
                    event.preventDefault();

                    }

            }else if(!validarHora($("#date-pick2").val())) {
                alert("Introduzca una hora correcta por favor");
                event.preventDefault();

            }

        }else if(!validarFormatoFecha($("#date-pickFec").val())){

            alert("Introduzca correctamente la fecha de nacimiento por favor");
            event.preventDefault();

        }

    });

    $("#modTar").click(function(){

        if($("#tarea-input-name").val()==''){

            alert("Inserte el nombre de la tarea por favor");
            event.preventDefault();

        }else if($("#tarea-input-name").val().length>30) {

            alert("El nombre de la tarea es demasiado largo");
            event.preventDefault();

        }else if($("#tarea-select-mascota option:selected").val()==''){

            alert("Seleccione una mascota por favor");
            event.preventDefault();

        }else if(validarFormatoFecha($("#tarea-input-date").val())) {
            var datos = $("#tarea-input-date").val().split("-");

            if ((datos[1] < 1) || (datos[1] > 12)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();


            } else if ((datos[2] < 1) || (datos[2] > 31)) {

                alert("Introduzca correctamente la fecha de nacimiento por favor");
                event.preventDefault();

            } else if (validarHora($("#tarea-input-hour").val())) {
                var datos2 = $("#tarea-input-hour").val().split(":");

                   if (datos2[0] > 23) {

                    alert("Introduzca correctamente la hora por favor");
                    event.preventDefault();


                   } else if (datos2[1] > 59) {

                    alert("Introduzca correctamente la hora por favor");
                    event.preventDefault();

                   } else if ($("#tarea-input-desc").val().length > 35) {

                    alert("La descripcion es demasiado larga");
                    event.preventDefault();

                    }

            }else if(!validarHora($("#tarea-input-hour").val())) {
                alert("Introduzca una hora correcta por favor");
                event.preventDefault();

            }

        }else if(!validarFormatoFecha($("#tarea-input-hour").val())){

            alert("Introduzca correctamente la fecha de nacimiento por favor");
            event.preventDefault();

        }

    });

    $("#btn-signupReg").click(function () {

        if($("#email").val()==''){

            alert("Inserte el email por favor");
            event.preventDefault();

        }else if(!validarEmail($("#email").val())){

            alert("Inserte el email correctamente");
            event.preventDefault();

        }else if(validarEmail($("#email").val())){

            if($("#firstname").val()==''){

                alert("Introduzca su nombre");
                event.preventDefault();

            }else if($("#lastname").val()==''){

                alert("Introduzca sus apellidos");
                event.preventDefault();

            }else if($("#user").val()==''){

                alert("Introduzca su nombre de usuario");
                event.preventDefault();

            }else if($("#password").val()==''){

                alert("Introduzca su contraseña");
                event.preventDefault();

            }

        }

    });

    $("#btn-loginPass").click(function () {

        if($("#id_email").val()==''){

            alert("Introduzca su email por favor");
            event.preventDefault();


        }else if($("#user").val()==''){

            alert("Introduzca su nombre de usuario");
            event.preventDefault();
        }




    });


    $("#btn-signupMod").click(function(){
         alert("Nombre de usuario y password obligatorios");
            event.preventDefault();


       if(($("#user").val()=='')||($("#password").val()=='')){

           alert("Nombre de usuario y password obligatorios");
            event.preventDefault();


       }


    });


  });
    function validarFormatoFecha(campo) {
      var RegExPattern = /^\d{4}\-\d{1,2}\-\d{1,2}$/;
      if ((campo.match(RegExPattern)) && (campo!='')) {
            return true;
      } else {
            return false;
      }
}

 function validarHora(campo) {
      var RegExPattern = /^\d{2}\:\d{2}$/;
      if ((campo.match(RegExPattern)) && (campo!='')) {
            return true;
      } else {
            return false;
      }


}

    function validarEmail(campo) {
      var RegExPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
      if ((campo.match(RegExPattern)) && (campo!='')) {
            return true;
      } else {
            return false;
      }


}