import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart } from 'chart.js';

@Component({
  selector: 'app-graph',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.scss' ]
})
export class AppComponent implements OnInit {
  countryList: string[] = ['a' , 'b'];
  private gasData;
  private gasList;
  private formdata: any = {};
  @ViewChild('canvas' , {static: false}) canvas: ElementRef;
  chart = [];
  constructor(private http: HttpClient) {}

  ngOnInit() {
    const headers = { country: 'Australia' , 'Access-Control-Allow-Origin': '*' , responseType: 'json'};
    this.http.get('http://127.0.0.1:5000/countries').subscribe(data => {
      this.countryList = data['countryList'];
      this.http.post('http://127.0.0.1:5000/gasData' , {'country' : this.countryList[0]} , {headers} )
      .subscribe(
        data => {
           this.gasData = data;
           this.gasList = Object.keys(data);
       });
    });
  }

  onSubmit() {
    const headers = { country: 'Australia' , 'Access-Control-Allow-Origin': '*' , responseType: 'json'};
    this.http.post('http://127.0.0.1:5000/gasData' , {'country': this.formdata.country} , {headers} )
    .subscribe(
        data => {
           this.gasData = data;
           this.gasList = Object.keys(data);
           if (this.gasData.hasOwnProperty(this.formdata.gas)) {
              const graphData = this.processData(this.formdata.gas);
              this.chart = new Chart(this.canvas.nativeElement.getContext('2d'), {
                  type: 'line',
                  data: {
                    labels: graphData.keys,
                    datasets: [
                      {
                        data: graphData.value,
                        borderColor: '#3cba9f',
                        fill: false
                      }
                    ]
                  },
                  options: {
                    legend: {
                      display: false
                    },
                    scales: {
                      xAxes: [{
                        display: true
                      }],
                      yAxes: [{
                        display: true
                      }],
                    }
                  }
                });
            } else {
              alert('gas values are not in database');
            }
    });
  }

  private processData(gas) {
    const obj  = this.gasData[gas];
    const keys = Object.keys(obj);
    const value = [];
    for (const key of keys) {
      value.push(this.gasData[gas][key]);
    }
    return {value , keys};
  }

}

