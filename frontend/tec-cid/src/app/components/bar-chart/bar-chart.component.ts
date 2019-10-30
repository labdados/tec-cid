import { Component, ElementRef, Input, OnChanges, ViewChild, ViewEncapsulation, HostListener } from '@angular/core';
import * as d3 from 'd3';
//import { DataModel } from 'src/app/models/data.model';
import { EstatisticasService } from 'src/app/services/estatisticas.service';

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

  margin = {top: 30, right: 0, bottom: 90, left: 192};

  constructor(
    private estatisticasService: EstatisticasService
  ) {}

  ngOnChanges(): void {
    this.createChart();
  }

  onResize() {
    this.createChart();
  }

  getRankingMunicipios() {
    this.rankingMunicipios = this.estatisticasService.getRankingMunicipios();
    // this.estatisticasService.getRankingMunicipios().subscribe(res => {
    //   this.rankingMunicipios = res.dados;
    //   console.log("1", this.rankingMunicipios);
    //   this.nomesMunicipios = res.dados.nome_municipio;
    //   this.valoresLicitacoes = res.dados.valor_licitacao;
    // })
  }

  private createChart(): void {
    d3.select('svg').remove();

    const element = this.chartContainer.nativeElement;
    //this.getRankingMunicipios();
    const data = this.data;

    const svg = d3.select(element).append('svg')
        .attr('width', element.offsetWidth)
        .attr('height', element.offsetHeight * (data.length / 3));

    const contentWidth = element.offsetWidth - this.margin.left - this.margin.right;
    const contentHeight = element.offsetHeight - this.margin.top - this.margin.bottom;

    let x = d3.scaleLinear()
      .domain([0, d3.max(data, d => Number(d.valor_licitacoes))])
      .range([this.margin.left, contentWidth + this.margin.right])

    let y = d3.scaleBand()
      .domain(data.map(d => d.nome_municipio))
      .range([this.margin.top, contentHeight + this.margin.bottom])
      .padding(0.1)

    let xAxis = g => g
      .attr("transform", `translate(0,${this.margin.top})`)
      .style("font", "14px sans-serif")
      .call(d3.axisTop(x).ticks(contentWidth / 180))
      .call(g => g.select(".domain").remove())

    let yAxis = g => g
      .attr("transform", `translate(${this.margin.left},0)`)
      .call(d3.axisLeft(y).tickSizeOuter(0))

    let format = x.tickFormat(20)

    svg.append("g")
      .attr("fill", "steelblue")
    .selectAll("rect")
    .data(data)
    .join("rect")
      .attr("x", x(0))
      .attr("y", d => y(d.nome_municipio))
      .attr("width", d => x(Number(d.valor_licitacoes)) - x(0))
      .attr("height", y.bandwidth());

    svg.append("g")
        .attr("fill", "#151C48")
        .style("font", "16px sans-serif")
      .selectAll("text")
      .data(data)
      .join("text")
        .attr("x", d => x(Number(d.valor_licitacoes)))
        .attr("y", d => y(d.nome_municipio) + y.bandwidth() / 2)
        .attr("dy", "0.25em")
        .attr("dx", "10px")
        .text(d => format(Number(d.valor_licitacoes)));

    //svg.append("g")
     //   .call(xAxis);

    svg.append("g")
        .style("font", "16px sans-serif")
        .call(yAxis);

  }
}
