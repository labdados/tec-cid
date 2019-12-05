import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BarchartEmpresasComponent } from './barchart-empresas.component';

describe('BarchartEmpresasComponent', () => {
  let component: BarchartEmpresasComponent;
  let fixture: ComponentFixture<BarchartEmpresasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarchartEmpresasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BarchartEmpresasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
