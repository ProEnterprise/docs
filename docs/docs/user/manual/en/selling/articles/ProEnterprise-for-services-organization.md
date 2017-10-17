#Pro Enterprise ERP for Service Organization

**Question:** Pro Enterprise ERP looks primarily designed for the traders and manufacturers. Is Pro Enterprise ERP used by companies offering servies?

**Answer:**

About 30% of Pro Enterprise ERP customers are companies into services. These are companies into software development, certification services, individual consultants and many more. Being into service business ourselves, we use Pro Enterprise ERP to manage our sales, accounting, support and HR operations. Check following video to learn how Pro Enterprise ERP uses Pro Enterprise ERP.

<iframe width="640" height="360" src="//www.youtube.com/embed/b6r7WxJMfFA" frameborder="0" allowfullscreen=""></iframe>

###Master Setup

The setup for a Service company differs primarily for Items. They don't maintain the Stock for Items and thus, don't have Warehouses.

To create a Service (non-stock) Item, in the item master, uncheck "Maintain Stock" field.

<img alt="Service Item" class="screenshot"  src="/docs/assets/img/articles/services-1.png">

When creating Sales Order for the services, select Order Type as **Maintenance**. Sales Order of Maintenance Type needs lesser details compared to stock item's order like Delivery Note, item warehouse etc.

Service company can still add stock items to mantain their fixed assets like computers, furniture and other office equipments.

###Hiding Non-required Features

Since many modules like Manufacturing and Stock will not be required for the services company, you can hide those modules from:

`Setup > Permissions > Show/Hide Modules`

Modules unchecked here will be hidden from all the User.

####Feature Setup

Within the form, there are many fields only needed for companies into trading and manufacturing businesses. These fields can be hidden for the service company. Feature Setup is a tool where you can enable/disable specific feature. If a feature is disabled, then fields relevant to that feature is hidden from all the forms. For example, if Serial No. feature is disabled, then Serial. No. field from Item as well as from all the sales and purchase transaction will be hidden.

[To learn more about Feature Setup, click here.](/docs/user/manual/en/customize-ProEnterprise/hiding-modules-and-features.html).

####Permissions

Pro Enterprise ERP is the permission controlled system. Users access system based on permissions assigned to them. So, if user is not assigned Role related to Stock and Manufacturing module, it will be hidden from that User. [Click here to learn more about permission management.](/docs/user/manual/en/setting-up/users-and-permissions.html).

You can also refer to help video on User and Permissions setting in Pro Enterprise ERP.

<iframe width="660" height="371" src="https://www.youtube.com/embed/fnBoRhBrwR4" frameborder="0" allowfullscreen></iframe>

<!-- markdown -->