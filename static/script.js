document.addEventListener('DOMContentLoaded', function() {
    var clearButton = document.getElementById('clear-predictions');
    var predictionTable = document.getElementById('prediction-table');
    var currentPriceElement = document.getElementById('price');

    // Function to fetch the current Bitcoin price
    function updateCurrentPrice() {
        fetch('/current_price')
            .then(response => response.json())
            .then(data => {
                currentPriceElement.textContent = '$' + data.price.toFixed(2);
            })
            .catch(error => {
                console.error('Error fetching current price:', error);
            });
    }

    // Update the current price immediately and then every 5 seconds
    updateCurrentPrice();
    setInterval(updateCurrentPrice, 5000);

    if (clearButton) {
        clearButton.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the form from submitting
            // Clear the content of the prediction table
            predictionTable.innerHTML = '';
        });
    }
});