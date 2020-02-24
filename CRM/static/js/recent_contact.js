document.addEventListener('DOMContentLoaded', function () {
    fetch('/recent_contact/').then(function (response) {
        response.text().then(function (text) {
            var element1 = document.getElementById("recent_contact");
            var element2 = document.getElementById("recent_client");
            var data = JSON.parse(text);
            for (cont of data.contact) {
                var elementToAdd1 = ` <div class="sidebar widget">
            <h6>Recent Contact</h6>
            <ul>
                <li>
                    <div class="sidebar-content">
                        <h5 class="animated bounceInRight"><a href="/details/${cont.id}">${cont.name}</a>
                        <span>${cont.country}</span>
                        <span>${cont.city} </span><br>
                        <span>${cont.date} </span>
             </h5>
                    </div><!-- .Sidebar-thumb -->
                    <div class="sidebar-meta">
                        <span class="time"> function :  ${cont.function}</span>
                        
                    </div><!-- .Sidebar-meta ends here -->
                </li><!-- .Li ends here -->
            </ul><!-- .Ul ends here -->
        </div><!-- .Widget ends here -->`
                element1.insertAdjacentHTML("beforeend", elementToAdd1);
            }
            for (clt of data.client) {
                var elementToAdd2 = ` <div class="sidebar widget">
            <h6>Recent Clients</h6>
            <ul>
                <li>
                    <div class="sidebar-content">
                        <h5 class="animated bounceInRight"><a href="/details/${clt.id}">${clt.name}</a>
                        <span> ${clt.country}</span>
                        <span>${clt.city} </span><br>
                        <span>${clt.date} </span>
                        </h5>
                    </div><!-- .Sidebar-thumb -->
                    <div class="sidebar-meta">
                        <span class="time"><i class="fa fa-clock-o"></i> function : ${clt.function}</span>
                    </div><!-- .Sidebar-meta ends here -->
                </li><!-- .Li ends here -->
            </ul><!-- .Ul ends here -->
        </div><!-- .Widget ends here -->`
                element2.insertAdjacentHTML("beforeend", elementToAdd2);
            }
        });
    });
});