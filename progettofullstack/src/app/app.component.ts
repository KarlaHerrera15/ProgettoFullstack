import { Component } from '@angular/core';
import { RouterOutlet, RouterModule} from '@angular/router';
import { FirsttenComponent } from './firstten/firstten.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule, FirsttenComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'progettofullstack';
}
