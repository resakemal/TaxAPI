**Tax API**
----
  API for storing and displaying tax amounts.
  
### API Documentation
  
1. Create Tax Object

* **URL**

  /tax

* **Method:**

  `POST`
  
* **URL Params** 

  None

* **Data Params** 
  
  `{
    u : {
      name : [string],
      tax_code : [numeric],
      price: [numeric]
    }
  }`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
      "name": "Tea",
      "tax_code": 1,
      "price": "15.00",
      "tax_type": "Food",
      "refundable": true,
      "tax_value": 1.5,
      "amount": 16.5
    }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "Unknown tax code" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/tax",
      dataType: "json",
      data : { 
        u: { 
          name : Tea,
          tax_code : 1,
          price: 15
        }
      },
      type : "POST",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
2. Display Tax Objects

* **URL**

  /tax

* **Method:**

  `GET`
  
* **URL Params** 

  None
  
* **Data Params** 

  None

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `[
      {
          "name": "Pizza",
          "tax_code": 1,
          "price": "100.00",
          "tax_type": "Food",
          "refundable": true,
          "tax_value": 10,
          "amount": 110
      },
      {
          "name": "Cigarettes",
          "tax_code": 2,
          "price": "50.00",
          "tax_type": "Tobacco",
          "refundable": false,
          "tax_value": 11,
          "amount": 61
      },
      {
        "total": {
          "price_total": 150,
          "tax_total": 21,
          "grand_total": 171
        }
      }
    ]`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/tax",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
### Database Structure

|   |  Column  |      Type      |
|---|----------|----------------|
| 1 |   name   |  varchar(256)  |
| 2 | tax_code |       int      |
| 3 |   price  |       int      |

* An assumption that duplicate tax objects with the same name and price is allowed is used.
* There is no range limitation on the tax_code column so that additional tax codes can be added.
