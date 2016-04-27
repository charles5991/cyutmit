$(document).on('change', '#selectFile', function() {
  var formData = new FormData();
  formData.append('fileToUpload', $('#selectFile')[0].files[0]);
  formData.append('folderName', '{{folderName}}');
  formData.append('csrfmiddlewaretoken', '{{csrf_token}}');

  $.ajax({
    url: '{% url 'main:upload' %}',  
    type: 'POST',
    success: function(data){
      var id = "[id^='mceu_'][id$='-inp']";
        $(id).attr({'value':data, 'disabled':true});
    },
    error: function(){
      alert('上傳失敗');
    },
    data: formData,
    cache: false,
    contentType: false,
    processData: false
  });
});