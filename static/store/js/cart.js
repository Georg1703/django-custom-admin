var updateBtns = document.getElementsByClassName('update-cart')
var quantityBtns = document.getElementsByName('quantity')


for (var i = 0; i < updateBtns.length; i++) {
      updateBtns[i].addEventListener('click', function(){
        var action = this.dataset.action;
        var productId = this.dataset.product;

        if (user === 'AnonymousUser'){
            MicroModal.show('modal-1');
        } else {
            updateUserOrder(productId, action)
        }
      });
}


for (var i = 0; i < quantityBtns.length; i++) {
    quantityBtns[i].addEventListener('change', function (){
        var productId = this.dataset.product;
        var quantity = this.value
        updateUserOrder(productId, 'set_quantity', quantity)
    })
}


function updateUserOrder(productId, action, quantity = 0){

    var url = '/update_item/'

    if (action == 'remove_all') {
        url = '/remove_all_items/'
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action, 'quantity': quantity})
    })

        .then((response) =>{
            return response.json()
        })

        .then((data) => {
            renderOrder(data)
        })
}


