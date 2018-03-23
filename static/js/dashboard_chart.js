var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Indore", "Bhopal", "Lucknow", "Gandhi Nagar", "Ahemdabad", "Vadodra"],
        datasets: [{
            label: '# of Complaints',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    show: true,
                    color: "rgba(0,0,0,0)",
                    zeroLineColor: "rgba(39,170,225,1)"
                },
                scaleLabel: {
                    display: true,
                    fontFamily: "Helvetica",
                    fontColor: "#27AAE1"
                },
            }],
            yAxes: [{
                gridLines: {
                    show: true,
                    color: "rgba(0,0,0,0)",
                    zeroLineColor: "rgba(39,170,225,1)"
                },
                ticks: {
                    beginAtZero: true,
                    // max: 3,
                    // min: 0,
                    // stepSize: 0.9
                },
            }]
        }
    }
});


const CHART = document.getElementById("Chart");


var morningChart = new Chart(CHART, {

    type: 'pie',

    data: {

        labels: ["MON", "TUE", "WED", "THU", "FR", "SAT", "SUN",],

        datasets: [

            {

                label: "dataset",

                fill: true,

                /*  lineTension: 0.2, */

                backgroundColor: [

                    'rgba(255, 99, 132, 0.6)',

                    'rgba(54, 162, 235, 0.6)',

                    'rgba(255, 206, 86, 0.6)',

                    'rgba(75, 192, 192, 0.6)',

                    'rgba(153, 102, 255, 0.6)',

                    'rgba(255, 159, 64, 0.6)',

                    'rgba(255, 99, 132, 0.6)'

                ],

                borderColor: "rgba(39,170,225,100)",

                borderCapStyle: 'butt',

                borderDash: [],

                borderDashOffset: 0.0,

                borderJoinStyle: 'miter',

                pointBorderColor: "rgba(39,170,225,100)",

                pointBackgroundColor: "#fff",

                pointBorderWidth: 5,

                pointHoverRadius: 5,

                pointHoverBackgroundColor: "rgba(75,192,192,1)",

                pointHoverBorderColor: "rgba(220,220,220,1)",

                pointHoverBorderWidth: 2,

                pointRadius: 1,

                pointHitRadius: 10,

                data: [1, 2, 5, 3, 4, 2, 3],

                spanGaps: false,

            },

        ],


    },

    options: {
        legend: {
            position: 'top',
            //  display:false
        },
        scales: {
            ticks: {
                beginAtZero: true
            },


        },

    },

});


const lineCHART = document.getElementById("Line_chart");


var morning_Chart = new Chart(lineCHART, {
    type: 'line',
    data: {
        labels: ["MON", "TUE", "WED", "THU", "FR", "SAT", "SUN"],
        datasets: [
            {
                label: "Male",
                fill: true,
                backgroundColor: "rgba(255, 255, 255, 0.3)",
                borderColor: "white",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "white",
                pointBackgroundColor: "#00acc1",
                pointBorderWidth: 2,
                pointHoverRadius: 7,
                pointHoverBackgroundColor: "rgba(75,192,192,1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 5,
                pointHitRadius: 10,
                data: [5,8,2,1,5,2,3],
                spanGaps: false
            },
            {
                label: "Female",
                fill: true,
                /*  lineTension: 0.2, */
                backgroundColor: "rgba(255, 255, 255, 0.3)",
                borderColor: "white",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "black",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 3,
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "rgba(75,192,192,1)",
                pointHoverBorderColor: "rgba(220,220,220,1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [1.7, 2.8, 5.5, 3.9, 4.5, 2.5, 3.5],
                spanGaps: false
            }
        ]
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    show: false,
                    color: "rgba(0,0,0,0)",
                    zeroLineColor: "rgba(39,170,225,1)"
                },
                ticks: {
                    fontColor: 'white'
                },
                scaleLabel: {
                    display: true,
                    fontFamily: "Helvetica",
                    fontColor: "#27AAE1"
                }
            }],
            yAxes: [{
                gridLines: {
                    show: true,
                    color: "lightcyan",
                    zeroLineColor: "rgba(39,170,225,1)"
                },
                ticks: {
                    beginAtZero: true,
                    fontColor: 'white'
                }
            }]
        }
    }
});
