import { Gift } from "./Clase.js";
let giftIdToUpdate = null;

let data = [
    {
        id: 1,
        gift: "Crunchyroll",
        type: "Subscription",
        time: "1 year",
        price: 1500,
        image: "img"
    }
];

const tableBody = document.querySelector("#table-body");
const modal = new bootstrap.Modal(document.getElementById("modal-gift"));
const loadTable = () => {
    tableBody.innerHTML = "";

    data.map((item) => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${item.gift}</td>
            <td>${item.type}</td>
            <td>${item.time}</td>
            <td>$${item.price}</td>
            <td>
                <button class="btn btn-warning me-2" onclick="window.showEditModal(${item.id})">
                    <i class="fas fa-pencil-alt"></i>
                </button>

                <button class="btn btn-danger" onclick="window.deleteGift(${item.id})">
                    <i class="fas fa-times"></i>
                </button>
            </td>
        `;

        tableBody.appendChild(row);
    });
};

loadTable();

window.deleteGift = (id) => {
    const index = data.findIndex(item => item.id === id);

    if (confirm(`Delete "${data[index].gift}"?`)) {
        data.splice(index, 1);
        loadTable();
    }
};

const formAdd = document.querySelector("#form-gift");
const btnClear = document.querySelector("#btn-clear");

formAdd.addEventListener("submit", addGift);

btnClear.addEventListener("click", () => {
    formAdd.reset(); // guaranteed to work now
});

function addGift(e) {
    e.preventDefault();

    const id = data.at(-1).id + 1;

    const gift = document.querySelector("#gift").value;
    const type = document.querySelector("#type").value;
    const time = document.querySelector("#time").value;
    const price = document.querySelector("#price").value;
    const image = document.querySelector("#image").value;

    data.push(new Gift(id, gift, type, time, price, image));

    formAdd.reset();
    loadTable();
}

window.showEditModal = (id) => {
    giftIdToUpdate = id;

    const index = data.findIndex(item => item.id === id);

    document.querySelector("#gift-modal").value = data[index].gift;
    document.querySelector("#type-modal").value = data[index].type;
    document.querySelector("#time-modal").value = data[index].time;
    document.querySelector("#price-modal").value = data[index].price;
    document.querySelector("#image-modal").value = data[index].image;

    modal.show();
};

const formModal = document.querySelector("#form-modal");
formModal.addEventListener("submit", updateGift);

function updateGift(e) {
    e.preventDefault();

    const index = data.findIndex(item => item.id === giftIdToUpdate);

    data[index].gift = document.querySelector("#gift-modal").value;
    data[index].type = document.querySelector("#type-modal").value;
    data[index].time = document.querySelector("#time-modal").value;
    data[index].price = document.querySelector("#price-modal").value;
    data[index].image = document.querySelector("#image-modal").value;

    loadTable();
    modal.hide();
}
