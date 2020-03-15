document.addEventListener('DOMContentLoaded', function () {
    fetch('/meeting_display/').then(function (response) {
        response.text().then(function (text) {
            var element = document.getElementById("fieldset")
            var data = JSON.parse(text);
            for (met of data.meeting){
                console.log(met)
                var elementToAdd =  `<label class="tasks-list-item">
                <input type="checkbox" class="tasks-list-cb">
                <span class="tasks-list-mark"></span>
                <span class="tasks-list-desc"> ${met.date} <br> at ${met.time}<br> with ${met.name} in ${met.place}</span>
                </label>`
                element.insertAdjacentHTML("beforeend", elementToAdd);
            }
            
        });
    });
});