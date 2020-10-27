const express = require('express');
const router = express.Router();

var data = {};

router.get('/', (req, res, next) => {
    res.send({
        message: 'Handling GET requests to /products',
        method: 'GET',
        data: data
    },200);   
});

router.post('/:productId/:productName', (req, res, next) => {
    data[req.params.productId] = req.params.productName;
    res.send({
        message: 'Handling POST requests to /products',
        method: 'POST'
    },201);
});

router.get('/:productId', (req, res, next) => {
    res.send({
        message: 'Retrieving your order',
        id: req.params.productId,
        data: data[req.params.productId],
        method: 'GET'
    },200);
});

router.patch('/:productId', (req, res, next) => {
    res.send({
        message: 'Updated product!',
        method: 'PATCH'
    },200);
});

router.delete('/:productId', (req, res, next) => {
    res.send({
        message: 'Deleted product!',
        method: 'DELETE'
    },200);
});

module.exports = router;