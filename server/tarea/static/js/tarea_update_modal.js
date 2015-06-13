$('#modalEditTarea').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Boton que desencadena el modal
  var modal = $(this);
  var dir="/tarea/borrar/"+button.data('idtarea');
  modal.find('#tarea-input-name').val(button.data('nombre'));
  modal.find('#tarea-select-mascota').val(button.data('animal'));
  modal.find('#tarea-input-date').val(button.data('date'));
  modal.find('#tarea-input-hour').val(button.data('hour'));
  modal.find('#tarea-input-desc').val(button.data('desc'));
  modal.find('#tarea-input-hidden-id').val(button.data('idtarea'));
  $('#redir').attr("href",dir);
});

$('#modalDeleteTarea').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget); // Boton que desencadena el modal
  var recipient = button.data('nombre');// Extraer información de los atributos Data
  var modal = $(this);
  modal.find('.modal-title').text('Eliminar a ' + recipient);
  modal.find('.modal-body input').val(recipient);
});