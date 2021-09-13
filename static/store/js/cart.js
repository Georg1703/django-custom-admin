var updateBtns = document.getElementsByClassName('update-cart')
var placeOrderBtn = document.getElementById('place_order')

for (var i = 0; i < updateBtns.length; i++) {
      updateBtns[i].addEventListener('click', function(){
        var action = this.dataset.action;
        var productId = this.dataset.product;

        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        } else {
            updateUserOrder(productId, action)
        }
      });
}

placeOrderBtn.addEventListener('click', function (){
    var order_code = this.dataset.order;

    var url = '/place_order/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'order_code': order_code})
    })

        .then((response) =>{
            return response.json()
        })

        .then((data) => {
            if (data.message == 'success') {
                renderOrder({
                    'quantity': 0,
                    'total_quantity': 0,
                    'get_order_total':  0,
                    'product_total_price': 0,
                    'is_deleted': false,
                    'delete_all': true
                })
            }
        })

});


function updateUserOrder(productId, action){
    console.log('User in logged in, sending data ...')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

        .then((response) =>{
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
            renderOrder(data)
        })
}


function renderOrder(data){
    if (product_price = document.getElementById('quantity_' + data.product_id)) {
        product_price.value = data.quantity
    }

    if (product_total_price = document.getElementById('product_' + data.product_id + '_total_price')) {
        product_total_price.innerHTML = data.product_total_price
    }

    $('.total_quantity').each(function(i, obj) {
        obj.innerHTML = data.total_quantity
    });

    $('.total_price').each(function(i, obj) {
        obj.innerHTML = data.get_order_total
    });

    if (data.is_deleted) {
        $('#order_item_' + data.product_id).remove()
        $('#cart_item_' + data.product_id).remove()
    } else if(data.delete_all) {
        order_body = document.getElementById('order_body')
        cart_body = document.getElementById('cart_body')
        order_body.innerHTML = ''
        cart_body.innerHTML = ''
    }
}


