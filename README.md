# **Footwear Fusion**
![Footwear Fusion website in variouse devices](readme-testing-files/readme/main-image.png "Footwear Fusion website in variouse devices")

[View live website here]()
</br>  

**Table of Contents**   

## **Introduction**
Introducing Footwear Fusion, your go-to e-commerce destination for trendy shoes and stylish accessories! Our platform offers a wide selection of footwear, complemented by an array of fashion-forward accessories like bags and wallets. Designed with user security in mind, Footwear Fusion incorporates robust authentication and Stripe payment integration, ensuring a secure and seamless shopping experience.

This innovative website marks the culmination of the Code Institute's Milestone Project 4, a pivotal component of their Diploma in Full Stack Software Development program. Footwear Fusion is a testament to the power of full-stack development, skillfully blending HTML, CSS, JavaScript, Django+Python, and relational databases. The project also leverages Stripe for secure transactions and utilizes various additional libraries to enhance functionality and user experience.

<br/>  

## **UX Development Plane**   
### **1. Strategy Plane**  
#### **Project Goals**   
The foremost objective of this project is to establish an e-commerce platform that excels in functionality, boasts an aesthetically pleasing design, and offers an intuitive user experience, even for first-time visitors. The site will provide essential e-commerce capabilities, including user registration and login, item selection, and secure payment processing. Beyond these fundamental features, the website aims to enhance user engagement and interaction. This will be achieved through additional functionalities, such as the ability to add products to a wishlist, submit product reviews, and access informative articles. The overarching goal is to ensure a seamless, enjoyable, and enriching shopping experience for all users.

#### **User Goals**  
Users seek a platform that offers:
- A user-friendly and intuitive online store/website, ensuring effortless navigation and a seamless purchasing experience.
- A digital storefront that not only facilitates shopping but also offers additional interactive activities to enhance user engagement.

The intended audience for this website includes:

Individuals aged 18 to 40, primarily young adults.
Trendy and style-conscious individuals.
Those who appreciate the ease of technology and are active on social media platforms.

#### **Site Owner Goals**  
The primary objectives of the site owner include:
- Generating revenue through the sale of products (and services) to customers.
- Efficiently administering the range of products offered on the website.

#### **User Stories** 
- As a shopper I want to be able to:
  1. Rapidly discern the type of products or services offered by the site.
  2. Instantly notice any special deals or promotions.
  3. Effortlessly search for specific products.
  4. Observe a preview of the most popular products.
  5. Browse through all products and smoothly transition between different categories.
  6. Organize products by price, rating, or color.
  7. Explore detailed information on individual product pages.
  8. Access reviews for products.
  9. Conveniently choose product size and quantity, and add them to the shopping bag.
  10. View the contents of the shopping bag.
  11. Modify the shopping bag by changing product quantities or removing items.
  12. Seamlessly proceed to checkout and input payment details.
  13. Be assured of the security of personal and payment information.
  14. Receive confirmation of orders post-purchase.
  15. Get email notifications confirming purchases.
  16. Engage with informative articles or blogs about shoes and accessories.
  17. Navigate the site with ease using the Navigation Bar and Footer.
  18. Register for an account without hassle.
  19. Locate a FAQ section for inquiries.
  20. Contact the store through an accessible contact form.

- As a registered user/ shopper, I want to be able to:
  1. Access all functionalities available to non-registered shoppers.
  2. Log in and log out with ease.
  3. Promptly recover forgotten passwords.
  4. Get email confirmations upon registration.
  5. Manage a personal user profile to view order history and update personal details.
  6. Submit reviews for previously purchased products.
  7. Modify or delete personal reviews.
  8. Place products in a wishlist for convenient access to items I'm interested in buying.
  9. Remove products from the wishlist, so I can remove products I don't wish to purchase.
  10. Transfer products from the wishlist to the shopping bag effortlessly.

