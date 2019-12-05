import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
import d3Tip from 'd3-tip';
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

  margin = {top: 20, right: 31, bottom: 20, left: 120};

  constructor() { }
  
  ngOnChanges(): void {
    if (!this.data) { return; }

    this.createChart();
  }
  
  onResize() {
    this.createChart();
  }

  private createChart(): void {
    const element = this.chartContainer.nativeElement;
    const data = this.data;
    
    let realFormatter = (value) => {
      return formatCurrency(value, "pt-BR", "", "BRL", "1.0-0")
    }
    
    d3.select(element).select('svg').remove();

    const svg = d3.select(element).append('svg')
        .attr("viewBox", `0 0 740 290`)
        .attr("preserveAspectRatio", "xMinYMin meet");

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
        .tickFormat(function(d) { return realFormatter(d);}
        ).tickSizeOuter(0)
      )

    let yAxis = g => g
      .attr("transform", `translate(${this.margin.left}, 0)`)
      .call(d3.axisLeft(y).tickSizeOuter(0))

    const tip = d3Tip()

    tip
      .attr('class', 'd3-tip')
      .offset([-10, 0])
      .html(function(d) {
        return "<div><span>" + d.nome_municipio + "</span></div>" +
               "<div><span style='color:white'>" + "R$"+ realFormatter(d.valor_licitacoes) + "</span></div>";
      });

    svg.call(tip);

    svg.append("g")
      .attr("fill", "steelblue")
      .selectAll("rect")
      .data(data)
      .join("rect")
      .attr("class", "bar")
      .attr("x", x(0))
      .attr("y", d => y(d.nome_municipio))
      .attr("height", y.bandwidth())
      .on('mouseover', (d, i, n) => tip.show(d, n[i]))
      .on("mouseout", d => tip.hide(d));

    svg.append("g")
      .call(xAxis);

    svg.append("g")
      .call(yAxis);

    svg.selectAll("rect")
      .data(data)
      .transition()
      .duration(2000)
      .attr("x", d => x(0))
      .attr("width", d => x(d.valor_licitacoes) - x(0));    

  }

}