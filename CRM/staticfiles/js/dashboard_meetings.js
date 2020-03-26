document.addEventListener('DOMContentLoaded', function () {
    fetch('/meeting_display/').then(function (response) {
        response.text().then(function (text) {
            var element = document.getElementById("meeting")
            var data = JSON.parse(text);
            console.log
            var elementToAdd = `<span> ${data.meeting[0].date} at ${data.meeting[0].time} with ${data.meeting[0].name}
                                in ${data.meeting[0].place}`
            element.insertAdjacentHTML("beforeend", elementToAdd);


        });
    });
});