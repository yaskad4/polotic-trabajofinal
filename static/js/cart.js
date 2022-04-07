var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0 ; updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productID=this.dataset.product
        var action=this.dataset.action
        console.log('productID:', productID, 'Action:',action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('No esta logueado')
        }else{
            updateUserOrder(productID, action)
        }
    })
}


function updateUserOrder(productID, action) {
    console.log('usuario logueado, enviando data....')

    var url = 'update_item'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productID, 'action': action})
    
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
    })
}
