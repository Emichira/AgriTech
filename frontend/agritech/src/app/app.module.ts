import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { CarouselModule } from 'ngx-owl-carousel-o';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './features/header/header.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { FooterComponent } from './features/footer/footer.component';
import { ProductsPageComponent } from './pages/products-page/products-page.component';
import { ProductDetailComponent } from './pages/product-detail/product-detail.component';
import { ShoppingCartComponent } from './pages/shopping-cart/shopping-cart.component';
import { CheckoutComponent } from './pages/checkout/checkout.component';
import { ShippingDetailsComponent } from './pages/checkout/shipping-details/shipping-details.component';
import { PaymentComponent } from './pages/checkout/payment/payment.component';
import { BlogComponent } from './pages/blog/blog.component';
import { BlogsPageComponent } from './pages/blog/blogs-page/blogs-page.component';
import { BlogDetailsComponent } from './pages/blog/blog-details/blog-details.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomePageComponent,
    FooterComponent,
    ProductsPageComponent,
    ProductDetailComponent,
    ShoppingCartComponent,
    CheckoutComponent,
    ShippingDetailsComponent,
    PaymentComponent,
    BlogComponent,
    BlogsPageComponent,
    BlogDetailsComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    CarouselModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
