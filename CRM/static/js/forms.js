document.addEventListener("DOMContentLoaded", function(event) { 
    document.getElementById("submit").addEventListener("click", function(e){
        e.preventDefault()
        var form1 = document.getElementById("form1")
        var form2 = document.getElementById("form2")
        var form3 = document.getElementById("form3")
        var xhr = new XMLHttpRequest();
        var xhr1 = new XMLHttpRequest();
        var xhr2 = new XMLHttpRequest();
        var for1 = new FormData(form1);
        var for2 = new FormData(form2);
        var for3 = new FormData(form3);
        xhr.open("POST", "/add_company/");
        xhr.onreadystatechange=function(){

        };
        xhr.send(for1);
        xhr1.open("POST", "/add_departement/");
        xhr1.onreadystatechange=function(){

        }
        xhr1.send(for2);
        xhr2.open("POST", "/add_contact/");
        xhr2.onreadystatechange=function(){
            
        }
        xhr2.send(for3);
        
    });
  });


