function decreaseQuantity() {
  const quantityInput = document.getElementById("quantityInput");
  if (quantityInput.value > 1) {
    quantityInput.value = parseInt(quantityInput.value) - 1;
  }
}

function increaseQuantity() {
  const quantityInput = document.getElementById("quantityInput");
  quantityInput.value = parseInt(quantityInput.value) + 1;
}
