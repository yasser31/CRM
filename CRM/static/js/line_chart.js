document.addEventListener('DOMContentLoaded', function () {
    fetch('/contact_month/').then(function (response) {
        response.text().then(function (text) {
            var data = JSON.parse(text);
            var myLineConfig =
            {
                "type": "line",
                "title": {
                    "text": "Contact And Client Evolution",
                    "font-size": "24px",
                    "adjust-layout": true
                },
                "plotarea": {
                    "margin": "dynamic"
                },
                "legend": {
                    "layout": "float",
                    "background-color": "none",
                    "border-width": 0,
                    "shadow": 0,
                    "align": "center",
                    "adjust-layout": true,
                    "toggle-action": "remove",
                    "item": {
                        "padding": 7,
                        "marginRight": 17,
                        "cursor": "hand"
                    }
                },
                "scale-x": {
                    "labels": ["January", "Februray", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November",
                        "December"],
                    "zooming": true,
                    "item": {
                        'font-size': 10
                    },
                    "shadow": 0,

                },
                'scroll-x': {

                },
                "scale-y": {
                    "line-color": "#f6f7f8",
                    "shadow": 0,
                    "guide": {
                        "line-style": "dashed"
                    },
                    "label": {
                        "text": "Page Views",
                    },
                    "minor-ticks": 0,
                    "thousands-separator": ","
                },
                "crosshair-x": {
                    "line-color": "#efefef",
                    "plot-label": {
                        "border-radius": "5px",
                        "border-width": "1px",
                        "border-color": "#f6f7f8",
                        "padding": "10px",
                        "font-weight": "bold"
                    },
                    "scale-label": {
                        "font-color": "#000",
                        "background-color": "#f6f7f8",
                        "border-radius": "5px"
                    }
                },
                "tooltip": {
                    "visible": false
                },
                "plot": {
                    "highlight": true,
                    "tooltip-text": "%t views: %v<br>%k",
                    "shadow": 0,
                    "line-width": "2px",
                    "marker": {
                        "type": "circle",
                        "size": 3
                    },
                    "highlight-state": {
                        "line-width": 3
                    },
                    "animation": {
                        "effect": 1,
                        "sequence": 2,
                        "speed": 100,
                    }
                },
                "series": [
                    {
                        "values": data.contact,
                        "text": "Contact",
                        "line-color": "#007790",
                        "legend-item": {
                            "background-color": "#007790",
                            "borderRadius": 5,
                            "font-color": "white"
                        },
                        "legend-marker": {
                            "visible": false
                        },
                        "marker": {
                            "background-color": "#007790",
                            "border-width": 1,
                            "shadow": 0,
                            "border-color": "#69dbf1"
                        },
                        "highlight-marker": {
                            "size": 6,
                            "background-color": "#007790",
                        }
                    },
                ]
            };

            zingchart.render({
                id: 'my_line_chart',
                data: myLineConfig,
                height: '100%',
                width: '100%'
            });
        });
    });
});

