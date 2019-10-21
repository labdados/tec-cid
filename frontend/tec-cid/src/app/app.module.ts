import { BrowserModule } from '@angular/platform-browser';
import { NgModule, LOCALE_ID } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import {APP_BASE_HREF} from '@angular/common';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { PesquisaComponent } from './pages/pesquisa/pesquisa.component';
import { FiltrosComponent } from './components/filtros/filtros.component';
import { MunicipioComponent } from './pages/municipio/municipio.component'

import { SelectDropDownModule } from 'ngx-select-dropdown';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { LicitacaoComponent } from './pages/licitacao/licitacao.component';
import { NgbTooltipModule, NgbToastModule } from '@ng-bootstrap/ng-bootstrap';
import { FilterPropostaPipe } from './pipes/filter-proposta.pipe';
import { FilterPropostaPerdedoraPipe } from './pipes/filter-proposta-perdedora.pipe';

registerLocaleData(localePt);


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    PesquisaComponent,
    FiltrosComponent,
    MunicipioComponent,
    LicitacaoComponent,
    FilterPropostaPipe,
    FilterPropostaPerdedoraPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    SelectDropDownModule,
    FormsModule,
    ReactiveFormsModule,
    Ng2SearchPipeModule,
    NgbTooltipModule,
    NgbToastModule
  ],
  providers: [
    { provide: LOCALE_ID, useValue: 'pt-BR'}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
