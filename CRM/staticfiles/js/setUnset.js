document.addEventListener("DOMContentLoaded", function (event) {
    var set = document.getElementById("set");
    var unset = document.getElementById("unset");
    var elements = document.getElementsByClassName("set");
    var setFunction = function (e) {
        e.preventDefault()
        var xhr;
        c_id = this.getAttribute("cp_id")
        console.log(c_id);
        xhr = new XMLHttpRequest();
        xhr.open('GET', `/set/${c_id}`, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                location.reload()
            }
        };
        xhr.send()

    }
    for (element of elements) {
        element.addEventListener("click", setFunction);
    }

});
