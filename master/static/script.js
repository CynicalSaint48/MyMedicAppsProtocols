const menuIconButton = document.querySelector("[data-menu-icon-btn]");
const protoButton = document.querySelector("[data-proto-btn]");
const medsButton = document.querySelector("[data-meds-btn]");
const otherButton = document.querySelector("[data-other-btn]");
const sidebarState = document.querySelector("[data-sidebar-state");
const protoList = document.querySelector("[proto-list]");
const medsList = document.querySelector("[meds-list]");
const otherList = document.querySelector("[other-list]");
const modal = document.querySelector('.modal');
const openModal = document.querySelector('.pt-info-div2');
const closeModal = document.querySelector('.close-dialog-btn');

menuIconButton.addEventListener("click", () => {
    window.scrollTo(0, 0), sidebarState.classList.toggle("open"), $("#proto-id > ul").slideUp(), $("#meds-id > ul").slideUp(), $("#other-id > ul").slideUp();
})

protoButton.addEventListener("click", () => {
    if (sidebarState.classList.contains("open")) {
        if (protoList.style.display == 'none') {
            $("#proto-id > ul").slideDown(), $("#meds-id > ul").slideUp(), $("#other-id > ul").slideUp(), protoList.style.display = 'block';
        } else {
            $("#proto-id > ul").slideUp(), $("#meds-id > ul").slideUp(), $("#other-id > ul").slideUp();
        }
    } else {
            if (protoList.style.display == 'none') {
                sidebarState.classList.add("open"), $("#proto-id > ul").slideDown(), $("#meds-id > ul").slideUp(), $("#other-id > ul").slideUp(), protoList.style.display = 'block';
            } else {
                sidebarState.classList.add("open"), $("#proto-id > ul").slideUp();
            }
        }
})

medsButton.addEventListener("click", () => {
    if (sidebarState.classList.contains("open")) {
        if (medsList.style.display == 'none') {
            $("#meds-id > ul").slideDown(), $("#proto-id > ul").slideUp(), $("#other-id > ul").slideUp(), medsList.style.display = 'block';
        } else {
            $("#meds-id > ul").slideUp(), $("#proto-id > ul").slideUp(), $("#other-id > ul").slideUp();
        }
    } else {
            if (medsList.style.display == 'none') {
                sidebarState.classList.add("open"), $("#meds-id > ul").slideDown(), $("#proto-id > ul").slideUp(), $("#other-id > ul").slideUp(), medsList.style.display = 'block';
            } else {
                sidebarState.classList.add("open"), $("#meds-id > ul").slideUp();
            }
        }
})

otherButton.addEventListener("click", () => {
    if (sidebarState.classList.contains("open")) {
        if (otherList.style.display == 'none') {
            $("#other-id > ul").slideDown(), $("#proto-id > ul").slideUp(), $("#meds-id > ul").slideUp(), otherList.style.display = 'block';
        } else {
            $("#other-id > ul").slideUp(), $("#proto-id > ul").slideUp(), $("#meds-id > ul").slideUp();
        }
    } else {
            if (otherList.style.display == 'none') {
                sidebarState.classList.add("open"), $("#other-id > ul").slideDown(), $("#proto-id > ul").slideUp(), $("#meds-id > ul").slideUp(), otherList.style.display = 'block';
            } else {
                sidebarState.classList.add("open"), $("#other-id > ul").slideUp();
            }
        }
})

openModal.addEventListener('click', () => {
    modal.showModal();
})

closeModal.addEventListener('click', () => {
    modal.close();
})