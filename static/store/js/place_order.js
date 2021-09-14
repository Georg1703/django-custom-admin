var placeOrderBtn = document.getElementById('place_order')


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