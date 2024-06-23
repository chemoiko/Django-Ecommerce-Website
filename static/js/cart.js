var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++){     //adds an event listener to each button with the class update-cart. When one of these buttons is clicked, it logs the productId and action values stored in the button's data-* attributes. Here's an explanation and a more complete example:
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('USER:', user)      //this logs the current user
        if(user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action) {       //send a POST request to the update_item/ URL with JSON data (productId and action), handle the response, and reload the page upon success. Adjust the function further based on your specific application requirements and error handling needs.
    console.log('User is logged in, sending data..');
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'productId': productId,
            'action': action
        })
    })
    .then(response =>{ return response.json()})
    .then(data => {
        console.log('data:', data);
        location.reload();  // Reload the page after updating
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors if necessary
    });
}
