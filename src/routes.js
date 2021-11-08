const route = require("./../.init/express-router");
const AuthController = require("./controllers/authController");
const SinglePorts = require("./controllers/SinglePorts");

const importe = {
  singlePorts: new SinglePorts(),
  authController: new AuthController()
}

route.post("/single-ports-check", importe.authController.checkLoginKey, importe.singlePorts.singlePortScan);
route.post("/check-history-port", importe.authController.checkLoginKey, importe.singlePorts.checkHistoryPorts);
route.post("/check-history-por-advanced", importe.authController.checkLoginKey, importe.singlePorts.checkHistoryPortsAdvanced);

module.exports = route;