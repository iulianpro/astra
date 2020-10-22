window.onload = function (e) {
    e.preventDefault();
    document.getElementById('checkout-button-price_1HcCdzJbpvQJZF24DWRFS1ZR').click();
};

(function () {
    var stripe = Stripe('pk_test_k3O0mK6VTkLOEZudObnpG2Lf00Fm4Pg64e');

    var checkoutButton = document.getElementById('checkout-button-price_1HcCdzJbpvQJZF24DWRFS1ZR');
    checkoutButton.addEventListener('click', function () {
        // When the customer clicks on the button, redirect
        // them to Checkout.
        stripe.redirectToCheckout({
            lineItems: [{ price: 'price_1HcCdzJbpvQJZF24DWRFS1ZR', quantity: 1 }],
            mode: 'payment',
            // Do not rely on the redirect to the successUrl for fulfilling
            // purchases, customers may not always reach the success_url after
            // a successful payment.
            // Instead use one of the strategies described in
            // https://stripe.com/docs/payments/checkout/fulfill-orders
            successUrl: 'https://iulian.pro/success',
            cancelUrl: 'https://iulian.pro/canceled',
        })
            .then(function (result) {
                if (result.error) {
                    // If `redirectToCheckout` fails due to a browser or network
                    // error, display the localized error message to your customer.
                    var displayError = document.getElementById('error-message');
                    displayError.textContent = result.error.message;
                }
            });
    });
})();