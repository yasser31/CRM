document.addEventListener('DOMContentLoaded', function () {
    fetch('/contact_percent/').then(function (response) {
        response.text().then(function (text) {
        var data = JSON.parse(text);
        var element = document.getElementById("contact_dashboard");
        var elementToAdd = `<div class="col-lg-3 col-6">
        <!-- small card -->
        <div class="small-box bg-info">
            <div class="inner">
                <h3 class="text-white">${data.total_contacts}</h3>
                <p>Tolal Contacts</p>
            </div>
            <div class="icon">
            <i class="ion ion-stats-bars"></i>
            </div>
            <a href="#" class="small-box-footer text-white">
                More info <i class="fas fa-arrow-circle-right"></i>
            </a>
        </div>
    </div>
    <!-- ./col -->
    <div class="col-lg-3 col-6">
        <!-- small card -->
        <div class="small-box bg-success">
            <div class="inner">
            <h3 class="text-white">${data.total_clients}<sup style="font-size: 20px"></sup></h3>
            <p>Total Clients</p>
            </div>
            <div class="icon">
                <i class="ion ion-stats-bars"></i>
            </div>
            <a href="#" class="small-box-footer text-white">
                More info <i class="fas fa-arrow-circle-right"></i>
            </a>
        </div>
    </div>
    <!-- ./col -->
    <div class="col-lg-3 col-6">
        <!-- small card -->
        <div class="small-box bg-warning">
            <div class="inner">
                <h3 class="text-white">${data.total_prospects}</h3>
                <p>Total Prospects</p>
            </div>
            <div class="icon">
            <i class="ion ion-stats-bars"></i>
            </div>
            <a href="#" class="small-box-footer text-white">
                More info <i class="fas fa-arrow-circle-right"></i>
            </a>
        </div>
    </div>
</div>`
        element.insertAdjacentHTML("beforeend", elementToAdd);
        });
    });
});
