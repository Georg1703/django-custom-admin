var updateBtns = document.getElementsByClassName('update-cart')

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
            // location.reload()
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
    }
}