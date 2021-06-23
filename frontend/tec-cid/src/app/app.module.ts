import { BrowserModule } from '@angular/platform-browser';
import { NgModule, LOCALE_ID } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import {APP_BASE_HREF} from '@angular/common';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { PesquisaComponent } from './pages/pesquisa/pesquisa.component';
import { FiltrosComponent } from './components/filtros/filtros.component';
import { BarChartComponent } from './components/bar-chart/bar-chart.component';
import { FilterPropostaPipe } from './pipes/filter-proposta.pipe';
import { FilterPropostaPerdedoraPipe } from './pipes/filter-proposta-perdedora.pipe';
import { TabelaComponent } from './components/tabela/tabela.component';
import {MatMenuModule} from '@angular/material/menu';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
//import {MatMomentDateModule} from '@angular/material/core'

import { SelectDropDownModule } from 'ngx-select-dropdown';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { LicitacaoComponent } from './pages/licitacao/licitacao.component';
import { NgbTooltipModule, NgbToastModule } from '@ng-bootstrap/ng-bootstrap';
import {MatTableModule, MatFormFieldModule, MatPaginatorModule, MatSortModule, MatPaginatorIntl, MatInputModule, MatTooltipModule, MatProgressSpinnerModule, MatIconModule, MatButtonModule, MatCardModule, MatAutocompleteModule} from '@angular/material';
import { getPortuguesePaginatorIntl } from './components/tabela/ptbr-pagination';
import { BarchartEmpresasComponent } from './components/barchart-empresas/barchart-empresas.component';
import { FormdateComponent } from './components/formdate/formdate.component';





registerLocaleData(localePt);


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    PesquisaComponent,
    FiltrosComponent,
    BarChartComponent,
    LicitacaoComponent,
    FilterPropostaPipe,
    FilterPropostaPerdedoraPipe,
    TabelaComponent,
    BarchartEmpresasComponent,
    FormdateComponent,
  ],
  imports: [
    MatMenuModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    SelectDropDownModule,
    FormsModule,
    ReactiveFormsModule,
    Ng2SearchPipeModule,
    NgbTooltipModule,
    NgbToastModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatFormFieldModule,
    MatPaginatorModule,
    MatSortModule,
    MatInputModule,
    MatTooltipModule,
    MatProgressSpinnerModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatAutocompleteModule,
    MatDatepickerModule,
    MatNativeDateModule
  ],
  providers: [
    { provide: LOCALE_ID, useValue: 'pt-BR'},
    { provide: MatPaginatorIntl, useValue: getPortuguesePaginatorIntl()},
    FormdateComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
