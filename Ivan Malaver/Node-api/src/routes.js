const express = require("express");
const router = express.Router();

let data = [
    { id: 1, name: "Sebas" },
    { id: 2, name: "Ivan" }
];

// GET ALL
router.get("/users", (req, res) => {
    res.json(data);
});

// GET ONE
router.get("/users/:id", (req, res) => {
    const user = data.find(u => u.id === Number(req.params.id));
    user ? res.json(user) : res.status(404).json({ error: "Not found" });
});

// POST
router.post("/users", (req, res) => {
    const newUser = { id: Date.now(), ...req.body };
    data.push(newUser);
    res.status(201).json(newUser);
});

module.exports = router;