- As an admin and store management, I want to be able to:
  1. Add new products to the inventory.
  2. Modify or update product details.
  3. Remove products from the listing.

<br/>  

### **2. Scope Plane**  
A comprehensive scope has been established for the site, taking into account all objectives and user narratives, while also allowing for potential future enhancements.

#### **Functional Requirements**  
Unregistered users can:
- Register by providing a username, email, and password.
- Browse all products and organize them by price, rating, and color.
- Conduct product searches.
- Access detailed product information.
- Place products into a shopping bag.
- Modify and remove items in the shopping bag.
- Complete purchases and process payments.
- Receive email confirmations for transactions.

Registered users have the capabilities of unregistered users, plus they can:
- Log in with a username and password.
- Access and edit their profile page.
- Update their delivery/contact details on the profile page.
- Review their order history on the profile page.
- Post, edit, and delete reviews for purchased products.
- Add and remove products from their wishlist.
 
Admin/site owners possess all registered user functionalities, as well as the ability to:
- Add new products to the site.
- Edit or update product details.
- Remove products from the site.

#### **Non-functional Requirements**  
Users will have the opportunity to:
- Explore articles and blogs about shoes, accessories, and fashion trends.
- Access a FAQ page for answers to common questions.
- Communicate with the store through a contact form.
- Navigate the site with ease and intuition.

<br/>  

### **3. Structure Plane**  
The website features a Hierarchical Tree Structure, meticulously organized to facilitate easy and intuitive navigation for users. Illustrated below is the website's workflow, thoughtfully crafted using [Creately](https://creately.com/).  

