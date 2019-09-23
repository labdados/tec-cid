import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { PesquisaComponent } from './pages/pesquisa/pesquisa.component';
import { FiltrosComponent } from './components/filtros/filtros.component';
import { HttpClientModule } from '@angular/common/http';

import { SelectDropDownModule } from 'ngx-select-dropdown';
import { MunicipioComponent } from './pages/municipio/municipio.component'

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    PesquisaComponent,
    FiltrosComponent,
    MunicipioComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    SelectDropDownModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
