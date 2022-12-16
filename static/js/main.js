// price slider fuction

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {
  output.innerHTML = this.value + " ETB";
};

// price slider END \\

// HIDDER FUNCTION

function advanceSearch() {
  const advanceButton = document.querySelector(".expand-icon");

  const toggler = document.querySelector(".advance-search");
  advanceButton.addEventListener("click", () => {
    toggler.classList.toggle("hidder");
  });
}

advanceSearch();

// HIDER FUNCTION END

// CANCEL BUTTON HANDLER

function cancel() {
  const cancelButton = document.querySelector(".cancel");

  const toggler = document.querySelector(".advance-search");
  cancelButton.addEventListener("click", () => {
    toggler.classList.toggle("hidder");
  });
}

cancel();

// END OF CANCEL BUTTON HANDELER

// atuo scroller to cathegories page

function explore() {
  const cancelButton = document.querySelector(".gotocategories");
  cancelButton.addEventListener("click", () => {
    window.scrollTo(0, 730);
  });
}

explore();
// end of auto scroller

// atuo scroller to about us ABOUTUS page

function exploreAbout() {
  const cancelButton = document.querySelector(".aboutus");
  cancelButton.addEventListener("click", () => {
    window.scrollTo(0, 1400);
  });
}

exploreAbout();
// end of auto scroller
