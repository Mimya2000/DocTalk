const menu = [
  {
    id: 1,
    title: "Dr. Zabir Raihan",
    category: "Immunologist",
    img: "./images/item-1.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.`,
  },
  {
    id: 2,
    title: "Dr. Selim Khan",
    category: "Meidicine",
    img: "./images/item-2.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. `,
  },
  {
    id: 3,
    title: "Dr. Shirin Afrin",
    category: "Neurologist",
    img: "./images/item-3.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`,
  },
  {
    id: 4,
    title: "Dr. Afsana Islam",
    category: "Immunologist",
    img: "./images/item-4.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. `,
  },
  {
    id: 5,
    title: "Dr. Akib Javed",
    category: "Meidicine",
    img: "./images/item-5.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. `,
  },
  {
    id: 6,
    title: "Dr. Humayon Kabir",
    category: "Neurologist",
    img: "./images/item-6.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`,
  },
  {
    id: 7,
    title: "Dr. Reja Shahriar",
    category: "Immunologist",
    img: "./images/item-7.jpg",
    desc: `carry jianbing normcore freegan. Viral single-origin coffee live-edge, pork belly cloud bread iceland put a bird `,
  },
  {
    id: 8,
    title: "Dr. Kaisar Hamid",
    category: "Meidicine",
    img: "./images/item-8.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. `,
  },
  {
    id: 9,
    title: "Dr. Kusum Sikder",
    category: "Neurologist",
    img: "./images/item-9.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`,
  },
  {
    id: 10,
    title: "Dr. Raihan Rashid",
    category: "Psychiatrist",
    img: "./images/item-10.jpg",
    desc: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`,
  },
];
// get parent element
const sectionCenter = document.querySelector(".section-center");
const btnContainer = document.querySelector(".btn-container");
// display all items when page loads
window.addEventListener("DOMContentLoaded", function () {
  diplayMenuItems(menu);
  displayMenuButtons();
});

function diplayMenuItems(menuItems) {
  let displayMenu = menuItems.map(function (item) {
    // console.log(item);

    return `<article class="menu-item">
          <img src=${item.img} alt=${item.title} class="photo" />
          <div class="item-info">
            <header>
              <h4>${item.title}</h4>
            </header>
            <p class="item-text">
              ${item.desc}
            </p>
          </div>
        </article>`;
  });
  displayMenu = displayMenu.join("");
  // console.log(displayMenu);

  sectionCenter.innerHTML = displayMenu;
}
function displayMenuButtons() {
  const categories = menu.reduce(
    function (values, item) {
      if (!values.includes(item.category)) {
        values.push(item.category);
      }
      return values;
    },
    ["all"]
  );
  const categoryBtns = categories
    .map(function (category) {
      return `<button type="button" class="filter-btn" data-id=${category}>
          ${category}
        </button>`;
    })
    .join("");

  btnContainer.innerHTML = categoryBtns;
  const filterBtns = btnContainer.querySelectorAll(".filter-btn");
  console.log(filterBtns);

  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      // console.log(e.currentTarget.dataset);
      const category = e.currentTarget.dataset.id;
      const menuCategory = menu.filter(function (menuItem) {
        // console.log(menuItem.category);
        if (menuItem.category === category) {
          return menuItem;
        }
      });
      if (category === "all") {
        diplayMenuItems(menu);
      } else {
        diplayMenuItems(menuCategory);
      }
    });
  });
}
