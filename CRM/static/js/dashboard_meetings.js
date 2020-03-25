document.addEventListener('DOMContentLoaded', function () {
    fetch('/meeting_display/').then(function (response) {
        response.text().then(function (text) {
            var element = document.getElementById("meeting")
            var data = JSON.parse(text);
            for (met of data.meeting){
                console.log(met)
                var elementToAdd =  `<span> ${met.date} at ${met.time} with ${met.name}
                                    in ${met.place}`
                element.insertAdjacentHTML("beforeend", elementToAdd);
            }
            
        });
    });
});