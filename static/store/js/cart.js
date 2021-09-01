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
            location.reload()
        })
}