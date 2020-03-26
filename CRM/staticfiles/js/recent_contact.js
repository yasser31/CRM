document.addEventListener('DOMContentLoaded', function () {
    fetch('/recent_contact/').then(function (response) {
        response.text().then(function (text) {
            var element1 = document.getElementById("rctbd");
            var data = JSON.parse(text);
            for (cont of data.contact) {
                var elementToAdd1 = `<tr class="rctr">
                                    <td class="rctd">${cont.id}</td>
                                    <td class="rctd">${cont.name}</td>
                                    <td class="rctd">${cont.country}</td>
                                    <td class="rctd">${cont.city}</td>
                                    <td class="rctd">${cont.function}</td>
                                    <td class="rctd">${cont.client}</td>
                                    </tr>`
                element1.insertAdjacentHTML("beforeend", elementToAdd1);
            }
        });
    });
});