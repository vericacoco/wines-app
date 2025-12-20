db = db.getSiblingDB("wines_db");

db.wines.insertMany([
    {
        name: "Merlot Reserve",
        country: "France",
        type: "Red",
        price: 18.5,
        description: "Smooth red wine with berry notes"
    },
    {
        name: "Pinot Grigio",
        country: "Italy",
        type: "White",
        price: 12.0,
        description: "Fresh and light white wine"
    }
]);
