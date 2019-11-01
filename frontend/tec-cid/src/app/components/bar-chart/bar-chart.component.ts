import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
import { formatCurrency } from '@angular/common';

@Component({
  selector: 'app-bar-chart',
  encapsulation: ViewEncapsulation.None,
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss']
})
export class BarChartComponent implements OnChanges {
  @ViewChild('chart', {static: false}) 
  private chartContainer: ElementRef;
  
  rankingMunicipios: any;
  nomesMunicipios: string[];
  valoresLicitacoes: number[];

  @Input()
  data: any[];

  margin = {top: 20, right: 31, bottom: 20, left: 125};

  ngOnChanges(): void {
    this.createChart();
  }

  onResize() {
    this.createChart();
  }

  private createChart(): void {
    d3.select('svg').remove();

    const element = this.chartContainer.nativeElement;
    const data = this.data;

    let realFormatter = (value) => {
      return formatCurrency(value, "pt-BR", "", "BRL", "1.0-0")
    }

    let height = data.length * 25 + this.margin.top + this.margin.bottom

    const svg = d3.select(element).append('svg')
        .attr('width', element.offsetWidth)
        .attr('height', height);

    const contentWidth = element.offsetWidth - this.margin.left - this.margin.right;
    const contentHeight = element.offsetHeight - this.margin.top - this.margin.bottom;

    let x = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.valor_licitacoes)])
      .range([this.margin.left, this.margin.left + contentWidth])

    let y = d3.scaleBand()
      .domain(data.map(d => d.nome_municipio))
      .range([this.margin.top, this.margin.top + contentHeight])
      .padding(0.1)

    let xAxis = g => g
      .attr("transform", `translate(0, ${contentHeight + this.margin.top})`)
      .style("font", "12px sans-serif")
      .call(d3.axisBottom(x).ticks(contentWidth / 180)
        .tickFormat(function(d) { return realFormatter(d);})
      )

    let yAxis = g => g
      .attr("transform", `translate(${this.margin.left}, 0)`)
      .call(d3.axisLeft(y).tickSizeOuter(0))

    svg.append("g")
      .attr("fill", "steelblue")
      .selectAll("rect")
      .data(data)
      .join("rect")
      .attr("class", "bar")
      .attr("x", x(0))
      .attr("y", d => y(d.nome_municipio))
      .attr("width", d => x(d.valor_licitacoes) - x(0))
      .attr("height", y.bandwidth());

    svg.append("g")
      .call(xAxis);

    svg.append("g")
        //.style("font", "10px sans-serif")
        .call(yAxis);
  }
}
