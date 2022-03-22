if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", ready);
} else {
  ready();
}

function ready() {
  var updateCartBtns = document.getElementsByClassName("update-cart");
  for (var i = 0; i < updateCartBtns.length; i++) {
    var updateCartBtn = updateCartBtns[i];
    updateCartBtn.addEventListener("click", updateCart);
  }

  var deleteBtns = document.getElementsByClassName("delete");
  for (var i = 0; i < deleteBtns.length; i++) {
    var deleteBtn = deleteBtns[i];
    deleteBtn.addEventListener("click", deleteRow);
  }
}

function updateCart() {
  console.log("USER : ", user);

  var productId = this.dataset.product;
  var action = this.dataset.action;

    if (action == "add") {
      try {
          this.parentElement.getElementsByClassName("item-quantity")[0].innerText =
          parseInt(this.parentElement.innerText.split("x")[1]) + 1;
          cartSubTotal(this);
          cartTotal();
      } catch(error) {
        console.log("Add from store (error passed out) ", error)
      } finally {
          cartTotalAdd();
          if (user == "AnonymousUser") {
            addCookieItem(productId, action);
          } else {
              updateUserOrder(productId, action);
          }
      }
    } else if (action == "remove") {
        if (parseInt(this.parentElement.getElementsByClassName("item-quantity")[0].innerText) != 1) {
                try {
                this.parentElement.getElementsByClassName("item-quantity")[0].innerText =
                parseInt(this.parentElement.innerText.split("x")[1]) - 1;
                cartSubTotal(this);
                cartTotal();
            } catch (error) {
                console.log("Add from store (error passed out) ", error)
            } finally {
                cartTotalRemove();
                if (user == "AnonymousUser") {
                    addCookieItem(productId, action);
                  } else {
                      updateUserOrder(productId, action);
                  }
            }
            }
            else console.log("Cant delete more items");
      }
      else if (action == "delete") {
        console.log("Delete row function");
        cartItemDeleted(this);
        deleteRow()
      }
}

function addCookieItem (productId, action) {
    console.log("User not logged in..");

    if (action == "add") {
        if (cart[productId] == undefined) {
            console.log("New product added");
            cart[productId] = {'quantity':1}
        } else {
            cart[productId]['quantity'] += 1
            console.log("Product quantity + 1");
        }
    }

    else if (action == "remove") {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 1) {
            console.log("Delete item")
            delete cart[productId]
        }
    }

    else if (action == "delete") {
        console.log("Item deleted")
        delete cart[productId]
    }
    console.log("Cart items : ", cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}

function deleteRow() {
  console.log("Delete row function");
  var productId = this.dataset.product;
  var action = this.dataset.action;
  cartItemDeleted(this);
  if (user == "AnonymousUser") {
    addCookieItem(productId, action);
  } else {
      updateUserOrder(productId, action);
  }
}

function updateUserOrder(productId, action) {
  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Data :", data);
      // location.reload();
    });
}

function cartTotalAdd() {
  document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText =
    parseInt(document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText) + 1;
}

function cartTotalRemove() {
  if (
    parseInt(document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText) >= 0
  ) {
    document.getElementsByClassName("cart-element")[0].innerText =
      parseInt(document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText) -
      1;
  }
}

function cartItemDeleted(elt) {
    var quantity = parseInt(
      elt.parentElement.parentElement
        .getElementsByClassName("quantity")[0]
        .getElementsByClassName("item-quantity")[0].innerText
    );
    document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText =
      parseInt(document.getElementsByClassName("cart-element")[0].getElementsByTagName('div')[0].innerText) -
      quantity;
  }

function cartSubTotal(elt) {
  var quantity = parseInt(
    [...elt.parentElement.getElementsByClassName("item-quantity")][0].innerText
  );
  var prices = parseFloat(
    [
      ...elt.parentElement.parentElement.getElementsByClassName("item-price"),
    ][0].innerText.split("$")[1]
  );
  elt.parentElement.parentElement.getElementsByClassName(
    "subtotal"
  )[0].innerText = (prices * quantity).toFixed(2);
}

function cartTotal() {
  var totalItems = [...document.getElementsByClassName("item-quantity")];
  var cartTotal = [...document.getElementsByClassName("subtotal")];

  var totalItemsNumber = 0;
  var cartTotalNumber = 0;

  totalItems.forEach((item) => {
    totalItemsNumber += parseInt(item.innerText);
  });

  cartTotal.forEach((total) => {
    cartTotalNumber += parseFloat(total.innerText);
  });

  console.log("Total items : ", totalItemsNumber);
  console.log("Cart total : ", cartTotalNumber.toFixed(2));

  document.getElementsByClassName("items")[0].innerText = totalItemsNumber;
  document.getElementsByClassName("cart-total")[0].innerText =
    cartTotalNumber.toFixed(2);
}
