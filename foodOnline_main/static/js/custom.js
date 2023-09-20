let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_address'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "IN" - add your country code
        componentRestrictions: {'country': ['in']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_address').placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
}

$(document).ready(function(){
    $('.add_to_cart').on('click', function(e){
        e.preventDefault();

        food_id = $(this).attr('data-id');
        url = $(this).attr('data-url');

        data = {
            food_id: food_id,
        }

        $.ajax({
            type: 'GET',
            url: url,
            data: data,
            success: function(response){
                if(response.status == 'Success'){
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    $('#qty-' + food_id).html(response.qty);
                    
                    applyCartAmount(response.cart_amount['subtotal'], response.cart_amount['tax'], response.cart_amount['grand_total']);
                }else if(response. status == 'Login_required'){
                    Swal.fire(response.message, '', 'info').then(function(result){
                        if(result.isConfirmed){
                            window.location = '/login';
                        }
                    });
                }else{
                    Swal.fire(response.message, '', 'error');
                }
            }
        });
    });

    $('.decrease_cart').on('click', function(e){
        e.preventDefault();

        food_id = $(this).attr('data-id');
        url = $(this).attr('data-url');
        cart_id = $(this).attr('id')

        data = {
            food_id: food_id,
        }

        $.ajax({
            type: 'GET',
            url: url,
            data: data,
            success: function(response){
                if(response.status == 'Success'){
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    $('#qty-' + food_id).html(response.qty);
                    
                    applyCartAmount(response.cart_amount['subtotal'], response.cart_amount['tax'], response.cart_amount['grand_total']);

                    if(window.location.pathname == '/cart/'){
                        removeCartItem(response.qty, cart_id);
                        checkEmptyCart();
                    }
                }else if(response. status == 'Login_required'){
                    Swal.fire(response.message, '', 'info').then(function(result){
                        if(result.isConfirmed){
                            window.location = '/login';
                        }
                    });
                }else{
                    Swal.fire(response.message, '', 'error');
                }
            }
        });
    });


    $('.item-qty').each(function(){
        var the_id = $(this).attr('id');
        var qty = $(this).attr('data-qty');
        $('#' + the_id).html(qty);
    });

    
    $('.delete_cart').on('click', function(e){
        e.preventDefault();

        cart_id = $(this).attr('data-id');
        url = $(this).attr('data-url');

        $.ajax({
            type: 'GET',
            url: url,
            success: function(response){
                if(response.status == 'Success'){
                    $('#cart_counter').html(response.cart_counter['cart_count']);
                    Swal.fire(response.message, '', 'success');

                    applyCartAmount(response.cart_amount['subtotal'], response.cart_amount['tax'], response.cart_amount['grand_total']);
                    
                    removeCartItem(0, cart_id);
                    checkEmptyCart();
                }else{
                    Swal.fire(response.message, '', 'error');
                }
            }
        });
    });

    function removeCartItem(cartItemQty, cart_id){
        if(cartItemQty <= 0){
            document.getElementById('cart-item-' + cart_id).remove();
        }
    }

    function checkEmptyCart(){
        var cart_counter = document.getElementById('cart_counter').innerHTML
        if(cart_counter == 0){
            document.getElementById('emty-cart').style.display = 'block';
        }
    }

    function applyCartAmount(subtotal, tax, grand_total){
        if(window.location.pathname == '/cart/'){
            $('#subtotal').html(subtotal);
            $('#tax').html(tax);
            $('#total').html(grand_total);
        }
    }
});