/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Montserrat", sans-serif',
        fontSize: '16px',
        '::label': {
            color: '#9baec2'
        }
    },
    invalid: {
        color: '#b0736b',
        iconColor: '#9c303b'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');