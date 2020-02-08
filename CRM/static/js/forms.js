document.addEventListener("DOMContentLoaded", function(event) { 
    document.getElementById("submit").addEventListener("click", function(e){
        e.preventDefault()
        document.getElementById("form1").submit();
        document.getElementById("form2").submit();
        document.getElementById("form3").submit();
    });
  });


