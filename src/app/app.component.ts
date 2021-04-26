import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart } from 'chart.js';
import { formdata } from './model/data.model';

@Component({
  selector: 'app-graph',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.scss' ]
})
export class AppComponent implements OnInit {
  countryList: string[] = [];
  gasList = ['CO2', 'GHG(Indirect CO2)', 'GHG', 'HFC', 'CH4', 'NF3', 'N2O', 'PFC', 'SF6', 'HFC+PFC'];
  formdata: formdata = {country : 'Australia' , gas: 'CO2'};
  @ViewChild('canvas' , {static: false}) canvas: ElementRef;
  chart = [];
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get('assets/country.csv', {responseType: 'text'})
    .subscribe(
        data => {
            const csvToRowArray = data.split('\n');
            for (const country of csvToRowArray) {
              this.countryList.push(country.trim());
            }
        }
    );
  }

  onSubmit() {
    this.http.get('assets/output.csv', {responseType: 'text'})
    .subscribe(
        data => {
            const gasValue = [];
            const yearLabel = [];
            const gasIndex = this.gasList.indexOf(this.formdata.gas) + 2;
            const csvToRowArray = data.split('\n').filter( (value) => value.includes(this.formdata.country));
            for (let index = 0; index < csvToRowArray.length - 1; index++) {
              const row = csvToRowArray[index].split(',');
              gasValue.push(row[gasIndex].trim());
              yearLabel.push(row[1]);
            }
            if (!gasValue.includes('null')){
              this.chart = new Chart(this.canvas.nativeElement.getContext('2d'), {
                type: 'line',
                data: {
                  labels: yearLabel,
                  datasets: [
                    {
                      data: gasValue,
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
              alert('Data not present for this gas , please select another gas');
            }
        }
    );
  }

}

