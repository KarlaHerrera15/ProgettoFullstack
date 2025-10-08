import { Routes } from '@angular/router';
import { FirsttenComponent } from './firstten/firstten.component';
import { MoviepageComponent } from './moviepage/moviepage.component';

export const routes: Routes = [
  { path: 'firstten', component: FirsttenComponent},
  { path: 'moviepag', component: MoviepageComponent}
];