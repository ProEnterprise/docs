<!-- add-breadcrumbs -->
# Delivery Note

A Delivery Note is made when a shipment is shipped from the company’s
Warehouse.

A copy of the Delivery Note is usually sent with the transporter. The Delivery
Note contains the list of Items that are sent in the shipment and updates the
inventory.

The entry of the Delivery Note is very similar to a Purchase Receipt. You can
create a new Delivery Note from:

> Stock > Delivery Note > New

or from a “Submitted” Sales Order (that is not already shipped) by clicking on
“Make Delivery Note”.

<img class="screenshot" alt="Delivery Note" src="/docs/assets/img/stock/delivery-note.png">

You can also “fetch” the details from an unshipped Sales Order.

You will notice that all the information about unshipped Items and other
details are carried over from your Sales Order.

### Shipping Packets or Items with Product Bundle

If you are shipping Items that have a [Product Bundle](/docs/user/manual/en/selling/setup/product-bundle.html), Pro Enterprise ERP will automatically
create a “Packing List” table for you based on the sub-Items in that Item.

If your Items are serialized, then for Product Bundle type of Items, you will have
to update the Serial Number in the “Packing List” table.

### Packing Items into Cases, for Container Shipment

If you are doing container shipment or by weight, then you can use the Packing
Slip to breakup your Delivery Note into smaller units. To make a Packing Slip
go to:

> Stock > Packing Slip > New Packing Slip

You can create multiple Packing Slips for your Delivery Note and Pro Enterprise ERP will
ensure that the quantities in the Packing Slip do not exceed the quantities in
the Delivery Note.

* * *

#### Q. How to Print Without Amounts?

If you want to print your Delivery Notes without the amount (this might be
useful if you are shipping high value items), just check the “Print without
Amount” box in the “More Info” section.

#### What happens when the Delivery Note is “Submitted”?

A Stock Ledger Entry is made for each Item and stock is updated. Pending
Quantity in the Sales Order is updated (if applicable).

{next}
