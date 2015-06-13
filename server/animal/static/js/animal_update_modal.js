$('#modalEdit').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Boton que desencadena el modal
  var recipient = button.data('nombre'); // Extraer información de los atributos Data
  var modal = $(this);
});

$('#modalDelete').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Boton que desencadena el modal
  var recipient = button.data('nombre');// Extraer información de los atributos Data
  var modal = $(this);
  modal.find('.modal-title').text('Eliminar a ' + recipient);
  modal.find('.modal-body input').val(recipient);
});