![The website's structure](readme-testing-files/readme/structure.png "The website's structure")   
The design distinctly differentiates the access levels between unregistered and registered users. While unregistered users have the capability to purchase products and receive confirmation emails, they lack certain privileges exclusive to registered users, including:

- Accessing their order history
- Posting, editing, and deleting product reviews
- Creating a personalized list of favorite products.

All the aforementioned functionalities are accessible only to users with a registered account.

<br/>  

### **4. Skeleton Plane**  
Using [Balsamiq](https://balsamiq.com/), wireframes were developed to outline the website's navigation and interface. These wireframes, specifically designed for desktop viewing, form the foundation upon which the interface will be adapted for various device sizes.

<br/>

#### **Color Scheme**  
The website's design language is articulated through a color palette that captures the essence of tranquility and natural beauty. Each hue is carefully chosen to create an ambiance that is both calming and welcoming, with a subtle infusion of warmth that conjures a sense of peace and serenity.
At the heart of the palette featured on [Coolors](https://coolors.co)is a soft blush pink (#F5CAC3), radiating a gentle and hospitable vibe. It's paired with an effervescent coral (#F28482), which injects the layout with a lively yet cozy warmth, resonating with a cheerful and dynamic spirit. Grounding these effusive tones, the muted teal (#84A59D) lends an earthy depth to the aesthetic, echoing the brand's connection to natural elements and understated elegance.

The selection of these colors transcends mere visual pleasure; it is a deliberate strategy to elicit a psychological sense of ease and contentment among visitors. This chromatic harmony is woven consistently throughout the website’s interface, from the tactile feedback of interactive elements to the enchanting allure of the hero image. Each detail is steeped in these colors, crafting a cohesive and engaging digital narrative that guides the user through an effortlessly integrated visual experience.
![The color scheme](readme-testing-files/readme/color-scheme.png "The color scheme")

#### **Typography**  
The typographic elements of the website are curated from the extensive collection available at [Google Fonts](https://fonts.google.com).   
- Primary Typeface: Noto Sans
  Serving as the primary typeface, Noto Sans is a sans-serif font favored for its contemporary and sleek aesthetic. It is employed across the board for paragraphs and button labels, offering a crisp and uncluttered look.
- Accent Typeface: DM Serif Display
  For a striking contrast, DM Serif Display is utilized for header texts on the Home page. As a serif font, it provides an elegant counterpoint to the sans-serif body text, adding a touch of sophistication and visual interest.

#### **Design Changes on The Final Product**  
The original wireframes were foundational in shaping the final design, however, adjustments were made to ensure optimal functionality and aesthetics:

- The logo underwent a transformation to a bolder version for enhanced visibility, addressing the issue that the initial, finer logo was not as prominent on smaller screens.
- Additional refinements included alterations in button colors and image selections, which were part of the creative evolution during the development process.

<br/>

## **Database Design**    

The database structure was conceptualized and outlined using [drawsql](https://drawsql.app/), starting with SQLite for the development phase and transitioning to Postgres for the production environment on Heroku. 
![The database schema](readme-testing-files/readme/database-schema.png " The database schema")  

- **Category Model**   
   - This model holds the category names for products, such as Women, Men, and Kids.
   - It includes a 'name' field for database identification and a 'friendly_name' field for the user interface display.

- **Subcategory Model**
   - This captures the subcategory names for products, which range from Sandals to New Arrivals.
   - The Category and Subcategory models are designed to be independent; no direct relationship is established to allow for greater flexibility.
   - Similar to the Category model, it has 'name' and 'friendly_name' fields for database and display purposes, respectively.  

- **Product Model**  
   - This model is a repository of comprehensive product details.
   - It is linked to the Category and Subcategory models through foreign keys.
   - Includes fields such as 'sku' for product identification, 'name', 'has_sizes' as a boolean to indicate if size variations exist, 'price', and 'rating'. 
   - The 'rating' initially reflects a retailer-provided quality assessment, which is updated as users review the product.
   - 'image' field for product visuals, and 'total_purchased' to track sales volume.

- **User M odel**  
   - Integral to the Django authentication system, this model stores user credentials, including username, email, and password.[django.contrib.auth](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/).

- **Order Model**
   - This model documents all the data related to successful orders.
   - It encompasses numerous fields from 'order_number' to 'stripe_pid', detailing everything from the buyer's information to payment details.

- **OrderLineItem Model**
   - Details of individual product orders are stored here.
   - It includes a 'product_size', 'quantity', and 'lineitem_total', which is the product of quantity and price.

- **UserProfile Model**
   - For registered users, this model holds shipping and contact information.
   - It is linked to the User model and contains fields like 'default_phone_number', 'default_country', etc.

- **Review Model**  
   - Captures user reviews for products they've purchased.
   - Includes a 'rating', 'review_text', and 'date' among other fields.

- **Blog Model**  
   - Used for storing blog articles for the website.
   - Contains fields for 'image', 'author', 'title', 'paragraph1', 'paragraph2', 'paragraph3', and 'created_on'.

- **Favorites Model**  
   - Keeps track of a user's favorite products.
   - To handle the many-to-many relationship with products, an intermediary model called 'FavoritesItem' is used, aligning with best practices from the Django documentation.([source from django documentation](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ManyToManyField.through_fields)).

- **Topic Model**
  - This model manages topics for the contact form.
  - It has a 'subject' field for database entries and a 'text' field for the display on the contact form.

- **ContactForm Model**
  - Stores submissions from the contact form.
  - Includes 'name', 'email', 'topic' (linked to the Topic model), 'order_number', 'message', and 'date' fields.

Each model is crafted to not only store essential data but also to create a seamless interaction between different segments of the site, ensuring data integrity and user experience are maintained at the highest standard.

<br/>  

## **Features**  
### **A. General Design Features**  
- **Responsive Design:** The website adapts seamlessly to all devices, ensuring a consistent user experience from the smallest smartphone (minimum width 320px) to the largest desktop display. Navigation is made effortless with intuitive buttons, accessible at any point during the user's journey through the site. 

- **Navigation Bar Across All Pages:**
   ![The Navbar on desktop](readme-testing-files/readme/navbar-desktop.png "The Navbar on desktop")   

   - The Navbar is designed for flexibility, transforming into a hamburger menu on smaller screens for ease of use, and remains fixed at the top of the screen (sticky) for convenient navigation regardless of the user's position on the page.
   - Symmetrically centered at the top, the logo acts as a beacon, always ready to guide users back to the homepage.
   - The search box is strategically placed on the left within the Navbar to facilitate quick keyword searches from the outset.
   - Sign In/Register buttons are prominently located at the top-right corner for unregistered users, unfolding options for either action. This area transforms into a My Account dropdown upon logging in, offering direct links to the user's profile and log-out function.
   - Quick-access links to Favorites and Shopping Bag are embedded within the Navbar, ensuring they're always within reach, no matter where users find themselves on the site.
   - Navigation links are provided for all product categories and subcategories: All Products, Women, Men, Kids, Accessories, and Sale.
   - A persistent sales banner positioned just below the Navbar alerts users to free delivery options, visible on every page for constant visibility.

- **Footer Accessible on All Pages:** 
   ![The Footer on desktop](readme-testing-files/readme/footer-desktop.png "The Footer on desktop") 
   The Footer mirrors the Navbar's color scheme for design continuity and houses all navigational links, social media connections (which open in a new tab), and the central logo that circles back to the Home page when clicked. 

- **Toast Notifications:**   
Toast notifications serve as an interactive feedback mechanism for users, confirming the success or alerting to the failure of their actions. These notifications are color-coded for clarity: red signifies errors, blue for informational alerts, yellow for warnings, and green indicates successful actions. Typically, users will encounter the green success toasts most frequently, such as when adding items to the shopping bag, complemented by a visual cue of the bag itself. For other successful actions like adding items to the favorites list, a success toast appears sans the bag icon. Here are examples of the success toast notifications, with and without the bag icon display.   
![Success toast message - without bag display](readme-testing-files/readme/toast-success-nobag.png "Success toast message - without bag display")
![Success toast message - with bag display](readme-testing-files/readme/toast-success.png "Success toast message - with bag display")   


### **B. Page Features**  
#### **1. Home Page**  
[View the Homepage layout here](readme-testing-files/readme/home-page.png)   
- The Home page engages visitors immediately with a dynamic array of images, serving as a visual lure to explore further and encouraging purchases.
- A full-screen hero image sets a striking tone, featuring a prominent jumbotron heading that delivers a memorable first impression. This element highlights the latest seasonal offerings, along with a call-to-action (CTA) button that guides users straight to the new arrivals. 
- A dedicated section for the Sneakers Collection offers swift access to these products.
- 'Shoes for Every Family Member' section simplifies navigation by dividing the offerings into categories: Women, Men, and Kids.
- 'Top Sellers' showcases the most frequently purchased items, hinting at popular choices among consumers, presented in a carousel format that displays eight products at a time.
- Final Sale' acts as a portal to discounted items, making bargain deals easily accessible.
- 'Bags and Accessories' directs shoppers to a curated selection of related items.
- The 'Articles and Blogs' area introduces the three most recent pieces from the store's admin or selected superusers, with an additional option to 'See More Articles', leading to a comprehensive view of all available content.

#### **2. Products Page Overview**  
[View the Products Page layout here](readme-testing-files/readme/products.png)   
- At the top of the Products page, users are greeted with breadcrumb navigation, which aids in tracking their journey through the site - for instance, selecting Women Sneakers displays: Home > Women > Sneakers.
- Prominently placed beneath the breadcrumb is a 'Final Sale' banner, catering to users' propensity to browse sale items initially. The 'shop now' button on this banner filters the view to showcase only items on sale.
- An exclusive desktop feature, the Side Navigation, allows for swift perusal of categories and subcategories, filtering the display to the user's specific interests. On mobile devices, this functionality is available via the hamburger menu.
- Users can also sort the displayed product results by price, rating, or name, enabling them to find products that meet their preferences more efficiently.
- The display of products is responsively designed, with 4 columns on large screens, 3 on medium-sized screens, and 2 on smaller screens, ensuring a cohesive visual experience across devices.
- Each product image is equipped with a heart icon in the top right corner, which fills in red upon hover. This interactive feature allows registered users to add products to their favorites with a single click, with the heart icon remaining red to signify its status as a favored item.
- For added convenience, a 'back to top' button is fixed on the right side of the screen, providing quick and easy navigation back to the top of the page.

#### **3. Individual Product Page**  
[View the Individual Product Page layout here](readme-testing-files/readme/individual-product-page.png)  
- At the outset, users are greeted by a breadcrumb trail, aiding in the understanding of the page’s position within the site's structure. 
- The page prominently displays the product's imagery, name, cost, ratings, category, and user reviews at the lower section. 
- A heart icon, placed near the top right of the product image, signals a feature for registered users to add the item to their favorites; this icon highlights in red upon interaction and remains red once the product is in the user's favorites.
- The option to add the product to the shopping bag is straightforward: select the size, determine the quantity, and click the 'Add to Bag' button.
- Registered users possess the unique capability to modify or remove their reviews, with 'edit' and 'delete' options conveniently located below the review they posted.

#### **4. Favorites Page**  
[View the Favorites Page layout here](readme-testing-files/readme/favorites-page.png)  
- The Favorites interface showcases a user's selected products, echoing the layout of the main product page with the item's image, name, price, and rating. These items are arranged into a responsive grid that adjusts across devices: four columns on large screens, three on medium, and two on small screens.
- Product interaction is refined on this page, with the heart icon replaced by a trash icon on the upper right of each product image, indicating the ability to remove items from favorites.
- Acknowledging the Favorites as a curated collection of items users are considering for purchase, there is a direct option to select sizes and an 'Add to Bag' button beneath each item, streamlining the process of transferring favorites directly to the shopping bag without visiting the product's individual page.

#### **5. Shopping Bag Page**  
[View the Bag page here](readme-testing-files/readme/bag-page.png)  
- The Shopping Bag interface displays all items a user has added to their cart, along with the total cost, allowing for adjustments in quantity or removal of items directly on this page.
- Detailed product information is presented, including the image, name, SKU, price, selected size, and chosen quantity.
- An intuitive trash icon adjacent to each item offers a clear call to action to remove products from the bag.
- The subtotal for each product is dynamically updated based on the chosen quantity, enhancing the user's understanding of the cost breakdown.
- Crucial checkout information, including the itemized total, delivery charges, and grand total, is distinctly separated within a dedicated box to draw attention to the final cost and next steps. This section also includes a conspicuous 'Checkout' call-to-action button and graphical representation of accepted payment methods.
- For users wishing to continue shopping, a 'Keep Shopping' button is conveniently placed below the grand total box as an alternative action.

#### **6. Checkout Page**  
[View the Checkout Page here](readme-testing-files/readme/checkout-page.png)  
The Checkout page is designed for efficiency and ease, consisting of a form for processing transactions and displaying order details. The form is intuitively organized into three distinct sections for simplicity: 'Details' for the user's name and email, 'Delivery' for the address, and 'Payment' for card information. A summary of products selected on the Bag page, along with the total amount due, is also prominently featured. To facilitate a smooth transaction, call-to-action (CTA) buttons are strategically placed to prompt payment and finalize the purchase or to provide an option to modify the bag contents.

#### **7. Checkout Success Page**   
[View the Checkout Sucess Page here](readme-testing-files/readme/checkout-success-page.png)  
Upon successful transaction processing, the Checkout Success page presents a detailed summary of the completed order. Here, users can review their order specifics, including the list of items purchased, the delivery address, and the billing details. For registered users, this summary is also accessible through their Profile page, enabling them to track and reference their orders conveniently.

#### **8. Profile Page - My Information**  


#### **9. Profile Page - My Purchases**  


#### **10. Profile Page - Ratings/Reviews**  













