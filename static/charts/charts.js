var module = angular.module('myApp',[]);

function Main($scope,$http, $compile){
// $http.get("/chart/").

$scope.FILTInit = function(){
  $http({
    method:"GET",
    url:"/chart1/",
    params:{
          req_date:1}
       }).then( function(response, status) {
$scope.data = response.data;
var name = $scope.data.y1
var options = {
          series: [{
          name: 'Total Donations',
          data: $scope.data.y1
        }],
        chart: {
          height: 350,
          type: 'bar',
          toolbar: {
      show: true,
      tools: {
          download: true,
          selection: false,
          zoom: true,
          zoomin: false,
          zoomout: false,
          pan: false,
          reset: true},}
        },
        plotOptions: {
          bar: {
            endingShape: 'rounded',
            columnWidth: '70%',
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 2
        },
        
        grid: {
          row: {
            colors: ['#fff', '#f2f2f2']
          }
        },
        xaxis: {
          labels: {
            rotate: -45
          },
          categories: $scope.data.x1,
          tickPlacement: 'on'
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'light',
            type: "horizontal",
            shadeIntensity: 0.25,
            gradientToColors: undefined,
            inverseColors: true,
            opacityFrom: 0.85,
            opacityTo: 0.85,
            stops: [50, 0, 100]
          },
        },
        tooltip: {
          y: {
            formatter: function(value) {
              return  '₹ '+value}}}
        }; 

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
chart.update();})}

// Work Order Chart Update
$scope.FILT = function(){
  $http({
    method:"GET",
    url:"/chart1/",
    params:{
          req_date:$scope.req_date}
       }).then( function(response, status) {
$scope.data = response.data;
var name = $scope.data.y1
var options = {
          series: [{
          name: 'Total Donations',
          data: $scope.data.y1
        }],
        chart: {
          height: 350,
          type: 'bar',
          toolbar: {
      show: true,
      tools: {
          download: true,
          selection: false,
          zoom: true,
          zoomin: false,
          zoomout: false,
          pan: false,
          reset: true},}
        },
        plotOptions: {
          bar: {
            endingShape: 'rounded',
            columnWidth: '70%',
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 2
        },
        
        grid: {
          row: {
            colors: ['#fff', '#f2f2f2']
          }
        },
        xaxis: {
          labels: {
            rotate: -45
          },
          categories: $scope.data.x1,
          tickPlacement: 'on'
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'light',
            type: "horizontal",
            shadeIntensity: 0.25,
            gradientToColors: undefined,
            inverseColors: true,
            opacityFrom: 0.85,
            opacityTo: 0.85,
            stops: [50, 0, 100]
          },
        },
        tooltip: {
          y: {
            formatter: function(value) {
              return  '₹ '+value}}}
        }; 

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
chart.update();})}

// $scope.FILTInit1 = function(){
//   $http({
//     method:"GET",
//     url:"/spin/",
//     params:{
//           req_date:1}
//        }).then( function(response, status) {
// $scope.data = response.data;

// var pj = $scope.data.spa
// document.getElementById("myText").innerHTML = pj;






// })}

}module.controller("MainCtrl",Main); 
