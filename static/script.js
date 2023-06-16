
const addButton = document.getElementById('popover-bottom-close');
  const popover = document.getElementById('popover-bottom');
  
  addButton.addEventListener('click', () => {
    popover.classList.add('invisible');
  });

  document.addEventListener("DOMContentLoaded", function() {
    const yearElement = document.getElementById("year");
    const currentYear = new Date().getFullYear();
    yearElement.innerText = currentYear;
  });

