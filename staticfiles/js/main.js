const overlay = document.getElementById("overlay");
const modalBar = document.getElementsByClassName("modal-bar")[0];
const modalBody = document.getElementsByClassName("modal")[0];
const products = [...document.getElementsByClassName("details")];
const addButtons = [...document.getElementsByClassName("update-cart")];
const collections = [...document.getElementsByClassName("collection")];
const collectionOverlays = [
  ...document.getElementsByClassName("collection-overlay"),
];
const collectionButtons = [
  ...document.getElementsByClassName("collection-btn-flt"),
];

const faders = document.querySelectorAll(".fade-in");
const sliders = document.querySelectorAll(".slide-in");

window.onscroll = function () {
  scrollFunction();
};

for (let i = 0; i < collections.length; i++) {
  collections[i].onmouseover = function () {
    collectionOverlays[i].classList.add("active");
    collectionButtons[i].classList.add("active");
  };
  collections[i].onmouseout = function () {
    collectionOverlays[i].classList.remove("active");
    collectionButtons[i].classList.remove("active");
  };
}

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("logo").style.transform = "scale(0.7)";
    document.getElementsByTagName("header")[0].style.padding = "0.3rem 1.5rem";
    // var options = [...document.getElementsByClassName("options")];
    // options.forEach((option) => {
    //   option.style.transform = "scale(0.9)";
    // });
  } else {
    document.getElementById("logo").style.transform = "scale(1)";
    document.getElementsByTagName("header")[0].style.padding = "1rem 1.5rem";

    // var options = [...document.getElementsByClassName("options")];
    // options.forEach((option) => {
    //   option.style.transform = "scale(1)";
    // });
  }
}

overlay.addEventListener("click", () => {
  const modals = document.querySelectorAll(".modal.active");
  modals.forEach((modal) => {
    closeModal(modal);
  });
});

products.forEach((product) =>
  product.addEventListener("click", (e) => {
    var dataID = product.getAttribute("data-product");
    var dataName = product.getAttribute("data-name");
    var dataImage = product.getAttribute("data-img");
    var dataPrice = product.getAttribute("data-price");
    var dataDesc = product.getAttribute("data-desc");
    modalBody.innerHTML = `
    <div class="modal-image-container">
        <img src="${dataImage} " alt="">
    </div>

    <div class="modal-info">

      <div class="modal-header">
        <button data-close-button="" class="close-button">&times;</button>
        <div class="modal-product-info">
            <h2 class="modal-title">${dataName} </h2>
            <img class="modal-image-min" src="${dataImage}" alt="">
        </div>
      </div>
        <hr style="width: 100%;  margin: 1rem 0rem;" />
        <div class="modal-body">
          <h4>Description produit :</h4>
            <P style="display: list-item;">${dataDesc}</p>
        </div>
        <hr style="width: 100%; margin: 1rem 0rem;" />
        <div class="modal-price">
          <h3>Price</h3>
          <h2>${dataPrice} €</h2>
        </div>

    </div>`;

    openModal(modal);

    const closeModalButtons = document.querySelectorAll("[data-close-button]");

    closeModalButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const modal = button.closest(".modal");
        closeModal(modal);
      });
    });
  })
);

addButtons.forEach((addButton) =>
  addButton.addEventListener("click", (e) => {
    var dataAction = addButton.getAttribute("data-action");
    var dataID = addButton.getAttribute("data-product");
    var dataName = addButton.getAttribute("data-name");
    var dataImage = addButton.getAttribute("data-img");
    var dataPrice = addButton.getAttribute("data-price");
    var dataDesc = addButton.getAttribute("data-desc");
    if(dataAction == 'add'){
      modalBar.innerHTML = `
      <img style="width: 50px; height: 50px; border-radius: 7px;" src="${dataImage} " alt="">
      <div style="height: min-content;" class="modal-title">${dataName} </div>
      <div style="color: var(--secondaryColor);"> Produit ajouté </div>
       `;
      openModalBar(modalBar);
    }

  })
);

function openModal(modal) {
  if (modal == null) return;
  modal.classList.add("active");
  overlay.classList.add("active");
}

function openModalBar(modalBar) {
  if (modalBar == null) return;
  modalBar.classList.add("active");
  setTimeout(function () {
    modalBar.className = modalBar.className.replace("active", "");
  }, 1500);
}

function closeModal(modal) {
  if (modal == null) return;
  modal.classList.remove("active");
  overlay.classList.remove("active");
}

const appearOptions = {
  threshold: 0,
  rootMargin: "0px 0px -250px 0px"
};

const appearOnScroll = new IntersectionObserver 
(function(
  entries,
  appearOnScroll
) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      return;
    } else {
      entry.target.classList.add("appear");
      appearOnScroll.unobserve(entry.target)
    }
  })
}, 
appearOptions);

faders.forEach(fader => {
  appearOnScroll.observe(fader);
})

sliders.forEach(slider => {
  appearOnScroll.observe(slider)
})

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("header").style.top = "0";
  } else {
    document.getElementById("header").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}
