document.addEventListener('DOMContentLoaded', function () {
	fetch('/contact_percent/').then(function (response) {
		response.text().then(function (text) {
			var data = JSON.parse(text)
			var myConfig = {
				type: "pie",
				plot: {
					borderColor: "#2B313B",
					borderWidth: 5,
					// slice: 90,
					valueBox: {
						placement: 'out',
						text: '%t\n%npv%',
						fontFamily: "Open Sans"
					},
					tooltip: {
						fontSize: '18',
						fontFamily: "Open Sans",
						padding: "5 10",
						text: "%npv%"
					},
					animation: {
						effect: 2,
						method: 5,
						speed: 900,
						sequence: 1,
						delay: 3000
					}
				},
				source: {
					text: 'gs.statcounter.com',
					fontColor: "#8e99a9",
					fontFamily: "Open Sans"
				},
				title: {
					fontColor: "#8e99a9",
					text: 'Contact Proportions',
					align: "left",
					offsetX: 10,
					fontFamily: "Open Sans",
					fontSize: 25
				},
				subtitle: {
					offsetX: 10,
					offsetY: 10,
					fontColor: "#8e99a9",
					fontFamily: "Open Sans",
					fontSize: "16",
					text: 'May 2016',
					align: "left"
				},
				plotarea: {
					margin: "20 0 0 0"
				},
				series: [
					{
						values: [data.clients_percent],
						text: "Client",
						backgroundColor: '#50ADF5',
					},
					{
						values: [data.prospects_percent],
						text: "Prospects",
						backgroundColor: '#FF7965',
						detached: true
					},
				]
			};

			zingchart.render({
				id: 'myChart',
				data: myConfig,
				height: '100%',
				width: '100%'
			});
		});

	});

});
