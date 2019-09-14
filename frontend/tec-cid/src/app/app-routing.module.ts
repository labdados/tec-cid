import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { PesquisaComponent } from './pages/pesquisa/pesquisa.component';
import { MunicipioComponent } from './pages/municipio/municipio.component';


const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'pesquisa', component:PesquisaComponent},
  {path: 'municipio/:codUnidadeGest', component:MunicipioComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
