const express = require("express");
const cors = require('cors');
const morgan = require('morgan');
const bodyParse = require("body-parser");
const routers = require("./../src/routes");

const app = express();
app.use(morgan('dev'));
app.use(cors());
app.use(express.json());
app.use(bodyParse.urlencoded({extended: false}));

app.use(routers);

module.exports = app;