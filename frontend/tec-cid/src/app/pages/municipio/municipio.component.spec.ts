import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MunicipioComponent } from './municipio.component';

describe('MunicipioComponent', () => {
  let component: MunicipioComponent;
  let fixture: ComponentFixture<MunicipioComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MunicipioComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MunicipioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
