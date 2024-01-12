# **Footwear Fusion**
![Footwear Fusion website in variouse devices](readme-testing-files/readme/main-image.png "Footwear Fusion website in variouse devices")

[View live website here]()
</br>  

**Table of Contents**   

## Introduction
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




