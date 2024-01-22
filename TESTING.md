# **Footwear Fusion - Testing**  

[Back to the main README.md file](FootwearFusion-README.md)

[Back to the Testing section in main README.md file](FootwearFusion-README.md#testing)

[View the live website here](https://footwear-fusion-9bb895189ceb.herokuapp.com/)  

## **Table of Contents**  
1. [User Stories Testing](#1-user-stories-testing)  
   - [Unregistered Users' Goals](#unregistered-users-goals)  
   - [Registered Users' Goals](#registered-users-goals) 
   - [Administrative Account Holder's Goals](#administrative-account-holder-s-goals) 
2. [Autoprefixer CSS](#autoprefixer-css)
3. [Manual Testing](#3-manual-testing)
   - [Browsers Compatibility](#browsers-compatibility) 
   - [Devices](#devices)
   - [Responsiveness](#responsiveness)
   - [Links](#links)
   - [Forms](#forms)
   - [Defensive Testing](#defensive-testing)
4. [W3C Validator Testing](#4-w3c-validator-testing) 
   - [HTML](#html)
   - [CSS](#css)
5. [JSHint Testing](#5-jshint-testing)
6. [Pep8 Online Testing](#6-pep8-online-testing)  
7. [Lighthouse Testing](#7-lighthouse-testing)  

The website was extensively tested during the development by using:
- console.log() and developer tools for front-end  
- printing variables to the terminal for back-end  
- manual testing and developing based on the user stories  

### **1. User Stories Testing**  

**A. As a shopper I want to be able to:**

1. *Rapidly discern the type of products or services offered by the site.*

   The company logo is prominently displayed at the top-center of the homepage, effectively highlighting our brand. The company name is clear and descriptive, immediately conveying the nature of our products. Additionally, the hero image prominently features shoes, clearly indicating our primary product line. As users scroll down the homepage, they will encounter intuitive navigation facilitated by large, visually appealing images of our products.
   ![Landing Page](readme-testing-files/testing/user-stories/home-1.png "Landing Page")  

2. *Instantly notice any special deals or promotions.*

   As users navigate down the homepage, they will encounter the Final Sale section. Clicking on the 'Shop Now' button will redirect them to a product page where all items on sale are conveniently pre-filtered for easy browsing.
   ![Sale Banner](readme-testing-files/testing/user-stories/sale.png "Sale Banner")   

3. *Effortlessly search for specific products.*

   Upon visiting the website, users have immediate access to the search function. On desktop, this feature is conveniently positioned at the top left of the screen, while on mobile devices, it is located on the right side.
   ![Search for Product](readme-testing-files/testing/user-stories/navbar-search.png "Search for Product")  

4. *Observe a preview of the most popular products.* 

   On the homepage, visitors can also explore a selection of the website's eight best-selling products. These popular items are showcased in a multi-item carousel format, allowing users to easily browse through them by clicking on the arrows to navigate left or right.
   ![Best Sellers Products](readme-testing-files/testing/user-stories/best-sellers.png "Best Sellers Products")  

5. *Browse through all products and smoothly transition between different categories.*

This website is organized into three primary categories: Women, Men, and Kids. When users select a category, it reveals a list of subcategories within it, such as Boots, Sneakers, Flats, and more. On desktop, a convenient side navigation menu enhances the user experience, enabling seamless transitions between categories and subcategories. On mobile devices, the side navigation transforms into a dropdown menu for user-friendly navigation. Additionally, a Breadcrumb Navigation feature is provided, allowing users to easily navigate back to broader categories for added convenience.

![Navigation - desktop](readme-testing-files/testing/user-stories/navigation.png "Navigation - desktop")   
![Navigation - mobile](readme-testing-files/testing/user-stories/navigation-mobile.png "Navigation - mobile")  

6. *Organize products by price, rating, or popularity.*

The sorting feature is located in the top-left corner of the products page.

![Sort functionality](readme-testing-files/testing/user-stories/sort.png "Sort functionality")  

7. *Explore detailed information on individual product pages.*

By clicking on the product image, users will be redirected to the Individual Product page, where they can access comprehensive details related to the product.

![Product's information](readme-testing-files/testing/user-stories/product-info.png "Product's information")   

8. *Access reviews for products.*

Users can scroll down on the Individual Product page to discover the product's reviews situated beneath its information.

![Product's reviews](readme-testing-files/testing/user-stories/reviews.png "Product's reviews") 

9. *Conveniently choose product size and quantity, and add them to the shopping bag.*

Customers have the convenience of effortlessly choosing their desired size and quantity, followed by a simple click on the "Add To Bag" button to make a purchase.

![Select Size and Quantity](readme-testing-files/testing/user-stories/select-size.png "Select Size and Quantity")  

10. *View the contents of the shopping bag.*

When users add a product to their shopping bag, a notification toast will appear in the top-right corner to provide information about the shopping bag's status.

![Shopping Bag Toast](readme-testing-files/readme/toast-success.png "Shopping Bag Toast")  

Users have the option to access the Shopping Bag page through two methods: either by selecting the "Shopping Bag" option in the Navigation Bar or by clicking the "Go To The Shopping Bag" button located within the toast notification.

![Shopping Bag Page](readme-testing-files/testing/user-stories/bag.png "Shopping Bag Page") 

11. *Modify the shopping bag by changing product quantities or removing items.*

Customers have the convenience of effortlessly modifying the product quantity by simply choosing the desired quantity. As a result, the Subtotal will automatically adjust to reflect this change. In the event that users wish to remove a product from their shopping bag, they can do so by clicking on the Trash icon.

![Adjust Bag](readme-testing-files/testing/user-stories/bag-adjust.png "Adjust Bag") 

12. *Seamlessly proceed to checkout and input payment details.*

13. *Be assured of the security of personal and payment information.*

Upon selecting the 'Secure Checkout' button located on the Shopping Bag page, users will be seamlessly redirected to the Checkout page. Within the payment section, the card payment details are conveniently organized into separate fields for card number, expiration date, CVC, and zip code entry.

![Checkout form](readme-testing-files/testing/user-stories/checkout-information.png "Checkout form")  

14. *Receive confirmation of orders post-purchase.*

Once users have completed the checkout form and clicked the 'Complete Order' button, they will be seamlessly redirected to a confirmation page displaying their order details. Simultaneously, they will receive an order confirmation email in their inbox.

![Order confirmation](readme-testing-files/testing/user-stories/order-confirmation.png "Order confirmation")  

15. *Get email notifications confirming purchases.*

As previously mentioned, users will receive an email confirmation in their inbox each time they successfully place an order.

![Email confirmation](readme-testing-files/testing/user-stories/email.png "Email confirmation")  

16. *Engage with informative articles or blogs about shoes and accessories.*

Users have the option to access the Articles page through two pathways: either by clicking the articles link in the footer or by navigating from the homepage. Once on the Articles page, they can select and view an article by simply clicking on their desired choice.

![All articles](readme-testing-files/testing/user-stories/articles.png "All articles")  

![Individual article](readme-testing-files/testing/user-stories/individual-article.png "Individual article")  


17. *Navigate the site with ease using the Navigation Bar and Footer.*

The website features a consistent Navigation Bar and Footer across all pages to enhance user navigation. The Navigation Bar is affixed to the top of the screen, ensuring it remains visible as users scroll down, providing convenient access to navigate the entire site.

For desktop users, the Navigation Bar and Footer are displayed as follows:

![Navbar on desktop](readme-testing-files/readme/navbar-desktop.png "Navbar on desktop")   

![Footer on desktop](readme-testing-files/readme/footer-desktop.png "Footer on desktop")   

On the other hand, for mobile users, the Navigation Bar and Footer are presented as follows:

![Navbar on mobile](readme-testing-files/testing/user-stories/navbar-mobile.png "Navbar on mobile") 

![Footer on mobile](readme-testing-files/testing/user-stories/footer-mobile.png "Footer on mobile")     


18. *Register for an account without hassle.*

To access registration or login options on the website, users can simply click the 'Sign In' link located on the left side of the Navbar when using a desktop computer. On mobile devices, they can achieve the same by tapping the user icon. These actions will lead users to either the Register/Sign Up page or the Log In page, depending on their choice.

![Register](readme-testing-files/testing/user-stories/register.png "Register")

![Log In](readme-testing-files/testing/user-stories/login.png "Log In")   


19. *Locate a FAQ section for inquiries.*

Users can locate the link to access the FAQ page within the website's footer.

![FAQ](readme-testing-files/testing/user-stories/faq.png "FAQ") 

20. *Contact the store through an accessible contact form.*

Users can also locate the link to access the contact page within the footer section.

![Contact form](readme-testing-files/testing/user-stories/contact-form.png "Contact form")   


[Back to top &uarr;](#table-of-contents)  
<br/>

**B. As a registered user/ shopper, I want to be able to:**