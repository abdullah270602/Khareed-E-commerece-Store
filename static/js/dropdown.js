document.addEventListener("DOMContentLoaded", function() {
    const dropdownButton = document.getElementById("dropdownDefaultButton");
    const dropdownMenu = document.getElementById("dropdown");
    
    dropdownButton.addEventListener("click", function() {
      dropdownMenu.classList.toggle("hidden");
    });
  });
  